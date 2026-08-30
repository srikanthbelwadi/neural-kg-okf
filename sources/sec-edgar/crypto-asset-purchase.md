---
type: Financial Statement Concept
title: Crypto Asset, Purchase — SEC EDGAR
description: This measure reports the total amount of increase in crypto assets resulting
  from purchases made by the organization. It specifically pertains to a publicly
  traded company or SEC filer and excludes any crypto assets that are held for platform
  users. The value is reported in currency and reflects changes over a fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- purchase
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetPurchase
periodType: duration
unit: currency
representativeQueries:
- What was the increase in crypto assets from purchases?
- How much did we spend on crypto assets?
- Can you tell me the amount of crypto assets acquired through purchases?
---

# Schema

Reports the `us-gaap:CryptoAssetPurchase` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
