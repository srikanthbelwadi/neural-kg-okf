---
type: Financial Statement Concept
title: Debt Instrument, Convertible, Number of Equity Instruments — SEC EDGAR
description: Debt Instrument, Convertible, Number of Equity Instruments reports the
  number of equity instruments that a holder of a convertible debt instrument would
  receive if the debt were converted into equity. This measure is relevant to a publicly
  traded company and highlights potential equity dilution, distinguishing it from
  other debt measures that do not consider conversion features. It is reported as
  a duration value in pure, indicating the count of equity instruments.
tags:
- finance
- sec
- edgar
- us-gaap
- debt
- instrument
- convertible
- number
source: ./_access.md
taxonomy: us-gaap
concept: DebtInstrumentConvertibleNumberOfEquityInstruments
periodType: duration
unit: pure
representativeQueries:
- How many equity instruments can be received upon conversion of the debt?
- What is the number of equity shares from the convertible debt?
- Can you tell me how many shares we get if we convert the debt?
---

# Schema

Reports the `us-gaap:DebtInstrumentConvertibleNumberOfEquityInstruments` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
