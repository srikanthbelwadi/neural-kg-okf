---
type: Financial Statement Concept
title: Stock Dividends, Shares — SEC EDGAR
description: This measure captures the total number of shares of both common and preferred
  stock issued as dividends during the reporting period. It is relevant to publicly
  traded companies that provide dividends across different classes of stock. This
  measure is distinct from individual stock dividend measures, as it combines both
  common and preferred shares. The count is reported in shares and reflects a duration
  value.
tags:
- finance
- sec
- edgar
- us-gaap
- stock
- dividends
- shares
source: ./_access.md
taxonomy: us-gaap
concept: StockDividendsShares
periodType: duration
unit: shares
representativeQueries:
- How many shares of stock were issued as dividends in total?
- What is the total number of shares issued as dividends?
- Can you tell me the shares of both common and preferred stock issued for dividends?
---

# Schema

Reports the `us-gaap:StockDividendsShares` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
