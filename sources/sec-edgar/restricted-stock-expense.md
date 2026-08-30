---
type: Financial Statement Concept
title: Restricted Stock or Unit Expense — SEC EDGAR
description: This measure captures the noncash expense incurred by a publicly traded
  company for the award of restricted stock or units under share-based payment arrangements.
  It specifically pertains to compensation that is not paid in cash, distinguishing
  it from other forms of employee compensation. The value is reported as a duration
  value in currency, indicating the total expense over the reporting period.
tags:
- finance
- sec
- edgar
- us-gaap
- restricted
- stock
- expense
source: ./_access.md
taxonomy: us-gaap
concept: RestrictedStockExpense
periodType: duration
unit: currency
representativeQueries:
- What is the expense for restricted stock or unit awards?
- How much did we recognize for share-based compensation this period?
- Can you provide the noncash expense for restricted stock?
- What was the total expense for restricted stock units?
---

# Schema

Reports the `us-gaap:RestrictedStockExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
