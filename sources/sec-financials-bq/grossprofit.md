---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Gross Profit (GrossProfit) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by gross profit (GrossProfit) using Google
  Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- grossprofit
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: GrossProfit
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- highest gross profit public companies
---

# Schema & Access

Provides SQL ranking and filtering for `GrossProfit` (Gross Profit) over `bigquery-public-data.sec_quarterly_financials.numbers`.
