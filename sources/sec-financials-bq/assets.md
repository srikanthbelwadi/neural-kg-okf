---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Total Assets (Assets) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by total assets (Assets) using Google Cloud
  BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- assets
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: Assets
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- Which public companies have the most assets?
- rank companies by total assets
---

# Schema & Access

Provides SQL ranking and filtering for `Assets` (Total Assets) over `bigquery-public-data.sec_quarterly_financials.numbers`.
