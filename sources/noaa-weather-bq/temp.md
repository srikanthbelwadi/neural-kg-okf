---
type: NOAA Global Surface Weather Summary (BigQuery) Measure (BigQuery)
title: Mean Daily Temperature (temp) — NOAA Global Surface Weather Summary (BigQuery)
description: Rank, filter, and aggregate by mean daily temperature (temp) using Google
  Cloud BigQuery.
tags:
- noaa-weather-bq
- bigquery
- ranking
- aggregate
- population
- temp
source: ./_access.md
bq:
  table: bigquery-public-data.noaa_gsod.gsod2023
  field: temp
  entity_field: stn
  entity_kind: station_id
  source: NOAA Global Surface Weather Summary (BigQuery)
  unit: degF
  name_table: bigquery-public-data.noaa_gsod.stations
  name_key: usaf
  name_field: name
representativeQueries:
- What was the hottest weather station in 2023?
- rank weather stations by temperature
---

# Schema & Access

Provides SQL ranking and filtering for `temp` (Mean Daily Temperature) over `bigquery-public-data.noaa_gsod.gsod2023`.
