---
type: Financial Statement Concept
title: Market Data Revenue — SEC EDGAR
description: This measure reports the total revenue generated from market data services,
  which includes information about current quotes and recent prices for specific securities.
  It pertains to publicly traded companies and SEC filers, reflecting their income
  from data services. This measure is distinct from other revenue measures as it specifically
  focuses on market data, rather than overall sales or service revenue. The amount
  is reported in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- market
- data
- revenue
source: ./_access.md
taxonomy: us-gaap
concept: MarketDataRevenue
periodType: duration
unit: currency
representativeQueries:
- What is the revenue from market data services?
- Can you tell me how much we earned from market data revenue?
- How much revenue did we generate from market data services?
---

# Schema

Reports the `us-gaap:MarketDataRevenue` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
