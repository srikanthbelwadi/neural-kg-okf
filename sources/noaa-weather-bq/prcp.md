---
type: NOAA Global Surface Weather Summary (BigQuery) Measure (BigQuery)
title: Total Daily Precipitation (prcp) — NOAA Global Surface Weather Summary (BigQuery)
description: Rank, filter, and aggregate by total daily precipitation (prcp) using
  Google Cloud BigQuery.
tags:
- noaa-weather-bq
- bigquery
- ranking
- aggregate
- population
- prcp
source: ./_access.md
bq:
  table: bigquery-public-data.noaa_gsod.gsod2023
  field: prcp
  entity_field: stn
  entity_kind: station_id
  source: NOAA Global Surface Weather Summary (BigQuery)
  unit: inches
  name_table: bigquery-public-data.noaa_gsod.stations
  name_key: usaf
  name_field: name
representativeQueries:
- Which stations recorded the highest precipitation?
- wettest weather stations in 2023
---

# Schema & Access

Provides SQL ranking and filtering for `prcp` (Total Daily Precipitation) over `bigquery-public-data.noaa_gsod.gsod2023`.
