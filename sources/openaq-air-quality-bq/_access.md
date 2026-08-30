---
type: Data Source
title: OpenAQ Global Air Quality (BigQuery) — OKF BigQuery Access
description: Aggregated real-time and historical air quality measurements across world
  monitoring stations.
resource: bigquery-public-data.openaq
publisher: OpenAQ / Google Cloud Public Datasets
trust:
  identity: did:web:openaq.googlecloud.com
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
        grain: location_name
        order:
          server: true
        population:
          complete: true
        requires_env: GOOGLE_CLOUD_PROJECT
entityType: Population of location_name for global ranking, filtering and aggregation
  in BigQuery.
---

# About

Actionable OKF access descriptor for `bigquery-public-data.openaq`.
