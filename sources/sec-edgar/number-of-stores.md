---
type: Financial Statement Concept
title: Number of Stores — SEC EDGAR
description: This measure represents the total number of stores operated by the entity.
  It pertains to a publicly traded company or SEC filer and provides insight into
  its retail footprint. Unlike broader measures that may encompass sales or revenue,
  this metric specifically counts physical store locations, distinguishing it from
  other operational metrics. The value is reported as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- number
- stores
source: ./_access.md
taxonomy: us-gaap
concept: NumberOfStores
periodType: instant
unit: pure
representativeQueries:
- What is the total number of stores?
- How many stores does the company have?
- Can you provide the count of stores?
- What’s the number of retail locations?
---

# Schema

Reports the `us-gaap:NumberOfStores` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
