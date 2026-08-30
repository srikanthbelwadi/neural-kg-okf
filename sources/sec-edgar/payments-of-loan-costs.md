---
type: Financial Statement Concept
title: Payments of Loan Costs — SEC EDGAR
description: This measure captures the cash outflow associated with loan origination
  costs for a publicly traded company, typically collected through escrow. It is reported
  as a duration value in currency, indicating the expenses incurred over a specified
  period. This measure is focused on the costs of initiating loans and does not include
  ongoing servicing fees or other loan-related expenses.
tags:
- finance
- sec
- edgar
- us-gaap
- payments
- loan
- costs
source: ./_access.md
taxonomy: us-gaap
concept: PaymentsOfLoanCosts
periodType: duration
unit: currency
representativeQueries:
- What are the cash outflows for loan costs?
- Can you provide the total payments made for loan origination costs?
- How much did we spend on loan costs this period?
---

# Schema

Reports the `us-gaap:PaymentsOfLoanCosts` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
