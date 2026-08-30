---
type: Financial Statement Concept
title: Federal Funds Purchased — SEC EDGAR
description: This measure represents the amount of short-term borrowing by a publicly
  traded company from another bank at the federal funds rate. It reflects the company's
  liquidity management and reliance on interbank lending for immediate funding needs.
  This measure is specifically focused on federal funds transactions, distinguishing
  it from other forms of borrowing or financing that may not involve interbank rates.
  The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- federal
- funds
- purchased
source: ./_access.md
taxonomy: us-gaap
concept: FederalFundsPurchased
periodType: instant
unit: currency
representativeQueries:
- How much are the federal funds I have purchased?
- What is the total amount of short-term borrowing at the federal funds rate?
- Can you tell me the amount I borrowed from another bank at the federal funds rate?
---

# Schema

Reports the `us-gaap:FederalFundsPurchased` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
