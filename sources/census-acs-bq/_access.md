---
type: Data Source
title: US Census ACS (BigQuery) — County & State Demographics — OKF BigQuery Access
description: American Community Survey socio-economic statistics as a queryable BigQuery
  table.
resource: bigquery-public-data.census_bureau_acs
publisher: US Census Bureau / Google Cloud Public Datasets
trust:
  identity: did:web:census_bureau_acs.googlecloud.com
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

Actionable OKF access descriptor for `bigquery-public-data.census_bureau_acs`.
