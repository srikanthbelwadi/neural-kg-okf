---
type: Financial Statement Concept
title: Investment Company, Dividend Distribution — SEC EDGAR
description: This measure reports the total amount of dividend distributions made
  by an investment company from ordinary income and capital gains. It applies to publicly
  traded investment companies and provides insight into shareholder returns. This
  measure is unique as it excludes distributions related to tax returns of capital,
  focusing solely on dividends.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- company
- dividend
- distribution
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentCompanyDividendDistribution
periodType: duration
unit: currency
representativeQueries:
- What is the amount of dividend distribution from ordinary income and capital gains?
- Can you tell me how much we distributed in dividends this period?
- What are the total dividends paid out from our income and capital gains?
---

# Schema

Reports the `us-gaap:InvestmentCompanyDividendDistribution` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
