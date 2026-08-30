---
type: Financial Statement Concept
title: Fee Income — SEC EDGAR
description: This measure captures the total amount of fee income generated, including
  various types of fees such as managerial assistance and servicing of investments.
  It applies to publicly traded companies or SEC filers and encompasses a broad range
  of fee-related income, distinguishing it from other income types. The amount is
  reported in currency and reflects the financial performance over a fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- fee
- income
source: ./_access.md
taxonomy: us-gaap
concept: FeeIncome
periodType: duration
unit: currency
representativeQueries:
- What is the total fee income for the period?
- Can you break down the fee income from services and origination fees?
- How much fee income did we earn this quarter?
---

# Schema

Reports the `us-gaap:FeeIncome` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
