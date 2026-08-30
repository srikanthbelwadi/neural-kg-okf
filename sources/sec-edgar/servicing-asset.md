---
type: Financial Statement Concept
title: Servicing Asset — SEC EDGAR
description: This measure represents the total aggregate amount of servicing assets
  held by a publicly traded company or SEC filer, which are subsequently measured
  at fair value or using the amortization method. It provides insight into the company's
  servicing capabilities and asset management. This measure is distinct from liabilities,
  as it focuses solely on assets related to servicing. The reported value is expressed
  in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- servicing
- asset
source: ./_access.md
taxonomy: us-gaap
concept: ServicingAsset
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of our servicing assets?
- Can you tell me about the aggregate servicing assets we have?
- How much are our servicing assets measured at fair value?
- What is the total value of servicing assets on our balance sheet?
---

# Schema

Reports the `us-gaap:ServicingAsset` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
