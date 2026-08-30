---
type: Financial Statement Concept
title: Income Tax Paid, before Refund Received — SEC EDGAR
description: This measure captures the total amount of cash paid as income tax to
  various jurisdictions, before any refunds are received. It applies to publicly traded
  companies and reflects their tax obligations over a specified duration. This measure
  is distinct from tax liabilities as it specifically reports cash outflows rather
  than accrued tax expenses. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- income
- taxes
- paid
source: ./_access.md
taxonomy: us-gaap
concept: IncomeTaxesPaid
periodType: duration
unit: currency
representativeQueries:
- What is the amount of income tax paid before receiving a refund?
- How much cash was paid in income tax to various jurisdictions?
- Can you provide details on the income tax paid amount?
---

# Schema

Reports the `us-gaap:IncomeTaxesPaid` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
