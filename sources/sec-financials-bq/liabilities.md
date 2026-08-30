---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Total Liabilities (Liabilities) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by total liabilities (Liabilities) using
  Google Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- liabilities
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: Liabilities
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- companies with highest total liabilities
---

# Schema & Access

Provides SQL ranking and filtering for `Liabilities` (Total Liabilities) over `bigquery-public-data.sec_quarterly_financials.numbers`.
