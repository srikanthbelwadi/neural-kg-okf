---
type: Financial Statement Concept
title: Dividends Receivable — SEC EDGAR
description: Dividends Receivable indicates the carrying amount of dividends that
  have been declared but not yet received by a publicly traded company as of the balance
  sheet date. This measure specifically focuses on dividends, distinguishing it from
  other types of receivables that may not involve dividend payments. It is reported
  as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
- receivable
source: ./_access.md
taxonomy: us-gaap
concept: DividendsReceivable
periodType: instant
unit: currency
representativeQueries:
- What are the dividends receivable on the balance sheet?
- Can you show me the amount of declared dividends that we haven't received?
- How much do we have in dividends that are due to us?
---

# Schema

Reports the `us-gaap:DividendsReceivable` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
