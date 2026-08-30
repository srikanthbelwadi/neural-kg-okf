---
type: Financial Statement Concept
title: Supplies Expense — SEC EDGAR
description: This measure reports the total amount of expenses associated with supplies
  used during the current accounting period by a publicly traded company or SEC filer.
  It specifically counts costs for materials and items consumed in operations. This
  measure is focused on supplies expenses, distinguishing it from other operational
  costs that may not involve supplies. The value is reported as a duration value in
  currency.
tags:
- finance
- sec
- edgar
- us-gaap
- supplies
- expense
source: ./_access.md
taxonomy: us-gaap
concept: SuppliesExpense
periodType: duration
unit: currency
representativeQueries:
- What are the supplies expenses for this accounting period?
- Can you provide the total for expenses related to supplies used?
- How much did we spend on supplies this period?
- What is the amount for supplies costs?
---

# Schema

Reports the `us-gaap:SuppliesExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
