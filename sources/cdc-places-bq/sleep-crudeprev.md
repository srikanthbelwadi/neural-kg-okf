---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: Short Sleep Duration (SLEEP_CrudePrev) — CDC PLACES Health Measures (BigQuery)
description: Rank, filter, and aggregate by short sleep duration (SLEEP_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- sleep-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: SLEEP_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- counties with highest sleep deprivation rate
---

# Schema & Access

Provides SQL ranking and filtering for `SLEEP_CrudePrev` (Short Sleep Duration) over `bigquery-public-data.cdc_places.places_county_2023`.
