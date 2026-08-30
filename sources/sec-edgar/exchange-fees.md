---
type: Financial Statement Concept
title: Exchange Fees — SEC EDGAR
description: The amount of expense in the period for fees charged by securities exchanges
  for the privilege of trading securities listed on that exchange. Some fees vary
  with the related volume, while others are fixed.
tags:
- finance
- sec
- edgar
- us-gaap
- exchange
- fees
source: ./_access.md
taxonomy: us-gaap
concept: ExchangeFees
periodType: duration
unit: currency
representativeQueries:
- What are the exchange fees we incurred this period?
- How much did we pay in fees to securities exchanges for trading?
- Can you detail the expenses for exchange fees related to our securities?
---

# Schema

Reports the `us-gaap:ExchangeFees` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
