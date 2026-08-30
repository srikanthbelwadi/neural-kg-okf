---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: High Blood Pressure Prevalence (BPHIGH_CrudePrev) — CDC PLACES Health Measures
  (BigQuery)
description: Rank, filter, and aggregate by high blood pressure prevalence (BPHIGH_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- bphigh-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: BPHIGH_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- counties with highest hypertension rates
---

# Schema & Access

Provides SQL ranking and filtering for `BPHIGH_CrudePrev` (High Blood Pressure Prevalence) over `bigquery-public-data.cdc_places.places_county_2023`.
