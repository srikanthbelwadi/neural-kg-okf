---
type: Financial Statement Concept
title: Investment Owned, Balance, Contracts — SEC EDGAR
description: This measure indicates the total number of contracts held by a publicly
  traded company or SEC filer at the close of the reporting period. It provides a
  snapshot of the company's derivative or options positions, which can be crucial
  for understanding risk exposure. Unlike measures that report on shares or monetary
  values, this metric specifically counts contracts, making it unique in its focus
  on derivative instruments. The value is reported in pure contracts.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- owned
- balance
- contracts
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentOwnedBalanceContracts
periodType: instant
unit: pure
representativeQueries:
- What is the balance of contracts held at the close of the period?
- Can you tell me the number of contracts owned at the end of the period?
- How many contracts are held in the investment?
---

# Schema

Reports the `us-gaap:InvestmentOwnedBalanceContracts` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
