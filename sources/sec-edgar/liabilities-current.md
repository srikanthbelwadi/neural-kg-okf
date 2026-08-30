---
type: Financial Statement Concept
title: Liabilities, Current — SEC EDGAR
description: This measure captures the total current liabilities incurred by a publicly
  traded company that are expected to be settled within the next twelve months or
  within one business cycle, if longer. It provides insight into the company's short-term
  financial obligations, reflecting its operational liquidity. This measure is specifically
  about current liabilities, distinguishing it from long-term obligations. The value
  is reported in currency as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- liabilities
- current
source: ./_access.md
taxonomy: us-gaap
concept: LiabilitiesCurrent
periodType: instant
unit: currency
representativeQueries:
- What are the current liabilities?
- Can you list the current obligations due within a year?
- How much are the liabilities expected to be paid in the next twelve months?
- What is the total of current obligations from normal operations?
---

# Schema

Reports the `us-gaap:LiabilitiesCurrent` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
