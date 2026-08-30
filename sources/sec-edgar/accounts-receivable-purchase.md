---
type: Financial Statement Concept
title: Accounts Receivable, Purchase — SEC EDGAR
description: This measure indicates the amount of increase in accounts receivable
  resulting from their purchase. It applies to publicly traded companies and SEC filers,
  capturing the financial impact of acquiring accounts receivable. This measure is
  distinct from other accounts receivable measures as it specifically focuses on the
  increase due to purchases, rather than sales or other transactions. The reported
  value is expressed in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- accounts
- receivable
- purchase
source: ./_access.md
taxonomy: us-gaap
concept: AccountsReceivablePurchase
periodType: duration
unit: currency
representativeQueries:
- How much did we increase accounts receivable from purchases?
- What is the amount added to accounts receivable due to purchases?
- Can you tell me the increase in accounts receivable from recent purchases?
---

# Schema

Reports the `us-gaap:AccountsReceivablePurchase` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
