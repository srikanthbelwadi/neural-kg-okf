---
type: Financial Statement Concept
title: Marketable Securities — SEC EDGAR
description: This measure reflects the total amount invested in marketable securities
  by a publicly traded company or SEC filer. It specifically encompasses all types
  of marketable securities without classification by current or noncurrent status.
  This measure is broader than current marketable securities, as it includes both
  current and noncurrent investments. It is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- marketable
- securities
source: ./_access.md
taxonomy: us-gaap
concept: MarketableSecurities
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of our marketable securities?
- How much do we have invested in marketable securities overall?
- Can you tell me the total investment in marketable securities?
---

# Schema

Reports the `us-gaap:MarketableSecurities` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
