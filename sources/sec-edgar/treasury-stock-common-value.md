---
type: Financial Statement Concept
title: Treasury Stock, Common, Value — SEC EDGAR
description: This measure reports the total monetary value allocated to common shares
  that a publicly traded company has repurchased and is holding in its treasury. It
  reflects the financial impact of share repurchases on the company's equity structure.
  The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- common
- value
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockCommonValue
periodType: instant
unit: currency
representativeQueries:
- What is the value of common shares we have repurchased and are holding in treasury?
- How much have we allocated to treasury stock for common shares?
- Can you provide the total value of common shares in treasury?
- What is the amount for repurchased common shares held in treasury?
---

# Schema

Reports the `us-gaap:TreasuryStockCommonValue` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
