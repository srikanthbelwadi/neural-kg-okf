---
type: Financial Statement Concept
title: Crypto Asset, Number of Units — SEC EDGAR
description: This measure reports the total number of restricted and unrestricted
  crypto asset units held by a publicly traded company. It provides insight into the
  company's holdings in crypto assets, excluding those held for platform users. This
  measure is distinct from other unit measures as it encompasses both restricted and
  unrestricted units, rather than focusing on one category.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- number
- units
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetNumberOfUnits
periodType: instant
unit: pure
representativeQueries:
- How many units of crypto assets do we hold?
- Can you provide the total number of crypto asset units we have?
- What is the count of restricted and unrestricted crypto asset units?
---

# Schema

Reports the `us-gaap:CryptoAssetNumberOfUnits` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
