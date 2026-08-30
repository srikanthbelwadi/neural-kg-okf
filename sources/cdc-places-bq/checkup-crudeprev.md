---
type: CDC PLACES Health Measures (BigQuery) Measure (BigQuery)
title: Annual Checkup Prevalence (CHECKUP_CrudePrev) — CDC PLACES Health Measures
  (BigQuery)
description: Rank, filter, and aggregate by annual checkup prevalence (CHECKUP_CrudePrev)
  using Google Cloud BigQuery.
tags:
- cdc-places-bq
- bigquery
- ranking
- aggregate
- population
- checkup-crudeprev
source: ./_access.md
bq:
  table: bigquery-public-data.cdc_places.places_county_2023
  field: CHECKUP_CrudePrev
  entity_field: countyfips
  entity_kind: fips
  source: CDC PLACES Health Measures (BigQuery)
  unit: '%'
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- counties with lowest annual doctor checkup rates
---

# Schema & Access

Provides SQL ranking and filtering for `CHECKUP_CrudePrev` (Annual Checkup Prevalence) over `bigquery-public-data.cdc_places.places_county_2023`.
