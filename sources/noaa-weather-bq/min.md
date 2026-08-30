---
type: NOAA Global Surface Weather Summary (BigQuery) Measure (BigQuery)
title: Minimum Temperature (min) — NOAA Global Surface Weather Summary (BigQuery)
description: Rank, filter, and aggregate by minimum temperature (min) using Google
  Cloud BigQuery.
tags:
- noaa-weather-bq
- bigquery
- ranking
- aggregate
- population
- min
source: ./_access.md
bq:
  table: bigquery-public-data.noaa_gsod.gsod2023
  field: min
  entity_field: stn
  entity_kind: station_id
  source: NOAA Global Surface Weather Summary (BigQuery)
  unit: degF
  name_table: bigquery-public-data.noaa_gsod.stations
  name_key: usaf
  name_field: name
representativeQueries:
- coldest recorded temperatures in 2023
---

# Schema & Access

Provides SQL ranking and filtering for `min` (Minimum Temperature) over `bigquery-public-data.noaa_gsod.gsod2023`.
