---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Median Age (median_age) — US Census ACS (BigQuery) — County & State Demographics
description: Rank, filter, and aggregate by median age (median_age) using Google Cloud
  BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- median-age
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: median_age
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: years
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- oldest counties by median age
- youngest counties in the US
---

# Schema & Access

Provides SQL ranking and filtering for `median_age` (Median Age) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
