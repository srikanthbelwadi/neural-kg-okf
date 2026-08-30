---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Median Gross Rent (median_rent) — US Census ACS (BigQuery) — County & State
  Demographics
description: Rank, filter, and aggregate by median gross rent (median_rent) using
  Google Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- median-rent
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: median_rent
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: USD
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- counties with highest median rent
- lowest rent counties
---

# Schema & Access

Provides SQL ranking and filtering for `median_rent` (Median Gross Rent) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
