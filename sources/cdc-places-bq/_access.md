---
type: Data Source
title: CDC PLACES Health Measures (BigQuery) — OKF BigQuery Access
description: Model-based county and city health estimates across all US counties from
  CDC PLACES.
resource: bigquery-public-data.cdc_places
publisher: CDC / Google Cloud Public Datasets
trust:
  identity: did:web:cdc_places.googlecloud.com
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
        grain: fips
        order:
          server: true
        population:
          complete: true
        requires_env: GOOGLE_CLOUD_PROJECT
entityType: Population of fips for global ranking, filtering and aggregation in BigQuery.
---

# About

Actionable OKF access descriptor for `bigquery-public-data.cdc_places`.
