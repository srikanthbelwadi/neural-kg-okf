---
type: Financial Statement Concept
title: Loan Portfolio Expense — SEC EDGAR
description: This measure reflects the loan servicing fees paid to third parties by
  a publicly traded company, related to the management of its entire loan portfolio.
  It is reported as a duration value in currency, indicating the expenses incurred
  over a specific period for servicing loans. This measure is distinct from other
  loan-related costs, as it specifically pertains to servicing rather than origination
  or other expenses.
tags:
- finance
- sec
- edgar
- us-gaap
- loan
- portfolio
- expense
source: ./_access.md
taxonomy: us-gaap
concept: LoanPortfolioExpense
periodType: duration
unit: currency
representativeQueries:
- What are the loan servicing fees for the portfolio?
- Can you tell me the total loan portfolio expenses paid to third parties?
- How much did we incur in loan servicing fees for our loan portfolio?
---

# Schema

Reports the `us-gaap:LoanPortfolioExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
