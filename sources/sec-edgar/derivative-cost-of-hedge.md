---
type: Financial Statement Concept
title: Derivative, Cost of Hedge — SEC EDGAR
description: This measure indicates the premium or cost associated with a hedge that
  is expensed during the reporting period. It pertains to publicly traded companies
  and provides insight into the financial impact of hedging activities. This measure
  is distinct from other derivative costs as it specifically focuses on the cost of
  hedges rather than gains or losses from hedging activities. The value is reported
  in currency over a fiscal duration.
tags:
- finance
- sec
- edgar
- us-gaap
- derivative
- cost
- hedge
source: ./_access.md
taxonomy: us-gaap
concept: DerivativeCostOfHedge
periodType: duration
unit: currency
representativeQueries:
- What is the cost of the hedge for this period?
- Can you tell me the premium we paid for the hedge?
- How much did we expense for the hedge cost?
- What was the hedge cost incurred during this period?
---

# Schema

Reports the `us-gaap:DerivativeCostOfHedge` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
