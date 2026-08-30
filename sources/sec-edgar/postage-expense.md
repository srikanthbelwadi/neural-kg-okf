---
type: Financial Statement Concept
title: Postage Expense — SEC EDGAR
description: This measure captures the total amount of expenses associated with postage
  incurred by a publicly traded company or SEC filer. It specifically counts costs
  related to mailing and shipping services. This measure is distinct from other operational
  expenses as it focuses solely on postage-related costs. The value is reported as
  a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- postage
- expense
source: ./_access.md
taxonomy: us-gaap
concept: PostageExpense
periodType: duration
unit: currency
representativeQueries:
- What is the total postage expense for this period?
- Can you tell me how much we spent on postage?
- How much are our expenses related to mailing?
- What is the amount for postage costs?
---

# Schema

Reports the `us-gaap:PostageExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
