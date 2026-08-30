---
type: Financial Statement Concept
title: Redeemable Preferred Stock Dividends — SEC EDGAR
description: This measure indicates the total dividends paid to holders of redeemable
  preferred stock by a publicly traded company, where the redemption is solely at
  the issuer's option. It specifically pertains to redeemable preferred stock dividends,
  distinguishing it from other types of dividends that may not have the same redemption
  characteristics. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- redeemable
- preferred
- stock
- dividends
source: ./_access.md
taxonomy: us-gaap
concept: RedeemablePreferredStockDividends
periodType: duration
unit: currency
representativeQueries:
- What dividends have we paid on redeemable preferred stock?
- How much did we distribute to preferred stockholders this period?
- Can you tell me the total amount of redeemable preferred stock dividends?
---

# Schema

Reports the `us-gaap:RedeemablePreferredStockDividends` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
