---
type: Financial Statement Concept
title: Derivative Asset, Number of Instruments Held — SEC EDGAR
description: This measure counts the number of derivative instruments held by a publicly
  traded company within a particular derivative asset or group of derivative assets.
  It provides insight into the company's exposure to derivatives and its risk management
  strategies. This measure is distinct from derivative liability measures, as it focuses
  solely on assets rather than liabilities, offering a different perspective on the
  company's financial instruments. The value is reported as an instant value in pure.
tags:
- finance
- sec
- edgar
- us-gaap
- derivative
- asset
- number
- instruments
source: ./_access.md
taxonomy: us-gaap
concept: DerivativeAssetNumberOfInstrumentsHeld
periodType: instant
unit: pure
representativeQueries:
- How many derivative instruments are held for this asset?
- Can you provide the count of derivative assets held?
- What is the number of instruments for the derivative asset?
---

# Schema

Reports the `us-gaap:DerivativeAssetNumberOfInstrumentsHeld` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
