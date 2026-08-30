---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Per Capita Income (income_per_capita) — US Census ACS (BigQuery) — County &
  State Demographics
description: Rank, filter, and aggregate by per capita income (income_per_capita)
  using Google Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- income-per-capita
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: income_per_capita
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: USD
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- highest per capita income counties in US
- rank US counties by per capita income
---

# Schema & Access

Provides SQL ranking and filtering for `income_per_capita` (Per Capita Income) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
