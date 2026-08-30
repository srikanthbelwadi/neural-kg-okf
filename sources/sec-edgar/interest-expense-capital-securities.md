---
type: Financial Statement Concept
title: Interest Expense, Capital Securities — SEC EDGAR
description: This measure accounts for the interest expense incurred on capital securities
  issued by the reporting entity during the reporting period. It is relevant to publicly
  traded companies or SEC filers and provides insight into the cost of capital financing.
  This measure is distinct from other interest expense metrics as it specifically
  pertains to capital securities, excluding interest on other types of debt. The value
  is reported in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- capital
- securities
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseCapitalSecurities
periodType: duration
unit: currency
representativeQueries:
- What is the interest expense incurred on capital securities during the reporting
  period?
- Can you tell me the interest expense related to capital securities?
- How much interest was paid on capital securities this period?
---

# Schema

Reports the `us-gaap:InterestExpenseCapitalSecurities` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
