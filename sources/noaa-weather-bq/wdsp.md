---
type: NOAA Global Surface Weather Summary (BigQuery) Measure (BigQuery)
title: Mean Wind Speed (wdsp) — NOAA Global Surface Weather Summary (BigQuery)
description: Rank, filter, and aggregate by mean wind speed (wdsp) using Google Cloud
  BigQuery.
tags:
- noaa-weather-bq
- bigquery
- ranking
- aggregate
- population
- wdsp
source: ./_access.md
bq:
  table: bigquery-public-data.noaa_gsod.gsod2023
  field: wdsp
  entity_field: stn
  entity_kind: station_id
  source: NOAA Global Surface Weather Summary (BigQuery)
  unit: knots
  name_table: bigquery-public-data.noaa_gsod.stations
  name_key: usaf
  name_field: name
representativeQueries:
- windiest weather stations in 2023
- rank locations by average wind speed
---

# Schema & Access

Provides SQL ranking and filtering for `wdsp` (Mean Wind Speed) over `bigquery-public-data.noaa_gsod.gsod2023`.
