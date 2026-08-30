---
type: Financial Statement Concept
title: Crypto Asset, Number of Units, Restricted — SEC EDGAR
description: This measure captures the number of crypto asset units that are subject
  to contractual sale restrictions. It is relevant to publicly traded companies holding
  crypto assets and provides insight into the limitations on their ability to sell
  these assets. This measure is narrower than the total number of units held, as it
  specifically focuses on restricted units.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- number
- restricted
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetNumberOfRestrictedUnits
periodType: instant
unit: pure
representativeQueries:
- What is the number of restricted crypto asset units we hold?
- Can you tell me how many crypto asset units are under sale restrictions?
- How many units of crypto assets are restricted from sale?
---

# Schema

Reports the `us-gaap:CryptoAssetNumberOfRestrictedUnits` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
