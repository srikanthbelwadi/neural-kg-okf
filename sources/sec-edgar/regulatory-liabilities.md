---
type: Financial Statement Concept
title: Regulatory Liability — SEC EDGAR
description: Regulatory Liability quantifies the amount of a specific regulatory liability
  held by a publicly traded company as itemized in a table of regulatory liabilities
  at the end of the fiscal period. This measure encompasses all regulatory liabilities,
  distinguishing it from current or noncurrent liabilities by its broader scope. The
  reported value is expressed in currency and reflects an instant value as of the
  reporting date.
tags:
- finance
- sec
- edgar
- us-gaap
- regulatory
- liabilities
source: ./_access.md
taxonomy: us-gaap
concept: RegulatoryLiabilities
periodType: instant
unit: currency
representativeQueries:
- What is the amount for the regulatory liability as of the end of the period?
- Can you provide the individual regulatory liability figure?
- How much is listed as a regulatory liability in the table?
- What is the total for regulatory liabilities at the end of the period?
---

# Schema

Reports the `us-gaap:RegulatoryLiabilities` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
