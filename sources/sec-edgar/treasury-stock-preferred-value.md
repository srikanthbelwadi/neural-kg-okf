---
type: Financial Statement Concept
title: Treasury Stock, Preferred, Value — SEC EDGAR
description: This measure reports the total monetary value allocated to preferred
  shares that a publicly traded company has repurchased and is holding in its treasury.
  It provides insight into the financial implications of the company's management
  of its preferred equity. The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- preferred
- value
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockPreferredValue
periodType: instant
unit: currency
representativeQueries:
- What is the value allocated to repurchased preferred shares in treasury?
- How much do we have in treasury for preferred shares we've bought back?
- Can you tell me the total value of preferred shares held in treasury?
- What is the amount for treasury stock related to preferred shares?
---

# Schema

Reports the `us-gaap:TreasuryStockPreferredValue` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
