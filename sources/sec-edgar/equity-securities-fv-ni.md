---
type: Financial Statement Concept
title: Equity Securities, FV-NI, Current — SEC EDGAR
description: This measure reports the amount invested in equity securities that are
  measured at fair value, with any changes in fair value recognized in net income,
  and classified as current. It pertains to publicly traded companies or SEC filers.
  This measure is distinct from others as it focuses solely on current equity securities,
  excluding long-term investments or those without readily determinable fair value.
  The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- equity
- securities
source: ./_access.md
taxonomy: us-gaap
concept: EquitySecuritiesFvNi
periodType: instant
unit: currency
representativeQueries:
- What is the current amount for FV-NI equity securities?
- Can you tell me the investment value for current equity securities?
- How much do we have in current equity securities at fair value?
- What is the amount of equity securities measured at fair value recognized in net
  income?
---

# Schema

Reports the `us-gaap:EquitySecuritiesFvNi` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
