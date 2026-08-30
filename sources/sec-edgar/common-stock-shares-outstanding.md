---
type: Financial Statement Concept
title: Common Stock, Shares, Outstanding — SEC EDGAR
description: The number of shares of common stock outstanding is captured in this
  measure. It specifically relates to the shares that are currently held by shareholders
  and represent ownership in the organization. This measure is distinct from authorized
  shares as it focuses solely on shares that have been issued and are currently in
  circulation, providing insight into the equity structure. The value is reported
  in shares as of the balance sheet date.
tags:
- finance
- sec
- edgar
- us-gaap
- common
- stock
- shares
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: CommonStockSharesOutstanding
periodType: instant
unit: shares
representativeQueries:
- What is the number of common shares outstanding?
- How many shares of common stock are currently held by shareholders?
- Can you provide the total outstanding common shares?
---

# Schema

Reports the `us-gaap:CommonStockSharesOutstanding` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
