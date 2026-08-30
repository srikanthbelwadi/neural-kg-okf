---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: Diabetes Prevalence (DIABETES_CrudePrev) — CDC PLACES Health Measures (BigQuery)
description: Rank, filter, and aggregate by diabetes prevalence (DIABETES_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- diabetes-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: DIABETES_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- Which counties have the highest diabetes prevalence?
- rank US counties by diabetes rate
---

# Schema & Access

Provides SQL ranking and filtering for `DIABETES_CrudePrev` (Diabetes Prevalence) over `bigquery-public-data.cdc_places.places_county_2023`.
