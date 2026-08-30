---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Operating Income (OperatingIncomeLoss) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by operating income (OperatingIncomeLoss)
  using Google Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- operatingincomeloss
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: OperatingIncomeLoss
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- companies with highest operating profit
- rank companies by operating income
---

# Schema & Access

Provides SQL ranking and filtering for `OperatingIncomeLoss` (Operating Income) over `bigquery-public-data.sec_quarterly_financials.numbers`.
