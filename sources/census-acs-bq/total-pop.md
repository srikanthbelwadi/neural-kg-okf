---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Total Population (total_pop) — US Census ACS (BigQuery) — County & State Demographics
description: Rank, filter, and aggregate by total population (total_pop) using Google
  Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- total-pop
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: total_pop
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: count
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- most populous counties in America
- rank counties by population
---

# Schema & Access

Provides SQL ranking and filtering for `total_pop` (Total Population) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
