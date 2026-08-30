---
type: Financial Statement Concept
title: Derivative Liability, Number of Instruments Held — SEC EDGAR
description: This measure counts the number of derivative instruments held by a publicly
  traded company within a particular derivative liability or group of derivative liabilities.
  It provides insight into the company's obligations and risk exposure related to
  derivatives. This measure is distinct from derivative asset measures, as it focuses
  specifically on liabilities, highlighting the potential financial risks associated
  with these instruments. The value is reported as an instant value in pure.
tags:
- finance
- sec
- edgar
- us-gaap
- derivative
- liability
- number
- instruments
source: ./_access.md
taxonomy: us-gaap
concept: DerivativeLiabilityNumberOfInstrumentsHeld
periodType: instant
unit: pure
representativeQueries:
- How many derivative instruments are held for this liability?
- Can you provide the count of derivative liabilities held?
- What is the number of instruments for the derivative liability?
---

# Schema

Reports the `us-gaap:DerivativeLiabilityNumberOfInstrumentsHeld` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
