---
type: Financial Statement Concept
title: Increase (Decrease) in Securities Borrowed — SEC EDGAR
description: This measure captures the change in the total amount due to the entity
  from securities borrowed transactions during the reporting period. It reflects the
  financial position of a publicly traded company or SEC filer regarding borrowed
  securities. This measure is distinct from other receivables as it specifically pertains
  to securities borrowed, rather than general accounts receivable or other financial
  instruments. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- increase
- decrease
- securities
- borrowed
source: ./_access.md
taxonomy: us-gaap
concept: IncreaseDecreaseInSecuritiesBorrowed
periodType: duration
unit: currency
representativeQueries:
- What is the increase or decrease in securities borrowed?
- Can you tell me how much we owe from securities borrowed transactions?
- How much has our securities borrowed liability changed recently?
---

# Schema

Reports the `us-gaap:IncreaseDecreaseInSecuritiesBorrowed` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
