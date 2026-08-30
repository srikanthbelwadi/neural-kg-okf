---
type: Financial Statement Concept
title: Payments of Dividends — SEC EDGAR
description: This measure captures the total cash outflow for capital distributions
  and dividends paid to common shareholders, preferred shareholders, and noncontrolling
  interests. It is applicable to companies that have multiple classes of equity holders.
  This measure is broader than others that focus solely on common or preferred dividends,
  as it encompasses all types of equity distributions. The value is reported as a
  duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- payments
- dividends
source: ./_access.md
taxonomy: us-gaap
concept: PaymentsOfDividends
periodType: duration
unit: currency
representativeQueries:
- What are the total payments of dividends?
- How much cash was distributed as dividends to shareholders?
- Can you tell me the cash outflow for capital distributions and dividends?
---

# Schema

Reports the `us-gaap:PaymentsOfDividends` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
