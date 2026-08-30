---
type: Financial Statement Concept
title: Investment Owned, Restricted, Cost — SEC EDGAR
description: This measure indicates the total cost of restricted investments owned
  by a publicly traded company or SEC filer at a specific point in time. It provides
  insight into the financial commitment made towards these restricted investments,
  which can affect liquidity and investment strategy. This measure is distinct from
  other investment cost metrics as it specifically addresses restricted investments
  rather than total investments or assets. The value is reported in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- owned
- restricted
- cost
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentOwnedRestrictedCost
periodType: instant
unit: currency
representativeQueries:
- What is the cost of the restricted investment?
- Can you tell me how much we paid for the restricted investment?
- How much is the cost associated with the restricted investment?
---

# Schema

Reports the `us-gaap:InvestmentOwnedRestrictedCost` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
