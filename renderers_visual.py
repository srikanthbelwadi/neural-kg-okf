#!/usr/bin/env python3
"""Visual Response Formatter for Neural KG / ARD / OKF.

Translates admitted query evidence into structured, interactive visual components:
- KPI / Metric Cards (animated primary stat, units, period, source badge)
- Interactive Data Tables (columns, rows, formatting, sortable, exportable)
- Dynamic Charts (Bar, Line, Area, Donut)
- Geographic Map specs (US States / Counties FIPS choropleths)
- Grant Graph Network nodes & edges (Funder -> Recipient)
- Infographic Summary Blocks
"""

import re
from typing import Any, Dict, List, Optional


def build_visual_payload(question: str, evidence: Any, answer_text: str) -> Dict[str, Any]:
    """Inspects evidence kind and shape to construct rich visual blocks."""
    blocks: List[Dict[str, Any]] = []
    
    if not evidence:
        return {"answer": answer_text, "blocks": blocks}

    kind = getattr(evidence, "kind", None) or (evidence.get("kind") if isinstance(evidence, dict) else "point")
    payload = getattr(evidence, "payload", None) or (evidence.get("payload", evidence) if isinstance(evidence, dict) else {})
    source = getattr(evidence, "source", None) or payload.get("source", "Data Source")
    measure = getattr(evidence, "measure", None) or payload.get("measure", "")
    unit = getattr(evidence, "unit", None) or payload.get("unit", "")
    currency = getattr(evidence, "currency", None) or payload.get("currency", "")
    period = getattr(evidence, "period", None) or payload.get("period", "")
    entity = getattr(evidence, "entity", None) or payload.get("entity", {})
    entity_label = entity.get("label", str(entity)) if isinstance(entity, dict) else str(entity or "")

    # 1. Point / Status queries -> KPI Metric Card
    if kind in ("point", "status", "keyed_read"):
        val = payload.get("value", payload.get("value_usd", payload.get("total_usd")))
        formatted_val = _format_value(val, unit, currency)
        
        blocks.append({
            "type": "kpi_card",
            "title": measure.title() if measure else entity_label,
            "entity": entity_label,
            "value": formatted_val,
            "raw_value": val,
            "unit": currency or unit,
            "period": period,
            "source": source,
            "provenance": payload.get("resource", payload.get("concept", ""))
        })

    # 2. Ranking / Population / List / BigQuery Server-Aggregate queries -> Data Table + Bar Chart
    elif kind in ("ranking", "population", "list", "server_aggregate", "aggregate"):
        rows = payload.get("rows", payload.get("items", payload.get("results", [])))
        if isinstance(rows, list) and len(rows) > 0:
            cols = _detect_columns(rows)
            formatted_rows = _format_rows(rows, cols)
            
            # Add Data Table Block
            blocks.append({
                "type": "data_table",
                "title": f"Top Results: {measure.title() if measure else 'Population Ranking'}",
                "columns": cols,
                "rows": formatted_rows,
                "total_count": len(rows),
                "source": source
            })

            # Add Bar / Column Chart Block if there are numeric values
            num_col = next((c for c in cols if c["type"] in ("number", "currency", "percentage") and c["key"] != "rank"), None)
            label_col = next((c for c in cols if c["type"] == "string"), cols[0] if cols else None)
            
            if num_col and label_col:
                chart_data = []
                for r in rows[:15]:
                    chart_data.append({
                        "label": str(r.get(label_col["key"], "")),
                        "value": _to_numeric(r.get(num_col["key"])),
                    })
                
                blocks.append({
                    "type": "bar_chart",
                    "title": f"{measure.title() if measure else num_col['label']} Comparison",
                    "x_key": "label",
                    "y_key": "value",
                    "unit": currency or unit or num_col.get("unit", ""),
                    "data": chart_data
                })

            # Check if FIPS/geo fields are present -> Choropleth Map Block
            geo_col = next((c for c in cols if "fips" in c["key"].lower() or "geo" in c["key"].lower()), None)
            if geo_col and num_col:
                geo_data = []
                for r in rows:
                    geo_data.append({
                        "fips": str(r.get(geo_col["key"], "")).zfill(5),
                        "name": str(r.get(label_col["key"], "")),
                        "value": _to_numeric(r.get(num_col["key"]))
                    })
                blocks.append({
                    "type": "geo_map",
                    "title": f"US Geographic Distribution ({measure.title() or num_col['label']})",
                    "metric_label": num_col["label"],
                    "unit": currency or unit,
                    "data": geo_data
                })

    # 3. Comparison queries (Entity A vs Entity B) -> Comparison Matrix + Dual KPI
    elif kind in ("comparison", "compare"):
        entities_data = payload.get("entities", payload.get("items", []))
        if isinstance(entities_data, list) and len(entities_data) >= 2:
            comp_items = []
            for item in entities_data:
                item_val = item.get("value", item.get("value_usd"))
                comp_items.append({
                    "entity": item.get("entity", {}).get("label", item.get("label", "Entity")),
                    "value": _format_value(item_val, unit, currency),
                    "raw_value": item_val,
                    "period": item.get("period", period),
                    "source": item.get("source", source)
                })
            
            blocks.append({
                "type": "comparison_card",
                "title": f"Comparison: {measure.title() if measure else 'Direct Compare'}",
                "items": comp_items,
                "unit": currency or unit
            })

    # 4. Timeseries queries -> Line / Trend Chart
    elif kind in ("timeseries", "trend"):
        points = payload.get("points", payload.get("series", payload.get("items", [])))
        if isinstance(points, list) and len(points) > 1:
            series_data = []
            for p in points:
                p_period = p.get("period", p.get("year", p.get("date", "")))
                p_val = _to_numeric(p.get("value", p.get("amount", 0)))
                series_data.append({"period": str(p_period), "value": p_val})
            
            # Sort by period
            series_data.sort(key=lambda x: str(x["period"]))
            
            blocks.append({
                "type": "timeseries_chart",
                "title": f"{entity_label} {measure.title() if measure else 'Historical Trend'}",
                "x_key": "period",
                "y_key": "value",
                "unit": currency or unit,
                "data": series_data
            })

    # 5. IRS 990 Grant Graph Queries -> Grant Flow & Network Block
    elif kind in ("grant_graph", "funder_network", "grants"):
        grants_list = payload.get("grants", payload.get("edges", payload.get("items", [])))
        direction = payload.get("direction", "funders" if "fund" in question.lower() else "recipients")
        
        if isinstance(grants_list, list) and len(grants_list) > 0:
            nodes = [{"id": "central", "label": entity_label, "type": "target", "value": 0}]
            links = []
            table_rows = []
            
            for i, g in enumerate(grants_list[:20]):
                partner_name = g.get("funder_name") or g.get("recipient_name") or g.get("name") or f"Org {i+1}"
                amount = _to_numeric(g.get("amount", g.get("grant_amount", 0)))
                purpose = g.get("purpose", "")
                year = g.get("year", period)
                
                node_id = f"node_{i}"
                nodes.append({"id": node_id, "label": partner_name, "type": "partner", "amount": amount})
                
                if direction == "funders":
                    links.append({"source": node_id, "target": "central", "amount": amount, "label": _format_currency(amount)})
                else:
                    links.append({"source": "central", "target": node_id, "amount": amount, "label": _format_currency(amount)})
                
                table_rows.append({
                    "organization": partner_name,
                    "amount": _format_currency(amount),
                    "year": year,
                    "purpose": purpose or "General Support"
                })

            blocks.append({
                "type": "grant_network",
                "title": f"IRS 990 Grant Graph ({'Top Funders' if direction == 'funders' else 'Top Recipients'} for {entity_label})",
                "central_entity": entity_label,
                "direction": direction,
                "nodes": nodes,
                "links": links
            })

            blocks.append({
                "type": "data_table",
                "title": f"Grant Distribution Details",
                "columns": [
                    {"key": "organization", "label": "Organization", "type": "string"},
                    {"key": "amount", "label": "Grant Amount", "type": "currency"},
                    {"key": "year", "label": "Tax Year", "type": "string"},
                    {"key": "purpose", "label": "Grant Purpose", "type": "string"}
                ],
                "rows": table_rows,
                "total_count": len(grants_list),
                "source": "IRS Form 990 Grant Graph"
            })

    return {
        "answer": answer_text,
        "blocks": blocks,
        "evidence_kind": kind,
        "source": source
    }


def _format_value(val: Any, unit: str = "", currency: str = "") -> str:
    if val is None or val == "":
        return "N/A"
    num = _to_numeric(val)
    if num is not None:
        if currency == "USD" or "$" in unit or "USD" in unit:
            return _format_currency(num)
        if unit == "%" or "percent" in unit.lower():
            return f"{num:,.2f}%" if isinstance(num, float) else f"{num}%"
        if isinstance(num, (int, float)):
            if num >= 1e9:
                return f"{num/1e9:,.2f}B {unit}".strip()
            if num >= 1e6:
                return f"{num/1e6:,.2f}M {unit}".strip()
            return f"{num:,.2f} {unit}".strip() if isinstance(num, float) else f"{num:,} {unit}".strip()
    return f"{val} {unit}".strip()


def _format_currency(num: float) -> str:
    if num >= 1e12:
        return f"${num/1e12:,.2f}T"
    if num >= 1e9:
        return f"${num/1e9:,.2f}B"
    if num >= 1e6:
        return f"${num/1e6:,.2f}M"
    if num >= 1e3:
        return f"${num:,.0f}"
    return f"${num:,.2f}"


def _to_numeric(val: Any) -> Optional[float]:
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        clean = re.sub(r"[^\d.-]", "", val)
        try:
            return float(clean)
        except ValueError:
            return None
    return None


def _detect_columns(rows: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    if not rows or not isinstance(rows[0], dict):
        return []
    
    first = rows[0]
    cols = []
    for k in first.keys():
        label = k.replace("_", " ").title()
        val = first[k]
        col_type = "string"
        if isinstance(val, (int, float)) or (isinstance(val, str) and _to_numeric(val) is not None and not k.endswith("id")):
            if any(term in k.lower() for term in ("usd", "dollar", "amount", "income", "revenue", "rent", "value", "cost", "fee")):
                col_type = "currency"
            elif any(term in k.lower() for term in ("rate", "percent", "pct", "prev")):
                col_type = "percentage"
            else:
                col_type = "number"
        cols.append({"key": k, "label": label, "type": col_type})
    return cols


def _format_rows(rows: List[Dict[str, Any]], cols: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    formatted = []
    for r in rows:
        item = {}
        for c in cols:
            k = c["key"]
            val = r.get(k)
            if c["type"] == "currency":
                num = _to_numeric(val)
                item[k] = _format_currency(num) if num is not None else str(val)
            elif c["type"] == "percentage":
                num = _to_numeric(val)
                item[k] = f"{num:.2f}%" if num is not None else str(val)
            elif c["type"] == "number":
                num = _to_numeric(val)
                item[k] = f"{num:,}" if num is not None else str(val)
            else:
                item[k] = str(val or "")
        formatted.append(item)
    return formatted
