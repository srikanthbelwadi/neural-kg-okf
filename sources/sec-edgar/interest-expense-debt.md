---
type: Financial Statement Concept
title: Interest Expense, Debt — SEC EDGAR
description: This measure reports the amount of interest expense associated with borrowed
  funds accounted for as interest expense for debt by a publicly traded company or
  SEC filer. It is presented as a duration value in currency. This measure is distinct
  as it focuses specifically on interest expenses related to debt, rather than other
  types of interest expenses.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- debt
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseDebt
periodType: duration
unit: currency
representativeQueries:
- What is the interest expense for our debt?
- How much are we paying in interest on borrowed funds?
- Can you tell me the total interest expense related to our debt?
---

# Schema

Reports the `us-gaap:InterestExpenseDebt` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
