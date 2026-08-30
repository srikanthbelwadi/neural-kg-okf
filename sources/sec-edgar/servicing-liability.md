---
type: Financial Statement Concept
title: Servicing Liability — SEC EDGAR
description: This measure captures the total aggregate amount of servicing liabilities
  held by a publicly traded company or SEC filer, which are subsequently measured
  at fair value or using the amortization method. It provides insight into the company's
  obligations related to servicing activities. This measure is distinct from assets,
  as it focuses solely on liabilities associated with servicing. The reported value
  is expressed in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- servicing
- liability
source: ./_access.md
taxonomy: us-gaap
concept: ServicingLiability
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of our servicing liabilities?
- Can you provide details on the aggregate servicing liabilities we have?
- How much are our servicing liabilities measured at fair value?
- What is the total value of servicing liabilities on our balance sheet?
---

# Schema

Reports the `us-gaap:ServicingLiability` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
