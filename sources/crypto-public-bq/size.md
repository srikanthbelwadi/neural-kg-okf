---
type: Google Cloud Crypto Blockchain Analytics (BigQuery) Measure (BigQuery)
title: Block Size (size) — Google Cloud Crypto Blockchain Analytics (BigQuery)
description: Rank, filter, and aggregate by block size (size) using Google Cloud BigQuery.
tags:
- crypto-public-bq
- bigquery
- ranking
- aggregate
- population
- size
source: ./_access.md
bq:
  table: bigquery-public-data.crypto_bitcoin.blocks
  field: size
  entity_field: number
  entity_kind: block_number
  source: Google Cloud Crypto Blockchain Analytics (BigQuery)
  unit: bytes
representativeQueries:
- largest Bitcoin blocks by byte size
---

# Schema & Access

Provides SQL ranking and filtering for `size` (Block Size) over `bigquery-public-data.crypto_bitcoin.blocks`.
