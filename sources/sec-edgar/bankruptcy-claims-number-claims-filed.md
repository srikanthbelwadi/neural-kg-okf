---
type: Financial Statement Concept
title: Bankruptcy Claims, Number Claims Filed — SEC EDGAR
description: This measure counts the total number of bankruptcy claims that have been
  filed with the bankruptcy court, reflecting the volume of claims against a publicly
  traded company or SEC filer. It is distinct from claims that have been settled or
  expunged, focusing solely on those currently filed. The reporting is done as a duration
  value in pure count.
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
concept: BankruptcyClaimsNumberClaimsFiled
periodType: duration
unit: pure
representativeQueries:
- What is the total number of bankruptcy claims we've filed?
- How many claims have we submitted to the bankruptcy court?
- Can you provide the count of claims filed in bankruptcy?
---

# Schema

Reports the `us-gaap:BankruptcyClaimsNumberClaimsFiled` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
