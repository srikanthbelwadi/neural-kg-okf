---
type: Financial Statement Concept
title: Common Stock, Value, Outstanding — SEC EDGAR
description: This measure represents the value of common shares held by shareholders
  of a publicly traded company or SEC filer. It specifically excludes common shares
  that have been repurchased and are held as treasury shares. This measure is distinct
  from other common stock metrics as it focuses on the outstanding value rather than
  total common stock or treasury shares. The value is reported as an instant value
  in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- common
- stock
- value
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: CommonStockValueOutstanding
periodType: instant
unit: currency
representativeQueries:
- What is the value of outstanding common shares held by shareholders?
- Can you provide the total value of common stock excluding treasury shares?
- What is the value of common shares that are not repurchased?
---

# Schema

Reports the `us-gaap:CommonStockValueOutstanding` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
