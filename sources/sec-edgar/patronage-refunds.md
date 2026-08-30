---
type: Financial Statement Concept
title: Patronage Refunds — SEC EDGAR
description: This measure captures the total amount of earnings distributed to patrons
  of an agricultural cooperative, reflecting the cooperative's profit-sharing practices.
  It pertains to publicly traded companies or SEC filers in the agricultural sector.
  This measure is distinct from retained earnings as it specifically focuses on distributions
  made to patrons, rather than earnings retained within the cooperative. The value
  is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- patronage
- refunds
source: ./_access.md
taxonomy: us-gaap
concept: PatronageRefunds
periodType: duration
unit: currency
representativeQueries:
- What are the patronage refunds distributed this period?
- How much did we distribute in earnings to patrons?
- Can you provide details on the total patronage refunds?
---

# Schema

Reports the `us-gaap:PatronageRefunds` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
