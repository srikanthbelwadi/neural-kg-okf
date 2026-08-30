---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Cash & Equivalents (CashAndCashEquivalentsAtCarryingValue) — SEC Quarterly
  Financials (BigQuery)
description: Rank, filter, and aggregate by cash & equivalents (CashAndCashEquivalentsAtCarryingValue)
  using Google Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- cashandcashequivalentsatcarryingvalue
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: CashAndCashEquivalentsAtCarryingValue
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- Which companies have the most cash on hand?
---

# Schema & Access

Provides SQL ranking and filtering for `CashAndCashEquivalentsAtCarryingValue` (Cash & Equivalents) over `bigquery-public-data.sec_quarterly_financials.numbers`.
