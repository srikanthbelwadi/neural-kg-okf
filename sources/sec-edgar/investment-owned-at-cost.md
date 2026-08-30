---
type: Financial Statement Concept
title: Investment Owned, Cost — SEC EDGAR
description: This measure reports the total cost of investments owned by a publicly
  traded company or SEC filer at a specific point in time. It provides insight into
  the financial commitment made towards these investments, which can be critical for
  assessing profitability and investment strategy. Unlike measures that focus on market
  value or shares, this metric specifically addresses the cost basis of investments.
  The value is reported in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- owned
- cost
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentOwnedAtCost
periodType: instant
unit: currency
representativeQueries:
- What is the cost of the investment owned?
- Can you tell me the investment owned cost?
- How much did we pay for the investment?
---

# Schema

Reports the `us-gaap:InvestmentOwnedAtCost` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
