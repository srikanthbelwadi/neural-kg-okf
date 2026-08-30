---
type: Financial Statement Concept
title: Interest Expense, Time Deposits — SEC EDGAR
description: This measure reports the aggregate interest expense incurred on all time
  deposits, including certificates of deposits, in domestic offices for a publicly
  traded company or SEC filer. It is presented as a duration value in currency. This
  measure is unique as it encompasses all time deposits, providing a comprehensive
  view of interest expenses related to this category.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- time
- deposits
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseTimeDeposits
periodType: duration
unit: currency
representativeQueries:
- What is the total interest expense on all time deposits?
- How much interest are we paying on our time deposits?
- Can you provide the aggregate interest expense for time deposits?
---

# Schema

Reports the `us-gaap:InterestExpenseTimeDeposits` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
