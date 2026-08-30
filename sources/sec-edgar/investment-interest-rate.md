---
type: Financial Statement Concept
title: Investment Interest Rate — SEC EDGAR
description: This measure reports the rate of interest earned on investments, reflecting
  the return generated from these financial assets. It is relevant to a publicly traded
  company or SEC filer and provides insight into the profitability of investments.
  This measure is distinct from other financial metrics as it focuses solely on the
  interest rate, rather than total returns or capital gains. The value is reported
  as a percentage at a specific point in time.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- interest
- rate
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentInterestRate
periodType: instant
unit: percent
representativeQueries:
- What is the interest rate on the investment?
- Can you tell me the investment interest rate?
- How much interest are we earning on the investment?
---

# Schema

Reports the `us-gaap:InvestmentInterestRate` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
