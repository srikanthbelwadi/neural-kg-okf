---
type: Financial Statement Concept
title: Number of States in which Entity Operates — SEC EDGAR
description: This measure indicates the number of states in which a publicly traded
  company or SEC filer operates as of the balance sheet date. It provides insight
  into the geographical reach and operational footprint of the entity. This measure
  is distinct from other operational metrics as it focuses specifically on the number
  of states rather than overall market presence or revenue generation. It is reported
  as an instant value in pure.
tags:
- finance
- sec
- edgar
- us-gaap
- number
- states
- which
- entity
source: ./_access.md
taxonomy: us-gaap
concept: NumberOfStatesInWhichEntityOperates
periodType: instant
unit: pure
representativeQueries:
- How many states does the entity operate in?
- What is the number of states where the entity has operations?
- Can you tell me how many states the entity is active in?
- What is the total count of states for the entity's operations?
---

# Schema

Reports the `us-gaap:NumberOfStatesInWhichEntityOperates` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
