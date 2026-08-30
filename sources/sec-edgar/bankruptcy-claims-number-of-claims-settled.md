---
type: Financial Statement Concept
title: Bankruptcy Claims, Number of Claims Settled — SEC EDGAR
description: This measure indicates the total number of bankruptcy claims that have
  been settled, representing the volume of claims resolved against a publicly traded
  company or SEC filer. It is different from claims that are still under review or
  have been expunged, as it only includes those that have reached a settlement. The
  reporting is done as an instant value in pure count.
tags:
- finance
- sec
- edgar
- us-gaap
- bankruptcy
- claims
- number
- claims
source: ./_access.md
taxonomy: us-gaap
concept: BankruptcyClaimsNumberOfClaimsSettled
periodType: instant
unit: pure
representativeQueries:
- How many bankruptcy claims have been settled?
- What is the total number of claims we've resolved?
- Can you tell me the number of settled claims in bankruptcy?
---

# Schema

Reports the `us-gaap:BankruptcyClaimsNumberOfClaimsSettled` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
