---
type: Financial Statement Concept
title: Accretion Expense — SEC EDGAR
description: This measure represents the amount recognized as accretion expense, typically
  related to liabilities that have been discounted to their net present values, for
  a publicly traded company or SEC filer. It specifically accounts for the passage
  of time in relation to these liabilities, excluding any accretion associated with
  asset retirement obligations. The value is reported in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- accretion
- expense
source: ./_access.md
taxonomy: us-gaap
concept: AccretionExpense
periodType: duration
unit: currency
representativeQueries:
- What is the accretion expense recognized for our discounted liabilities?
- Can you provide the amount recognized for the passage of time on our liabilities?
- How much accretion expense do we have for our net present value liabilities?
---

# Schema

Reports the `us-gaap:AccretionExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
