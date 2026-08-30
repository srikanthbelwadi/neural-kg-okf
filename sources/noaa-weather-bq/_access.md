---
type: Data Source
title: NOAA Global Surface Weather Summary (BigQuery) — OKF BigQuery Access
description: Global daily weather observations from over 9,000 meteorological stations
  worldwide.
resource: bigquery-public-data.noaa_gsod
publisher: NOAA / Google Cloud Public Datasets
trust:
  identity: did:web:noaa_gsod.googlecloud.com
  identityType: did
access:
  auth: gcp
  operations:
    query:
      method: BIGQUERY
      url: ''
      capability:
        paths:
        - key
        - filter
        - order
        - enumerate
        - aggregate
        grain: station_id
        order:
          server: true
        population:
          complete: true
        requires_env: GOOGLE_CLOUD_PROJECT
entityType: Population of station_id for global ranking, filtering and aggregation
  in BigQuery.
---

# About

Actionable OKF access descriptor for `bigquery-public-data.noaa_gsod`.
