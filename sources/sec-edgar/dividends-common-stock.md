---
type: Financial Statement Concept
title: Dividends, Common Stock — SEC EDGAR
description: The amount of paid and unpaid common stock dividends declared, settled
  in cash, stock, or payment-in-kind (PIK) is reported by a publicly traded company
  or SEC filer. This measure provides insight into the company's dividend policy and
  shareholder returns. It is reported in currency for the duration of the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- dividends
- common
- stock
source: ./_access.md
taxonomy: us-gaap
concept: DividendsCommonStock
periodType: duration
unit: currency
representativeQueries:
- What are the total dividends declared for common stock?
- Can you show me the amount of common stock dividends paid and unpaid?
- How much in common stock dividends do we have?
---

# Schema

Reports the `us-gaap:DividendsCommonStock` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
