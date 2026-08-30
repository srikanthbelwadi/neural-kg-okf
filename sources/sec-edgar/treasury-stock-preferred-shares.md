---
type: Financial Statement Concept
title: Treasury Stock, Preferred, Shares — SEC EDGAR
description: This measure counts the number of preferred shares that a publicly traded
  company has repurchased and is currently holding in its treasury. It provides insight
  into the company's management of its preferred equity and can signal strategic financial
  decisions. The count is reported as an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- preferred
- shares
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockPreferredShares
periodType: instant
unit: shares
representativeQueries:
- How many preferred shares have we repurchased and are now in treasury?
- What is the count of preferred shares held in treasury?
- Can you tell me the number of preferred shares we've bought back?
- What is the total number of preferred shares repurchased?
---

# Schema

Reports the `us-gaap:TreasuryStockPreferredShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
