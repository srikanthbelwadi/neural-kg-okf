---
type: Financial Statement Concept
title: Bankruptcy Claims, Amount of Claims Settled — SEC EDGAR
description: This measure indicates the total amount of bankruptcy claims that have
  been settled, representing the financial resolution of claims against a publicly
  traded company or SEC filer. It is distinct from claims that are still under review
  or have been expunged, as it only includes those that have reached a settlement
  agreement. The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- bankruptcy
- claims
- amount
- claims
source: ./_access.md
taxonomy: us-gaap
concept: BankruptcyClaimsAmountOfClaimsSettled
periodType: instant
unit: currency
representativeQueries:
- What is the amount of bankruptcy claims that have been settled?
- How much have we paid to resolve bankruptcy claims?
- Can you tell me the total settled claims in bankruptcy?
---

# Schema

Reports the `us-gaap:BankruptcyClaimsAmountOfClaimsSettled` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
