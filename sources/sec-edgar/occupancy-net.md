---
type: Financial Statement Concept
title: Occupancy, Net — SEC EDGAR
description: This measure reports the net amount of occupancy expenses incurred by
  a publicly traded company or SEC filer, which may include depreciation of facilities,
  lease expenses, property taxes, and insurance costs. It specifically counts the
  costs associated with maintaining physical spaces used for operations. This measure
  is distinct from broader operational expenses as it focuses solely on occupancy-related
  costs. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- occupancy
- net
source: ./_access.md
taxonomy: us-gaap
concept: OccupancyNet
periodType: duration
unit: currency
representativeQueries:
- What is the net occupancy expense for this period?
- Can you provide the total for occupancy-related expenses?
- How much did we spend on lease and property taxes?
- What is included in our net occupancy expenses?
---

# Schema

Reports the `us-gaap:OccupancyNet` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
