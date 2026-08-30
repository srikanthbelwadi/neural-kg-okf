---
type: Financial Statement Concept
title: Investment Company, Total Return — SEC EDGAR
description: This measure captures the percentage change in the net asset value of
  an investment company, assuming that dividends and capital gains are reinvested.
  It pertains to publicly traded investment companies and provides a comprehensive
  view of total investment performance. This measure is unique as it encompasses both
  capital appreciation and income reinvestment, distinguishing it from other return
  measures.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- company
- total
- return
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentCompanyTotalReturn
periodType: duration
unit: percent
representativeQueries:
- What is the total return percentage for the fund?
- Can you tell me how much the fund's net asset value has increased or decreased?
- What is the total return assuming we reinvest dividends and capital gains?
---

# Schema

Reports the `us-gaap:InvestmentCompanyTotalReturn` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
