---
type: Financial Statement Concept
title: Auction Market Preferred Securities, Shares, Redeemed — SEC EDGAR
description: This measure captures the number of auction market preferred securities
  shares that have been redeemed during the reporting period. The subject scope pertains
  to a publicly traded company or SEC filer. It is distinct from other share measures
  as it specifically counts redeemed shares, excluding shares that are still outstanding
  or newly issued. The value is reported as a duration value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- auction
- market
- preferred
- securities
source: ./_access.md
taxonomy: us-gaap
concept: AuctionMarketPreferredSecuritiesSharesRedeemed
periodType: duration
unit: shares
representativeQueries:
- How many auction market preferred securities shares were redeemed?
- Can you provide the number of AMPS shares redeemed during the period?
- What is the total number of auction market preferred shares that were redeemed?
- How many shares of auction market preferred securities were taken back?
---

# Schema

Reports the `us-gaap:AuctionMarketPreferredSecuritiesSharesRedeemed` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
