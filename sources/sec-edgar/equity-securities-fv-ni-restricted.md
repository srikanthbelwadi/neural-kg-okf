---
type: Financial Statement Concept
title: Equity Securities, FV-NI, Restricted — SEC EDGAR
description: This measure reports the amount of restricted investments in equity securities
  that are measured at fair value, with changes in fair value recognized in net income.
  It pertains to publicly traded companies or SEC filers. This measure is distinct
  as it focuses solely on restricted equity securities, excluding unrestricted investments.
  The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- equity
- securities
- restricted
source: ./_access.md
taxonomy: us-gaap
concept: EquitySecuritiesFvNiRestricted
periodType: instant
unit: currency
representativeQueries:
- What is the fair value of my restricted equity securities?
- Can you tell me the amount of restricted equity securities at fair value?
- How much are my restricted equity investments worth at fair value?
---

# Schema

Reports the `us-gaap:EquitySecuritiesFvNiRestricted` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
