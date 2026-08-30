---
type: Financial Statement Concept
title: Crypto Asset, Addition — SEC EDGAR
description: This measure indicates the total amount of increase in crypto assets
  resulting from additions made by the organization. It pertains to a publicly traded
  company or SEC filer and excludes any crypto assets held for platform users. The
  value is reported in currency and reflects changes over a fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- addition
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetAddition
periodType: duration
unit: currency
representativeQueries:
- What is the increase in crypto assets from additions?
- How much did we add to our crypto assets?
- Can you provide the amount of crypto assets acquired through additions?
---

# Schema

Reports the `us-gaap:CryptoAssetAddition` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
