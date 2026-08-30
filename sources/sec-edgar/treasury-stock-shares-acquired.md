---
type: Financial Statement Concept
title: Treasury Stock, Shares, Acquired — SEC EDGAR
description: This measure counts the total number of shares that a publicly traded
  company has repurchased during a specific fiscal period and are currently held in
  treasury. It reflects the company's strategy regarding its own stock and can indicate
  confidence in its financial health. This measure is distinct from other stock-related
  metrics as it specifically focuses on shares acquired for treasury purposes, rather
  than shares issued or outstanding. The value is reported in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- shares
- acquired
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockSharesAcquired
periodType: duration
unit: shares
representativeQueries:
- How many shares have been repurchased and are held in treasury?
- What is the number of shares acquired and held in treasury?
- Can you tell me the count of treasury stock acquired this period?
- What was the total number of shares held in treasury after repurchase?
---

# Schema

Reports the `us-gaap:TreasuryStockSharesAcquired` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
