---
type: Data Source
title: Google Cloud Crypto Blockchain Analytics (BigQuery) — OKF BigQuery Access
description: On-chain ledger data and token transaction metrics for major cryptocurrencies.
resource: bigquery-public-data.crypto_bitcoin
publisher: Google Cloud Public Datasets
trust:
  identity: did:web:crypto_bitcoin.googlecloud.com
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
        grain: block_number
        order:
          server: true
        population:
          complete: true
        requires_env: GOOGLE_CLOUD_PROJECT
entityType: Population of block_number for global ranking, filtering and aggregation
  in BigQuery.
---

# About

Actionable OKF access descriptor for `bigquery-public-data.crypto_bitcoin`.
