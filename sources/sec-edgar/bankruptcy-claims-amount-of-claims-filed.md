---
type: Financial Statement Concept
title: Bankruptcy Claims, Amount of Claims Filed — SEC EDGAR
description: This measure counts the total amount of bankruptcy claims that have been
  filed with the bankruptcy court, reflecting the financial obligations claimed by
  creditors against a publicly traded company or SEC filer. It is important to note
  that this measure does not include claims that have been settled or expunged, focusing
  solely on those that are currently filed. The reporting is done as a duration value
  in currency.
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
concept: BankruptcyClaimsAmountOfClaimsFiled
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of bankruptcy claims we've filed?
- How much have we claimed in bankruptcy court?
- Can you provide the amount of claims submitted to the bankruptcy court?
---

# Schema

Reports the `us-gaap:BankruptcyClaimsAmountOfClaimsFiled` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
