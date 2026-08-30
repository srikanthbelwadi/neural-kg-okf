---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: Lack of Health Insurance (ACCESS2_CrudePrev) — CDC PLACES Health Measures (BigQuery)
description: Rank, filter, and aggregate by lack of health insurance (ACCESS2_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- access2-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: ACCESS2_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- Which counties have the highest uninsured rate?
- rank counties by uninsured population
---

# Schema & Access

Provides SQL ranking and filtering for `ACCESS2_CrudePrev` (Lack of Health Insurance) over `bigquery-public-data.cdc_places.places_county_2023`.
