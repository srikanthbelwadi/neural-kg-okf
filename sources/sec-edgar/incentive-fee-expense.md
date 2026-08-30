---
type: Financial Statement Concept
title: Incentive Fee Expense — SEC EDGAR
description: This measure captures the total expense related to incentive fees based
  on performance for a publicly traded company or SEC filer. It reflects costs associated
  with managing operations, including investments. This measure is distinct from other
  fee-related expenses as it specifically pertains to performance-based incentives,
  reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- incentive
- fee
- expense
source: ./_access.md
taxonomy: us-gaap
concept: IncentiveFeeExpense
periodType: duration
unit: currency
representativeQueries:
- What is the amount of incentive fee expense based on performance?
- Can you provide the total expense for incentive fees this period?
- How much did we incur in incentive fees for managing operations?
- What is the total expense for performance-based incentive fees?
---

# Schema

Reports the `us-gaap:IncentiveFeeExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
