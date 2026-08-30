---
type: Financial Statement Concept
title: Dividends, Stock — SEC EDGAR
description: This measure reports the total amount of stock dividends that have been
  declared, both paid and unpaid, for different classes of stock, such as common and
  preferred. It pertains to publicly traded companies and reflects their distribution
  of profits to shareholders in the form of additional shares. This measure is distinct
  from cash dividends, as it specifically focuses on stock dividends rather than cash
  payouts. The value is reported in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
- stock
source: ./_access.md
taxonomy: us-gaap
concept: DividendsStock
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of stock dividends declared?
- Can you provide details on the stock dividends for all classes of stock?
- How much in stock dividends have been declared overall?
---

# Schema

Reports the `us-gaap:DividendsStock` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
