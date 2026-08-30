---
type: Financial Statement Concept
title: Short-Term Investments — SEC EDGAR
description: This measure indicates the total amount of short-term investments held
  by a publicly traded company, which includes trading securities, available-for-sale
  securities, held-to-maturity securities, and other current short-term investments.
  It provides insight into the company's liquidity and investment strategy, distinguishing
  it from long-term investments. The measure is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- short
- term
- investments
source: ./_access.md
taxonomy: us-gaap
concept: ShortTermInvestments
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of our short-term investments?
- Can you provide the value of our trading and available-for-sale securities?
- How much do we have in short-term investments classified as current?
- What is the total value of our short-term investment portfolio?
---

# Schema

Reports the `us-gaap:ShortTermInvestments` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
