---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: Obesity Prevalence (OBESITY_CrudePrev) — CDC PLACES Health Measures (BigQuery)
description: Rank, filter, and aggregate by obesity prevalence (OBESITY_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- obesity-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: OBESITY_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- Which counties have the highest obesity rate?
- rank counties by adult obesity
---

# Schema & Access

Provides SQL ranking and filtering for `OBESITY_CrudePrev` (Obesity Prevalence) over `bigquery-public-data.cdc_places.places_county_2023`.
