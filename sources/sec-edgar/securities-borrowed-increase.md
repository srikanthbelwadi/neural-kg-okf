---
type: Financial Statement Concept
title: Securities Borrowed, Increase — SEC EDGAR
description: This measure captures the amount of increase in securities borrowed resulting
  from entering into new transactions. It is applicable to publicly traded companies
  and SEC filers, providing insight into the financial activities related to borrowing
  securities. This measure is distinct from other borrowing metrics, as it specifically
  focuses on increases in borrowed securities, and is reported as a duration value
  in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- securities
- borrowed
- increase
source: ./_access.md
taxonomy: us-gaap
concept: SecuritiesBorrowedIncrease
periodType: duration
unit: currency
representativeQueries:
- What is the increase in borrowed securities from new transactions?
- Can you provide details on the increase in securities borrowed?
- How much did we increase our borrowed securities from entering new transactions?
---

# Schema

Reports the `us-gaap:SecuritiesBorrowedIncrease` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
