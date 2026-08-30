---
type: Financial Statement Concept
title: Treasury Stock, Shares, Retired — SEC EDGAR
description: This measure indicates the number of shares of common and preferred stock
  that have been retired from treasury by a publicly traded company during the reporting
  period. It reflects the company's actions to reduce its outstanding shares, which
  can impact earnings per share and shareholder value. This measure is distinct from
  shares repurchased, as it specifically counts shares that have been permanently
  retired. It is reported as a duration value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- shares
- retired
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockSharesRetired
periodType: duration
unit: shares
representativeQueries:
- How many shares of treasury stock were retired this period?
- Can you provide the number of common and preferred shares retired?
- What is the total number of shares retired from treasury?
---

# Schema

Reports the `us-gaap:TreasuryStockSharesRetired` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
