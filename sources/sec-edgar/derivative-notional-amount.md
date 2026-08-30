---
type: Financial Statement Concept
title: Derivative, Notional Amount — SEC EDGAR
description: This measure reports the nominal or face amount used to calculate payment
  on a derivative held by a publicly traded company. It serves as a basis for determining
  the financial obligations or revenues associated with the derivative. This measure
  is distinct from nonmonetary notional amounts, which focus on unit counts, emphasizing
  monetary values instead. It is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- derivative
- notional
- amount
source: ./_access.md
taxonomy: us-gaap
concept: DerivativeNotionalAmount
periodType: instant
unit: currency
representativeQueries:
- What is the notional amount for our derivative contracts?
- Can you provide the face amount used for calculating payments on derivatives?
- What is the nominal amount for our derivatives?
- How is the notional amount determined for our derivative instruments?
---

# Schema

Reports the `us-gaap:DerivativeNotionalAmount` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
