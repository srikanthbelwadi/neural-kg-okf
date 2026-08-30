---
type: Financial Statement Concept
title: Income Tax Holiday, Aggregate Dollar Amount — SEC EDGAR
description: This measure indicates the total amount of income taxes from which a
  reporting entity is exempt or for which it will receive a reduction due to an income
  tax holiday granted by the taxing jurisdiction. It pertains to a publicly traded
  company and provides insight into tax benefits received as a result of specific
  incentives. This measure is distinct from general tax liabilities, as it focuses
  specifically on exemptions or reductions granted during a tax holiday. The value
  is reported in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- income
- tax
- holiday
- aggregate
source: ./_access.md
taxonomy: us-gaap
concept: IncomeTaxHolidayAggregateDollarAmount
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of income tax exemptions we received?
- How much did the income tax holiday save us?
- Can you tell me the dollar amount of our income tax reductions from the holiday?
- What is the aggregate income tax benefit from the holiday?
---

# Schema

Reports the `us-gaap:IncomeTaxHolidayAggregateDollarAmount` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
