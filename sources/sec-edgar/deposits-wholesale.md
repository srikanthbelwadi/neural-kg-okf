---
type: Financial Statement Concept
title: Deposits, Wholesale — SEC EDGAR
description: This measure captures the total amount of all wholesale deposit accounts,
  including certificates of deposits, held by a publicly traded company or SEC filer.
  It provides a comprehensive view of the company's wholesale funding sources. This
  measure is broader than specific deposit types, as it encompasses all wholesale
  deposits rather than focusing on individual categories. It is reported as an instant
  value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- deposits
- wholesale
source: ./_access.md
taxonomy: us-gaap
concept: DepositsWholesale
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of wholesale deposit accounts?
- Can you tell me the aggregate value of all wholesale deposits including CDs?
- What’s the current total for wholesale deposits?
---

# Schema

Reports the `us-gaap:DepositsWholesale` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
