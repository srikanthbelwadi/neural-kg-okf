---
type: SEC Quarterly Financials (BigQuery) Measure (BigQuery)
title: R&D Expense (ResearchAndDevelopmentExpense) — SEC Quarterly Financials (BigQuery)
description: Rank, filter, and aggregate by r&d expense (ResearchAndDevelopmentExpense)
  using Google Cloud BigQuery.
tags:
- sec-financials-bq
- bigquery
- ranking
- aggregate
- population
- researchanddevelopmentexpense
source: ./_access.md
bq:
  table: bigquery-public-data.sec_quarterly_financials.numbers
  field: ResearchAndDevelopmentExpense
  entity_field: cik
  entity_kind: cik
  source: SEC Quarterly Financials (BigQuery)
  unit: USD
  name_via: wikidata
representativeQueries:
- Which companies spend the most on R&D?
- rank companies by research and development expense
---

# Schema & Access

Provides SQL ranking and filtering for `ResearchAndDevelopmentExpense` (R&D Expense) over `bigquery-public-data.sec_quarterly_financials.numbers`.
