---
type: Financial Statement Concept
title: Payments to Suppliers — SEC EDGAR
description: This measure captures the total cash payments made to suppliers for goods
  and services during the current period. It provides insight into the operational
  costs incurred by the organization related to procurement. This measure is distinct
  from payments made to employees and is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- payments
- suppliers
source: ./_access.md
taxonomy: us-gaap
concept: PaymentsToSuppliers
periodType: duration
unit: currency
representativeQueries:
- What are the cash payments made to suppliers this period?
- How much did we pay suppliers for goods and services?
- Can you tell me the total cash outflow to suppliers?
---

# Schema

Reports the `us-gaap:PaymentsToSuppliers` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
