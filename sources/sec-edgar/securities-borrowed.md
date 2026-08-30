---
type: Financial Statement Concept
title: Securities Borrowed — SEC EDGAR
description: Amount, after the effects of master netting arrangements, of securities
  borrowed from entities in exchange for collateral. Includes assets not subject to
  a master netting arrangement and not elected to be offset.
tags:
- finance
- sec
- edgar
- us-gaap
- securities
- borrowed
source: ./_access.md
taxonomy: us-gaap
concept: SecuritiesBorrowed
periodType: instant
unit: currency
representativeQueries:
- What is the amount of securities we have borrowed?
- Can you provide the value of securities borrowed after netting arrangements?
- How much do we owe for borrowed securities?
- What is the total value of our borrowed securities?
---

# Schema

Reports the `us-gaap:SecuritiesBorrowed` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
