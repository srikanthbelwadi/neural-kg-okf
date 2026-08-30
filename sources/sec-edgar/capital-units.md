---
type: Financial Statement Concept
title: Capital Units, Value — SEC EDGAR
description: This measure indicates the value of capital units or capital shares issued
  by the reporting entity. It is relevant to issuers of face-amount certificates and
  registered investment companies, providing insight into their capital structure.
  This measure is distinct from other equity measures as it specifically focuses on
  capital units, excluding other forms of equity or liabilities. The value is reported
  in currency as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- capital
- units
source: ./_access.md
taxonomy: us-gaap
concept: CapitalUnits
periodType: instant
unit: currency
representativeQueries:
- What is the value of the capital units or capital shares?
- Can you provide the current value of capital units?
- How much are the capital shares valued at?
---

# Schema

Reports the `us-gaap:CapitalUnits` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
