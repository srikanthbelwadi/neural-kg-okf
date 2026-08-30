---
type: Financial Statement Concept
title: Cost, Direct Material — SEC EDGAR
description: This measure captures the cost of direct materials used in the production
  of goods and services, relevant to a publicly traded company or SEC filer. It quantifies
  the expenses directly associated with the materials required for manufacturing and
  service delivery, providing insight into production costs. This measure is distinct
  from other cost metrics, such as labor or overhead, as it focuses specifically on
  material costs. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- cost
- direct
- material
source: ./_access.md
taxonomy: us-gaap
concept: CostDirectMaterial
periodType: duration
unit: currency
representativeQueries:
- What is the cost of direct materials used in production?
- Can you tell me how much was spent on materials for goods produced?
- What is the total cost of materials for services rendered?
- How much did we spend on direct materials for production?
---

# Schema

Reports the `us-gaap:CostDirectMaterial` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
