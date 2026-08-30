---
type: Financial Statement Concept
title: Dividends, Cash — SEC EDGAR
description: This measure reports the total amount of cash dividends declared across
  various classes of stock, including both paid and unpaid amounts. It applies to
  publicly traded companies or SEC filers and is distinct from other dividend measures
  by encompassing all cash dividends rather than focusing on specific classes of stock.
  The value is reported in currency as a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
- cash
source: ./_access.md
taxonomy: us-gaap
concept: DividendsCash
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of cash dividends declared?
- Can you tell me about the cash dividends for all classes of stock?
- How much in cash dividends have been declared overall?
---

# Schema

Reports the `us-gaap:DividendsCash` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
