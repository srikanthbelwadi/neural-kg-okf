---
type: Financial Statement Concept
title: Management Fee Expense — SEC EDGAR
description: This measure reports the total expense incurred for management fees related
  to investment management for a publicly traded company or SEC filer. It includes
  costs associated with research, selection, supervision, and custody of investments.
  This measure is distinct from other management-related expenses as it specifically
  focuses on investment management fees, reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- management
- fee
- expense
source: ./_access.md
taxonomy: us-gaap
concept: ManagementFeeExpense
periodType: duration
unit: currency
representativeQueries:
- What is the amount of management fee expense incurred?
- Can you tell me the total expense for investment management fees?
- How much did we spend on management fees for investment services?
- What is the total expense for management fees related to investments?
---

# Schema

Reports the `us-gaap:ManagementFeeExpense` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
