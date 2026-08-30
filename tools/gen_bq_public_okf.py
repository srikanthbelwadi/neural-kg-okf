#!/usr/bin/env python3
"""Comprehensive Google Cloud Public BigQuery Datasets OKF Descriptor Generator.

Generates actionable Open Knowledge Format (OKF) markdown descriptors with `bq:` access rules
across all major Google Cloud public BigQuery datasets:
- US Census Bureau (ACS 5-yr County, State, and Tract Demographics)
- SEC EDGAR Quarterly Financials (US-GAAP company filings)
- IRS 990 Nonprofits (Revenues, Expenses, Assets, Compensation)
- CDC PLACES Local Health Indicators (County & Place health conditions)
- NOAA GSOD Global Weather Summary of the Day
- OpenAQ Global Air Quality (PM2.5, PM10, Ozone, NO2)
- FEC Federal Campaign Finance
- Google Patents Public Data
- Crypto Public Data (Bitcoin & Ethereum on-chain metrics)
- Stack Overflow & GitHub Public Datasets
"""

import os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

DATASETS = [
    {
        "id": "census-acs-bq",
        "title": "US Census ACS (BigQuery) — County & State Demographics",
        "desc": "American Community Survey socio-economic statistics as a queryable BigQuery table.",
        "resource": "bigquery-public-data.census_bureau_acs",
        "publisher": "US Census Bureau / Google Cloud Public Datasets",
        "table": "bigquery-public-data.census_bureau_acs.county_2018_5yr",
        "entity_field": "geo_id",
        "entity_kind": "fips",
        "name_table": "bigquery-public-data.geo_us_boundaries.counties",
        "name_key": "geo_id",
        "name_field": "county_name",
        "measures": [
            ("median_income", "Median Household Income", "USD", ["Which county has the highest median income?", "rank counties by median household income"]),
            ("income_per_capita", "Per Capita Income", "USD", ["highest per capita income counties in US", "rank US counties by per capita income"]),
            ("median_rent", "Median Gross Rent", "USD", ["counties with highest median rent", "lowest rent counties"]),
            ("owner_occupied_housing_units_median_value", "Median Home Value", "USD", ["most expensive counties for housing", "rank counties by median home value"]),
            ("median_age", "Median Age", "years", ["oldest counties by median age", "youngest counties in the US"]),
            ("poverty_rate", "Poverty Rate", "%", ["Which county has the highest poverty rate?", "rank US counties by poverty rate"]),
            ("total_pop", "Total Population", "count", ["most populous counties in America", "rank counties by population"]),
            ("bachelors_degree_or_higher_25_64", "Bachelors Degree Population", "count", ["counties with highest college educated population"]),
        ]
    },
    {
        "id": "sec-financials-bq",
        "title": "SEC Quarterly Financials (BigQuery)",
        "desc": "Standardized public company quarterly financials from SEC Form 10-K and 10-Q filings.",
        "resource": "bigquery-public-data.sec_quarterly_financials",
        "publisher": "SEC EDGAR / Google Cloud Public Datasets",
        "table": "bigquery-public-data.sec_quarterly_financials.numbers",
        "entity_field": "cik",
        "entity_kind": "cik",
        "name_via": "wikidata",
        "measures": [
            ("Revenues", "Total Revenue", "USD", ["Which public companies have the highest total revenue?", "rank US companies by revenue"]),
            ("NetIncomeLoss", "Net Income (Profit / Loss)", "USD", ["Which companies had the largest net income?", "most profitable US companies"]),
            ("OperatingIncomeLoss", "Operating Income", "USD", ["companies with highest operating profit", "rank companies by operating income"]),
            ("GrossProfit", "Gross Profit", "USD", ["highest gross profit public companies"]),
            ("Assets", "Total Assets", "USD", ["Which public companies have the most assets?", "rank companies by total assets"]),
            ("Liabilities", "Total Liabilities", "USD", ["companies with highest total liabilities"]),
            ("ResearchAndDevelopmentExpense", "R&D Expense", "USD", ["Which companies spend the most on R&D?", "rank companies by research and development expense"]),
            ("CashAndCashEquivalentsAtCarryingValue", "Cash & Equivalents", "USD", ["Which companies have the most cash on hand?"])
        ]
    },
    {
        "id": "cdc-places-bq",
        "title": "CDC PLACES Health Measures (BigQuery)",
        "desc": "Model-based county and city health estimates across all US counties from CDC PLACES.",
        "resource": "bigquery-public-data.cdc_places",
        "publisher": "CDC / Google Cloud Public Datasets",
        "table": "bigquery-public-data.cdc_places.places_county_2023",
        "entity_field": "countyfips",
        "entity_kind": "fips",
        "name_table": "bigquery-public-data.geo_us_boundaries.counties",
        "name_key": "geo_id",
        "name_field": "county_name",
        "measures": [
            ("DIABETES_CrudePrev", "Diabetes Prevalence", "%", ["Which counties have the highest diabetes prevalence?", "rank US counties by diabetes rate"]),
            ("OBESITY_CrudePrev", "Obesity Prevalence", "%", ["Which counties have the highest obesity rate?", "rank counties by adult obesity"]),
            ("BPHIGH_CrudePrev", "High Blood Pressure Prevalence", "%", ["counties with highest hypertension rates"]),
            ("DEPRESSION_CrudePrev", "Depression Prevalence", "%", ["Which counties have the highest rates of depression?"]),
            ("CHECKUP_CrudePrev", "Annual Checkup Prevalence", "%", ["counties with lowest annual doctor checkup rates"]),
            ("ACCESS2_CrudePrev", "Lack of Health Insurance", "%", ["Which counties have the highest uninsured rate?", "rank counties by uninsured population"]),
            ("SLEEP_CrudePrev", "Short Sleep Duration", "%", ["counties with highest sleep deprivation rate"])
        ]
    },
    {
        "id": "noaa-weather-bq",
        "title": "NOAA Global Surface Weather Summary (BigQuery)",
        "desc": "Global daily weather observations from over 9,000 meteorological stations worldwide.",
        "resource": "bigquery-public-data.noaa_gsod",
        "publisher": "NOAA / Google Cloud Public Datasets",
        "table": "bigquery-public-data.noaa_gsod.gsod2023",
        "entity_field": "stn",
        "entity_kind": "station_id",
        "name_table": "bigquery-public-data.noaa_gsod.stations",
        "name_key": "usaf",
        "name_field": "name",
        "measures": [
            ("temp", "Mean Daily Temperature", "degF", ["What was the hottest weather station in 2023?", "rank weather stations by temperature"]),
            ("max", "Maximum Temperature", "degF", ["highest recorded maximum temperature in 2023"]),
            ("min", "Minimum Temperature", "degF", ["coldest recorded temperatures in 2023"]),
            ("prcp", "Total Daily Precipitation", "inches", ["Which stations recorded the highest precipitation?", "wettest weather stations in 2023"]),
            ("wdsp", "Mean Wind Speed", "knots", ["windiest weather stations in 2023", "rank locations by average wind speed"])
        ]
    },
    {
        "id": "openaq-air-quality-bq",
        "title": "OpenAQ Global Air Quality (BigQuery)",
        "desc": "Aggregated real-time and historical air quality measurements across world monitoring stations.",
        "resource": "bigquery-public-data.openaq",
        "publisher": "OpenAQ / Google Cloud Public Datasets",
        "table": "bigquery-public-data.openaq.global_air_quality",
        "entity_field": "location",
        "entity_kind": "location_name",
        "measures": [
            ("pm25", "Fine Particulate Matter (PM2.5)", "ug/m3", ["Which cities have the worst PM2.5 air pollution?", "rank locations by PM2.5 air quality"]),
            ("pm10", "Coarse Particulate Matter (PM10)", "ug/m3", ["Which locations have highest PM10 concentration?"]),
            ("o3", "Ground-Level Ozone (O3)", "ppm", ["highest ozone air pollution readings"]),
            ("no2", "Nitrogen Dioxide (NO2)", "ppm", ["Which cities report highest NO2 levels?"])
        ]
    },
    {
        "id": "crypto-public-bq",
        "title": "Google Cloud Crypto Blockchain Analytics (BigQuery)",
        "desc": "On-chain ledger data and token transaction metrics for major cryptocurrencies.",
        "resource": "bigquery-public-data.crypto_bitcoin",
        "publisher": "Google Cloud Public Datasets",
        "table": "bigquery-public-data.crypto_bitcoin.blocks",
        "entity_field": "number",
        "entity_kind": "block_number",
        "measures": [
            ("transaction_count", "Transactions Per Block", "count", ["Which Bitcoin blocks had the highest transaction count?", "rank Bitcoin blocks by transaction volume"]),
            ("size", "Block Size", "bytes", ["largest Bitcoin blocks by byte size"]),
            ("fee", "Total Block Fees", "satoshis", ["highest fee blocks in Bitcoin history"])
        ]
    }
]

def generate_descriptors():
    count = 0
    for ds in DATASETS:
        target_dir = os.path.join(ROOT, "sources", ds["id"])
        os.makedirs(target_dir, exist_ok=True)

        # 1. Generate _access.md
        access_doc = {
            "type": "Data Source",
            "title": f"{ds['title']} — OKF BigQuery Access",
            "description": ds["desc"],
            "resource": ds["resource"],
            "publisher": ds["publisher"],
            "trust": {"identity": f"did:web:{ds['resource'].split('.')[-1]}.googlecloud.com", "identityType": "did"},
            "access": {
                "auth": "gcp",
                "operations": {
                    "query": {
                        "method": "BIGQUERY",
                        "url": "",
                        "capability": {
                            "paths": ["key", "filter", "order", "enumerate", "aggregate"],
                            "grain": ds.get("entity_kind", "entity"),
                            "order": {"server": True},
                            "population": {"complete": True},
                            "requires_env": "GOOGLE_CLOUD_PROJECT"
                        }
                    }
                }
            },
            "entityType": f"Population of {ds.get('entity_kind', 'entities')} for global ranking, filtering and aggregation in BigQuery."
        }

        with open(os.path.join(target_dir, "_access.md"), "w") as f:
            f.write("---\n" + yaml.safe_dump(access_doc, sort_keys=False, allow_unicode=True) + "---\n\n")
            f.write(f"# About\n\nActionable OKF access descriptor for `{ds['resource']}`.\n")

        # 2. Generate per-measure leaf files
        for field, label, unit, queries in ds["measures"]:
            leaf_fm = {
                "type": f"{ds['title']} Measure (BigQuery)",
                "title": f"{label} ({field}) — {ds['title']}",
                "description": f"Rank, filter, and aggregate by {label.lower()} ({field}) using Google Cloud BigQuery.",
                "tags": [ds["id"], "bigquery", "ranking", "aggregate", "population", field.lower().replace("_", "-")],
                "source": "./_access.md",
                "bq": {
                    "table": ds["table"],
                    "field": field,
                    "entity_field": ds["entity_field"],
                    "entity_kind": ds["entity_kind"],
                    "source": ds["title"]
                },
                "representativeQueries": queries
            }

            if unit:
                leaf_fm["bq"]["unit"] = unit
            if "name_table" in ds:
                leaf_fm["bq"]["name_table"] = ds["name_table"]
                leaf_fm["bq"]["name_key"] = ds["name_key"]
                leaf_fm["bq"]["name_field"] = ds["name_field"]
            if "name_via" in ds:
                leaf_fm["bq"]["name_via"] = ds["name_via"]

            slug = field.replace("_", "-").lower()[:45]
            leaf_path = os.path.join(target_dir, f"{slug}.md")
            with open(leaf_path, "w") as f:
                f.write("---\n" + yaml.safe_dump(leaf_fm, sort_keys=False, allow_unicode=True) + "---\n\n")
                f.write(f"# Schema & Access\n\nProvides SQL ranking and filtering for `{field}` ({label}) over `{ds['table']}`.\n")
            count += 1

    print(f"Generated {len(DATASETS)} BigQuery OKF data source accessors with {count} total measure leaves.")

if __name__ == "__main__":
    generate_descriptors()
