---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Net Income (Profit / Loss) (NetIncomeLoss) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by net income (profit / loss) (NetIncomeLoss)
  using Google Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- netincomeloss
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: NetIncomeLoss
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- Which companies had the largest net income?
- most profitable US companies
---

# Schema & Access

Provides SQL ranking and filtering for `NetIncomeLoss` (Net Income (Profit / Loss)) over `bigquery-public-data.sec_quarterly_financials.numbers`.
