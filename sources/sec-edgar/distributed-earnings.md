---
type: Financial Statement Concept
title: Distributed Earnings — SEC EDGAR
description: The total amount of dividends declared in the period for each class of
  stock and the contractual amount of dividends (or interest on participating income
  bonds) that must be paid for the period (for example, unpaid cumulative dividends).
  Dividends declared in the current period do not include dividends declared in respect
  of prior-period unpaid cumulative dividends. Preferred dividends that are cumulative
  only if earned are deducted only to the extent that they are earned.
tags:
- finance
- sec
- edgar
- us-gaap
- distributed
- earnings
source: ./_access.md
taxonomy: us-gaap
concept: DistributedEarnings
periodType: duration
unit: currency
representativeQueries:
- What are the total distributed earnings for the period?
- Can you provide details on the dividends declared this period?
- How much did we declare in dividends for each class of stock?
---

# Schema

Reports the `us-gaap:DistributedEarnings` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
