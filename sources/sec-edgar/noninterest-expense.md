---
type: Financial Statement Concept
title: Noninterest Expense — SEC EDGAR
description: This measure captures the total aggregate amount of all noninterest expenses
  incurred by the entity. It pertains to publicly traded companies or SEC filers,
  providing insights into their operational costs outside of interest expenses. This
  measure is distinct from interest expenses, focusing solely on other types of expenses.
  The value is reported in currency, reflecting the total noninterest expenses over
  a specified duration.
tags:
- finance
- sec
- edgar
- us-gaap
- noninterest
- expense
source: ./_access.md
taxonomy: us-gaap
concept: NoninterestExpense
periodType: duration
unit: currency
representativeQueries:
- What is the total noninterest expense for the period?
- Can you tell me the aggregate amount of noninterest expenses?
- How much did we spend on noninterest expenses?
---

# Schema

Reports the `us-gaap:NoninterestExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
