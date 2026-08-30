---
type: Financial Statement Concept
title: Investment Tax Credit — SEC EDGAR
description: This measure reflects the amount deducted from a publicly traded company's
  taxes, representing a percentage of investments made in certain assets over their
  useful life. It specifically includes deferred investment tax credits, distinguishing
  it from other tax credits that may not relate to investments. The value is reported
  as a duration value in currency, indicating the total tax credit over a defined
  period.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- tax
- credit
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentTaxCredit
periodType: duration
unit: currency
representativeQueries:
- What is the investment tax credit amount for this period?
- How much did we deduct from taxes for investment tax credits?
- Can you tell me the percentage of investment tax credits recognized?
- What was the total investment tax credit for the assets?
---

# Schema

Reports the `us-gaap:InvestmentTaxCredit` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
