---
type: Financial Statement Concept
title: Long-Term Debt — SEC EDGAR
description: This measure represents the total amount of long-term debt held by a
  publicly traded company or SEC filer, after accounting for unamortized premiums,
  discounts, and debt issuance costs. It is distinguished from current debt by focusing
  on obligations that extend beyond one year. The value is reported in currency as
  of the balance sheet date.
tags:
- finance
- sec
- edgar
- us-gaap
- long
- term
- debt
source: ./_access.md
taxonomy: us-gaap
concept: LongTermDebt
periodType: instant
unit: currency
representativeQueries:
- What is the total long-term debt after deductions?
- Can you tell me the amount of long-term debt excluding lease obligations?
- How much long-term debt do we have net of issuance costs?
- What is our long-term debt figure after accounting for premiums and discounts?
---

# Schema

Reports the `us-gaap:LongTermDebt` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
