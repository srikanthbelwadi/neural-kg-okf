---
type: Financial Statement Concept
title: Selling Expense — SEC EDGAR
description: This measure captures expenses recognized in the period that are directly
  related to the selling and distribution of products or services. It pertains to
  a publicly traded company or SEC filer and reflects the costs incurred in the sales
  process. This measure is distinct from other expense classifications by focusing
  specifically on selling expenses, reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- selling
- expense
source: ./_access.md
taxonomy: us-gaap
concept: SellingExpense
periodType: duration
unit: currency
representativeQueries:
- What are our selling expenses for this period?
- Can you break down the selling expenses?
- How much did we spend on selling and distribution?
- What are the direct costs related to selling our products?
---

# Schema

Reports the `us-gaap:SellingExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
