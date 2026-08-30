---
type: Financial Statement Concept
title: Securities Borrowed, Decrease — SEC EDGAR
description: This measure reports the amount of decrease in securities borrowed resulting
  from the settlement of transactions. It is relevant to publicly traded companies
  and SEC filers, reflecting the financial implications of settling borrowing transactions.
  This measure is distinct from other borrowing metrics, as it specifically addresses
  decreases in borrowed securities, and is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- securities
- borrowed
- decrease
source: ./_access.md
taxonomy: us-gaap
concept: SecuritiesBorrowedDecrease
periodType: duration
unit: currency
representativeQueries:
- What is the decrease in borrowed securities from settlement transactions?
- Can you tell me about the decrease in securities borrowed?
- How much did we decrease our borrowed securities from settlements?
---

# Schema

Reports the `us-gaap:SecuritiesBorrowedDecrease` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
