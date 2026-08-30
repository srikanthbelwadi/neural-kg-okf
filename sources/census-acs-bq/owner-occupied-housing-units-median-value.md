---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Median Home Value (owner_occupied_housing_units_median_value) — US Census ACS
  (BigQuery) — County & State Demographics
description: Rank, filter, and aggregate by median home value (owner_occupied_housing_units_median_value)
  using Google Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- owner-occupied-housing-units-median-value
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: owner_occupied_housing_units_median_value
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: USD
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- most expensive counties for housing
- rank counties by median home value
---

# Schema & Access

Provides SQL ranking and filtering for `owner_occupied_housing_units_median_value` (Median Home Value) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
