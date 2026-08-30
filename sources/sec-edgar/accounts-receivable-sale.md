---
type: Financial Statement Concept
title: Accounts Receivable, Sale — SEC EDGAR
description: This measure reports the amount of decrease in accounts receivable resulting
  from their sale. It is relevant to publicly traded companies and SEC filers, capturing
  the financial impact of selling accounts receivable. This measure is distinct from
  other accounts receivable measures as it specifically focuses on the decrease due
  to sales, rather than purchases or other transactions. The reported value is expressed
  in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- accounts
- receivable
- sale
source: ./_access.md
taxonomy: us-gaap
concept: AccountsReceivableSale
periodType: duration
unit: currency
representativeQueries:
- How much did we decrease accounts receivable from sales?
- What is the amount deducted from accounts receivable due to sales?
- Can you tell me the decrease in accounts receivable from recent sales?
---

# Schema

Reports the `us-gaap:AccountsReceivableSale` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
