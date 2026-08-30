---
type: Google Cloud Crypto Blockchain Analytics (BigQuery) Measure (BigQuery)
title: Total Block Fees (fee) — Google Cloud Crypto Blockchain Analytics (BigQuery)
description: Rank, filter, and aggregate by total block fees (fee) using Google Cloud
  BigQuery.
tags:
- crypto-public-bq
- bigquery
- ranking
- aggregate
- population
- fee
source: ./_access.md
bq:
  table: bigquery-public-data.crypto_bitcoin.blocks
  field: fee
  entity_field: number
  entity_kind: block_number
  source: Google Cloud Crypto Blockchain Analytics (BigQuery)
  unit: satoshis
representativeQueries:
- highest fee blocks in Bitcoin history
---

# Schema & Access

Provides SQL ranking and filtering for `fee` (Total Block Fees) over `bigquery-public-data.crypto_bitcoin.blocks`.
