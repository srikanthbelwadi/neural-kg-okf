---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: Total Revenue (Revenues) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by total revenue (Revenues) using Google
  Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- revenues
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: Revenues
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- Which public companies have the highest total revenue?
- rank US companies by revenue
---

# Schema & Access

Provides SQL ranking and filtering for `Revenues` (Total Revenue) over `bigquery-public-data.sec_quarterly_financials.numbers`.
