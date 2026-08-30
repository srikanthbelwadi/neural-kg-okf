---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Poverty Rate (poverty_rate) — US Census ACS (BigQuery) — County & State Demographics
description: Rank, filter, and aggregate by poverty rate (poverty_rate) using Google
  Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- poverty-rate
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: poverty_rate
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- Which county has the highest poverty rate?
- rank US counties by poverty rate
---

# Schema & Access

Provides SQL ranking and filtering for `poverty_rate` (Poverty Rate) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
