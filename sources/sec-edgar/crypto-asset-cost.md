---
type: Financial Statement Concept
title: Crypto Asset, Cost — SEC EDGAR
description: This measure indicates the total cost of crypto assets owned by a publicly
  traded company, reflecting the financial investment made in acquiring these assets.
  It specifically excludes crypto assets held for platform users, distinguishing it
  from other cost measures that may not have this restriction. The value is reported
  as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- cost
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetCost
periodType: instant
unit: currency
representativeQueries:
- What is the total cost of our crypto assets?
- Can you provide the cost for all crypto assets we hold?
- How much did we invest in our crypto assets?
- What is the cost basis for our crypto assets?
---

# Schema

Reports the `us-gaap:CryptoAssetCost` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
