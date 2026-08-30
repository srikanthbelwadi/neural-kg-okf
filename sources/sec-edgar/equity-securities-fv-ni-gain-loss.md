---
type: Financial Statement Concept
title: Equity Securities, FV-NI, Gain (Loss) — SEC EDGAR
description: This measure indicates the amount of unrealized and realized gains or
  losses on investments in equity securities measured at fair value, with changes
  in fair value recognized in net income. It is relevant to publicly traded companies
  or SEC filers. This measure encompasses both types of gains and losses, distinguishing
  it from measures that focus solely on unrealized or realized gains or losses. The
  value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- equity
- securities
- gain
- loss
source: ./_access.md
taxonomy: us-gaap
concept: EquitySecuritiesFvNiGainLoss
periodType: duration
unit: currency
representativeQueries:
- What is the gain or loss on FV-NI equity securities?
- Can you show me the unrealized and realized gains for these investments?
- How much have we gained or lost on equity securities measured at fair value?
- What is the total gain or loss for these equity investments?
---

# Schema

Reports the `us-gaap:EquitySecuritiesFvNiGainLoss` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
