---
type: Financial Statement Concept
title: Payment for Pension Benefits — SEC EDGAR
description: This measure indicates the cash outflow for pension benefits, including
  employer contributions to fund plan assets and payments to retirees. It is relevant
  to companies that provide pension plans to their employees. This measure is distinct
  from other employee benefit measures as it specifically pertains to pension contributions,
  excluding other postretirement benefits. The value is reported as a duration value
  in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- pension
- contributions
source: ./_access.md
taxonomy: us-gaap
concept: PensionContributions
periodType: duration
unit: currency
representativeQueries:
- What is the cash outflow for pension benefits?
- How much did we pay out for pension contributions and retiree payments?
- Can you provide the amount spent on pension benefits?
---

# Schema

Reports the `us-gaap:PensionContributions` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
