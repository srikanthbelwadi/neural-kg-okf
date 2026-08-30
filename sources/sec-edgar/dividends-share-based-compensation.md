---
type: Financial Statement Concept
title: Dividend, Share-Based Payment Arrangement — SEC EDGAR
description: This measure aggregates the amount of paid and unpaid cash, stock, and
  paid-in-kind dividends declared for awards under share-based payment arrangements.
  It is relevant to publicly traded companies and provides a comprehensive view of
  all forms of dividends related to equity compensation. This measure is distinct
  from individual dividend types, as it encompasses all forms of dividends rather
  than focusing on a single type. The value is reported in currency for the duration
  of the period.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
- share
- based
- compensation
source: ./_access.md
taxonomy: us-gaap
concept: DividendsShareBasedCompensation
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of dividends declared for share-based payment arrangements?
- Can you tell me the combined cash, stock, and paid-in-kind dividends for share-based
  payments?
- How much in total dividends were declared for share-based payment awards?
- What is the overall dividend amount for share-based payment arrangements?
---

# Schema

Reports the `us-gaap:DividendsShareBasedCompensation` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
