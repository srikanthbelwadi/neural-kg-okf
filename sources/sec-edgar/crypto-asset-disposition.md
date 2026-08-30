---
type: Financial Statement Concept
title: Crypto Asset, Disposition — SEC EDGAR
description: This measure reports the amount of decrease in a crypto asset due to
  its disposition. It pertains to a publicly traded company or SEC filer and excludes
  crypto assets held for platform users. Unlike sales measures, this captures decreases
  from various forms of disposition, making it distinct in its focus, and it is reported
  in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- disposition
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetDisposition
periodType: duration
unit: currency
representativeQueries:
- What is the decrease in crypto assets from dispositions?
- Can you tell me how much crypto we disposed of?
- How much did our crypto assets decrease due to dispositions?
- What is the amount deducted from crypto assets for disposals?
---

# Schema

Reports the `us-gaap:CryptoAssetDisposition` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
