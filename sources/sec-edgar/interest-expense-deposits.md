---
type: Financial Statement Concept
title: Interest Expense, Deposits — SEC EDGAR
description: This measure captures the aggregate amount of interest expense incurred
  on all deposits by a publicly traded company or SEC filer. It is reported as a duration
  value in currency. This measure is unique as it encompasses interest expenses related
  to all types of deposits, providing a comprehensive view of deposit-related costs.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- deposits
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseDeposits
periodType: duration
unit: currency
representativeQueries:
- What is the total interest expense on all deposits?
- How much interest are we incurring for all our deposits?
- Can you provide the aggregate interest expense for deposits?
---

# Schema

Reports the `us-gaap:InterestExpenseDeposits` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
