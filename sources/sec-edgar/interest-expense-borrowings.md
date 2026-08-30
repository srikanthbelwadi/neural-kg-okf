---
type: Financial Statement Concept
title: Interest Expense, Borrowings — SEC EDGAR
description: This measure reports the aggregate amount of interest expense incurred
  on all borrowings by a publicly traded company or SEC filer. It is presented as
  a duration value in currency. This measure is distinct from other interest expense
  measures as it specifically focuses on borrowings, excluding other types of interest
  expenses.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- borrowings
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseBorrowings
periodType: duration
unit: currency
representativeQueries:
- What is the total interest expense on all borrowings?
- How much interest are we paying on our borrowings?
- Can you tell me the aggregate interest expense for our borrowings?
---

# Schema

Reports the `us-gaap:InterestExpenseBorrowings` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
