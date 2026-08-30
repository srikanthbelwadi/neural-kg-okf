---
type: Financial Statement Concept
title: Equity Securities, FV-NI, Realized Gain (Loss) — SEC EDGAR
description: This measure captures the amount of realized gains or losses from the
  sale of investments in equity securities measured at fair value, with changes in
  fair value recognized in net income. It is applicable to publicly traded companies
  or SEC filers. This measure encompasses both realized gains and losses, distinguishing
  it from measures that focus solely on gains or losses. The value is reported as
  a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- equity
- securities
- realized
- gain
source: ./_access.md
taxonomy: us-gaap
concept: EquitySecuritiesFvNiRealizedGainLoss
periodType: duration
unit: currency
representativeQueries:
- What is the realized gain or loss from the sale of FV-NI equity securities?
- Can you show me the total gain or loss from selling these investments?
- How much have we gained or lost on the sale of equity securities measured at fair
  value?
- What is the total realized gain or loss for these equity securities?
---

# Schema

Reports the `us-gaap:EquitySecuritiesFvNiRealizedGainLoss` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
