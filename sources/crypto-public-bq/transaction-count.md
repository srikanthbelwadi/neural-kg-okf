---
type: Google Cloud Crypto Blockchain Analytics (BigQuery) Measure (BigQuery)
title: Transactions Per Block (transaction_count) — Google Cloud Crypto Blockchain
  Analytics (BigQuery)
description: Rank, filter, and aggregate by transactions per block (transaction_count)
  using Google Cloud BigQuery.
tags:
- crypto-public-bq
- bigquery
- ranking
- aggregate
- population
- transaction-count
source: ./_access.md
bq:
  table: bigquery-public-data.crypto_bitcoin.blocks
  field: transaction_count
  entity_field: number
  entity_kind: block_number
  source: Google Cloud Crypto Blockchain Analytics (BigQuery)
  unit: count
representativeQueries:
- Which Bitcoin blocks had the highest transaction count?
- rank Bitcoin blocks by transaction volume
---

# Schema & Access

Provides SQL ranking and filtering for `transaction_count` (Transactions Per Block) over `bigquery-public-data.crypto_bitcoin.blocks`.
