---
type: Financial Statement Concept
title: Cost, Maintenance — SEC EDGAR
description: This measure reports the cost of maintenance incurred that is directly
  related to the production of goods and services, applicable to a publicly traded
  company or SEC filer. It quantifies expenses associated with maintaining equipment
  and facilities necessary for production, providing insight into operational efficiency.
  This measure is distinct from other cost metrics, such as direct materials or labor,
  as it focuses specifically on maintenance costs. The value is reported as a duration
  value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- cost
- maintenance
source: ./_access.md
taxonomy: us-gaap
concept: CostMaintenance
periodType: duration
unit: currency
representativeQueries:
- What is the cost of maintenance related to production?
- Can you tell me how much was spent on maintenance for goods produced?
- What is the total cost of maintenance for services rendered?
- How much did we incur as a cost of maintenance for production?
---

# Schema

Reports the `us-gaap:CostMaintenance` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
