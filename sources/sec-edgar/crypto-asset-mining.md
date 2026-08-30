---
type: Financial Statement Concept
title: Crypto Asset, Mining — SEC EDGAR
description: This measure reports the total increase in crypto assets resulting from
  mining activities conducted by a publicly traded company, indicating the financial
  benefits derived from this process. It specifically excludes crypto assets held
  for platform users, distinguishing it from other measures of asset increases. The
  amount is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- mining
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetMining
periodType: duration
unit: currency
representativeQueries:
- What is the increase in crypto assets from mining?
- How much have we gained in crypto assets through mining?
- Can you provide the amount of crypto asset increase from mining activities?
---

# Schema

Reports the `us-gaap:CryptoAssetMining` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
