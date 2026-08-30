---
type: Financial Statement Concept
title: Investments and Cash — SEC EDGAR
description: This measure represents the total sum of investments and unrestricted
  cash held by a publicly traded company or SEC filer as of the balance sheet date.
  It provides insight into the liquidity and investment position of the organization.
  This measure is distinct from other financial metrics as it specifically combines
  both investments and cash, rather than focusing on one or the other. The value is
  reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- investments
- and
- cash
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentsAndCash
periodType: instant
unit: currency
representativeQueries:
- What is the total amount of investments and unrestricted cash on the balance sheet?
- Can you tell me the sum of cash and investments as of the balance sheet date?
- What is the value of unrestricted cash combined with investments?
---

# Schema

Reports the `us-gaap:InvestmentsAndCash` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
