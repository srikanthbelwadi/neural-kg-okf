---
type: Financial Statement Concept
title: Derivative, Number of Instruments Held — SEC EDGAR
description: This measure indicates the number of derivative instruments of a particular
  group held by a publicly traded company. It provides insight into the company's
  exposure to derivatives and its risk management strategies. This measure is specifically
  about the count of instruments, distinguishing it from measures that focus on financial
  values or rates. It is reported as an instant value in pure.
tags:
- finance
- sec
- edgar
- us-gaap
- derivative
- number
- instruments
- held
source: ./_access.md
taxonomy: us-gaap
concept: DerivativeNumberOfInstrumentsHeld
periodType: instant
unit: pure
representativeQueries:
- How many derivative instruments do we currently hold?
- What is the count of derivative instruments in our portfolio?
- Can you tell me the number of derivatives we have?
- What is the total number of derivative contracts held?
---

# Schema

Reports the `us-gaap:DerivativeNumberOfInstrumentsHeld` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
