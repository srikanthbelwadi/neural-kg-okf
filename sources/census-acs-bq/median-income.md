---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Median Household Income (median_income) — US Census ACS (BigQuery) — County
  & State Demographics
description: Rank, filter, and aggregate by median household income (median_income)
  using Google Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- median-income
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: median_income
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: USD
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- Which county has the highest median income?
- rank counties by median household income
---

# Schema & Access

Provides SQL ranking and filtering for `median_income` (Median Household Income) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
