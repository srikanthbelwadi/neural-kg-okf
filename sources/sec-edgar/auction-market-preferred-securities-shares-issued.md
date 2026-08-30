---
type: Financial Statement Concept
title: Auction Market Preferred Securities, Shares, Issued — SEC EDGAR
description: This measure reports the number of auction market preferred securities
  shares that have been issued. The subject scope pertains to a publicly traded company
  or SEC filer. It is distinct from other share measures as it specifically counts
  shares that have been issued, excluding shares that are outstanding or redeemed.
  The value is reported as a duration value in shares.
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
concept: AuctionMarketPreferredSecuritiesSharesIssued
periodType: duration
unit: shares
representativeQueries:
- How many auction market preferred securities shares were issued?
- Can you provide the number of shares issued for AMPS?
- What is the total number of auction market preferred shares issued?
- How many shares of auction market preferred securities do we have issued?
---

# Schema

Reports the `us-gaap:AuctionMarketPreferredSecuritiesSharesIssued` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
