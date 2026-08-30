---
type: Financial Statement Concept
title: Shares Acquired, Average Cost Per Share — SEC EDGAR
description: This measure calculates the average cost per share of shares repurchased
  by a publicly traded company, derived by dividing the total cost of repurchased
  shares by the total number of shares repurchased. It provides insight into the company's
  capital management strategies and the cost-effectiveness of its share buyback programs.
  This measure is distinct from total repurchase costs, as it focuses specifically
  on the average cost per share. It is reported as a duration value in per-share.
tags:
- finance
- sec
- edgar
- us-gaap
- treasury
- stock
- acquired
- average
source: ./_access.md
taxonomy: us-gaap
concept: TreasuryStockAcquiredAverageCostPerShare
periodType: duration
unit: per-share
representativeQueries:
- What is the average cost per share for shares acquired?
- Can you tell me the total cost of shares repurchased divided by the number of shares?
- How much did we pay on average for each share we bought back?
---

# Schema

Reports the `us-gaap:TreasuryStockAcquiredAverageCostPerShare` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
