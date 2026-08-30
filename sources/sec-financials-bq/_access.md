---
type: Data Source
title: SEC Quarterly Financials (BigQuery) — OKF BigQuery Access
description: Standardized public company quarterly financials from SEC Form 10-K and
  10-Q filings.
resource: bigquery-public-data.sec_quarterly_financials
publisher: SEC EDGAR / Google Cloud Public Datasets
trust:
  identity: did:web:sec_quarterly_financials.googlecloud.com
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
        grain: cik
        order:
          server: true
        population:
          complete: true
        requires_env: GOOGLE_CLOUD_PROJECT
entityType: Population of cik for global ranking, filtering and aggregation in BigQuery.
---

# About

Actionable OKF access descriptor for `bigquery-public-data.sec_quarterly_financials`.
