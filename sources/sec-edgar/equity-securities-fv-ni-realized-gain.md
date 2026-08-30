---
type: Financial Statement Concept
title: Equity Securities, FV-NI, Realized Gain — SEC EDGAR
description: This measure reports the amount of realized gains from the sale of investments
  in equity securities that are measured at fair value, with changes in fair value
  recognized in net income. It pertains to publicly traded companies or SEC filers.
  This measure specifically focuses on realized gains, distinguishing it from measures
  that include losses or unrealized gains. The value is reported as a duration value
  in currency.
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
concept: EquitySecuritiesFvNiRealizedGain
periodType: duration
unit: currency
representativeQueries:
- What is the realized gain from the sale of FV-NI equity securities?
- Can you tell me how much we gained from selling these equity investments?
- How much was the realized gain on equity securities measured at fair value?
- What is the total realized gain from these equity securities?
---

# Schema

Reports the `us-gaap:EquitySecuritiesFvNiRealizedGain` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
