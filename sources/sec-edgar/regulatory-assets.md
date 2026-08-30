---
type: Financial Statement Concept
title: Regulatory Asset — SEC EDGAR
description: Regulatory Asset quantifies the amount of a specific regulatory asset
  held by a publicly traded company as itemized in a table of regulatory assets at
  the end of the fiscal period. This measure focuses on individual regulatory assets,
  distinguishing it from broader asset categories by its regulatory context. The reported
  value is expressed in currency and reflects an instant value as of the reporting
  date.
tags:
- finance
- sec
- edgar
- us-gaap
- regulatory
- assets
source: ./_access.md
taxonomy: us-gaap
concept: RegulatoryAssets
periodType: instant
unit: currency
representativeQueries:
- What is the amount for the regulatory asset as of the end of the period?
- Can you provide the individual regulatory asset figure?
- How much is listed as a regulatory asset in the table?
- What is the total for regulatory assets at the end of the period?
---

# Schema

Reports the `us-gaap:RegulatoryAssets` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
