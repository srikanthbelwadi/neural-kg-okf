---
type: Financial Statement Concept
title: Crypto Asset, Sale — SEC EDGAR
description: This measure indicates the amount of decrease in a crypto asset resulting
  from its sale. It is relevant to a publicly traded company or SEC filer and excludes
  crypto assets held for platform users. This measure specifically focuses on sales
  transactions, differentiating it from other forms of asset decrease such as payments
  for services or dispositions, and it is reported in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- crypto
- asset
- sale
source: ./_access.md
taxonomy: us-gaap
concept: CryptoAssetSale
periodType: duration
unit: currency
representativeQueries:
- What is the decrease in crypto assets from sales?
- Can you tell me how much crypto we sold?
- How much did our crypto assets decrease due to sales?
- What is the amount deducted from crypto assets for sales?
---

# Schema

Reports the `us-gaap:CryptoAssetSale` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
