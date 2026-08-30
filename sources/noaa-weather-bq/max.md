---
type: NOAA Global Surface Weather Summary (BigQuery) Measure (BigQuery)
title: Maximum Temperature (max) — NOAA Global Surface Weather Summary (BigQuery)
description: Rank, filter, and aggregate by maximum temperature (max) using Google
  Cloud BigQuery.
tags:
- noaa-weather-bq
- bigquery
- ranking
- aggregate
- population
- max
source: ./_access.md
bq:
  table: bigquery-public-data.noaa_gsod.gsod2023
  field: max
  entity_field: stn
  entity_kind: station_id
  source: NOAA Global Surface Weather Summary (BigQuery)
  unit: degF
  name_table: bigquery-public-data.noaa_gsod.stations
  name_key: usaf
  name_field: name
representativeQueries:
- highest recorded maximum temperature in 2023
---

# Schema & Access

Provides SQL ranking and filtering for `max` (Maximum Temperature) over `bigquery-public-data.noaa_gsod.gsod2023`.
