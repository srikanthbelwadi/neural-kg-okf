---
type: Financial Statement Concept
title: Dividends — SEC EDGAR
description: This measure indicates the total amount of paid and unpaid cash, stock,
  and paid-in-kind (PIK) dividends declared. It pertains to a publicly traded company
  and encompasses dividends related to both common and preferred stock. This measure
  is distinct from other income measures, as it specifically focuses on distributions
  to shareholders rather than overall earnings. The amount is reported in currency
  as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
source: ./_access.md
taxonomy: us-gaap
concept: Dividends
periodType: duration
unit: currency
representativeQueries:
- What are the total dividends declared?
- Can you tell me the amount of paid and unpaid dividends?
- How much do we have in cash and stock dividends declared?
- What is the total for dividends, including PIK dividends?
---

# Schema

Reports the `us-gaap:Dividends` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
