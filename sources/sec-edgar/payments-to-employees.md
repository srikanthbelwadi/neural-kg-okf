---
type: Financial Statement Concept
title: Payments to Employees — SEC EDGAR
description: This measure indicates the total cash payments made to employees during
  the current period, including wages and salaries. It provides insight into the labor
  costs incurred by the organization. This measure is distinct from payments made
  to suppliers or other operational costs and is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- payments
- employees
source: ./_access.md
taxonomy: us-gaap
concept: PaymentsToEmployees
periodType: duration
unit: currency
representativeQueries:
- What are the total payments made to employees?
- Can you tell me how much cash was paid to employees this period?
- How much did we spend on wages and salaries for employees?
- What is the total amount of cash payments to our employees?
---

# Schema

Reports the `us-gaap:PaymentsToEmployees` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
