---
type: Financial Statement Concept
title: Loss Contingency, Damages Awarded, Value — SEC EDGAR
description: This measure captures the total amount of damages awarded to a plaintiff
  in a legal matter, reflecting the financial liability recognized by a publicly traded
  company or SEC filer. It provides insight into the potential financial impact of
  legal contingencies on the company's financial position. This measure is distinct
  from amounts paid, as it focuses solely on awarded damages rather than actual cash
  outflows. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- loss
- contingency
- damages
- awarded
source: ./_access.md
taxonomy: us-gaap
concept: LossContingencyDamagesAwardedValue
periodType: duration
unit: currency
representativeQueries:
- What is the amount of damages awarded in the legal case?
- Can you provide the value of damages that were awarded to the plaintiff?
- What is the total damages awarded in this legal matter?
---

# Schema

Reports the `us-gaap:LossContingencyDamagesAwardedValue` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
