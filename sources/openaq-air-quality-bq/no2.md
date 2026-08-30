---
type: OpenAQ Global Air Quality (BigQuery) Measure (BigQuery)
title: Nitrogen Dioxide (NO2) (no2) — OpenAQ Global Air Quality (BigQuery)
description: Rank, filter, and aggregate by nitrogen dioxide (no2) (no2) using Google
  Cloud BigQuery.
tags:
- openaq-air-quality-bq
- bigquery
- ranking
- aggregate
- population
- no2
source: ./_access.md
bq:
  table: bigquery-public-data.openaq.global_air_quality
  field: no2
  entity_field: location
  entity_kind: location_name
  source: OpenAQ Global Air Quality (BigQuery)
  unit: ppm
representativeQueries:
- Which cities report highest NO2 levels?
---

# Schema & Access

Provides SQL ranking and filtering for `no2` (Nitrogen Dioxide (NO2)) over `bigquery-public-data.openaq.global_air_quality`.
