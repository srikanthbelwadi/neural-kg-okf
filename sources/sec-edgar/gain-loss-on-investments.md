---
type: Financial Statement Concept
title: Gain (Loss) on Investments — SEC EDGAR
description: This measure captures the amount of realized and unrealized gain or loss
  on investments for a publicly traded company. It reflects the financial performance
  of the company's investment portfolio, providing insight into investment strategies.
  This measure is distinct from other gain measures as it encompasses both realized
  and unrealized gains or losses, rather than focusing solely on one type. The value
  is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- gain
- loss
- investments
source: ./_access.md
taxonomy: us-gaap
concept: GainLossOnInvestments
periodType: duration
unit: currency
representativeQueries:
- What is the gain or loss on investments?
- Can you tell me the realized and unrealized gain or loss on investments?
- How much gain or loss was recognized from investment activities?
- What is the total gain or loss from all investments?
---

# Schema

Reports the `us-gaap:GainLossOnInvestments` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
