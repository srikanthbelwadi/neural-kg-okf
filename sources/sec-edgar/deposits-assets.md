---
type: Financial Statement Concept
title: Deposits Assets — SEC EDGAR
description: This measure indicates the carrying value of amounts that a publicly
  traded company has transferred to third parties for security purposes, expected
  to be returned or applied towards payment in the future. It encompasses both current
  and long-term deposits, distinguishing it from current deposits. The reported value
  is an instant value in currency, representing the company's overall deposit assets.
tags:
- finance
- sec
- edgar
- us-gaap
- deposits
- assets
source: ./_access.md
taxonomy: us-gaap
concept: DepositsAssets
periodType: instant
unit: currency
representativeQueries:
- What is the total value of our deposits with third parties?
- Can you provide details on the deposits we expect to recover in the future?
- How much do we have in deposits that will be returned later?
---

# Schema

Reports the `us-gaap:DepositsAssets` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
