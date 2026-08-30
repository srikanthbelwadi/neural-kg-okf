---
type: Financial Statement Concept
title: Investment Owned, Balance, Shares — SEC EDGAR
description: This measure counts the total number of shares of investments owned by
  a publicly traded company or SEC filer at a specific point in time. It provides
  insight into the company's equity holdings and investment strategy. Unlike other
  measures that may focus on the value or cost of investments, this metric specifically
  reports the quantity of shares held, making it distinct in its focus on ownership
  volume. The value is reported in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- owned
- balance
- shares
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentOwnedBalanceShares
periodType: instant
unit: shares
representativeQueries:
- How many shares of the investment are owned?
- Can you tell me the number of shares held in the investment?
- What is the balance of shares owned in the investment?
---

# Schema

Reports the `us-gaap:InvestmentOwnedBalanceShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
