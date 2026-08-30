---
type: Financial Statement Concept
title: Patronage Source Earnings — SEC EDGAR
description: This measure captures the amount of revenue that exceeds costs resulting
  from transactions with patrons, reflecting the financial performance of an agricultural
  cooperative. It pertains to publicly traded companies or SEC filers operating in
  the agricultural sector. This measure is distinct from nonpatronage earnings as
  it specifically focuses on transactions involving patrons, rather than all revenue
  sources. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- patronage
- source
- earnings
source: ./_access.md
taxonomy: us-gaap
concept: PatronageSourceEarnings
periodType: duration
unit: currency
representativeQueries:
- What are the patronage source earnings this period?
- How much revenue did we generate from patron transactions?
- Can you provide details on earnings from patronage sources?
---

# Schema

Reports the `us-gaap:PatronageSourceEarnings` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
