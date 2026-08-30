---
type: Financial Statement Concept
title: Repayments of Senior Debt — SEC EDGAR
description: Repayments of Senior Debt capture the cash outflow for long-term debt
  where the holder has the highest claim on the entity's assets in the event of bankruptcy
  or liquidation. This measure is relevant to publicly traded companies or SEC filers
  with senior debt obligations. It is distinguished from other debt repayment measures
  by its focus on the priority of claims associated with the debt. The cash outflow
  is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- repayments
- senior
- debt
source: ./_access.md
taxonomy: us-gaap
concept: RepaymentsOfSeniorDebt
periodType: duration
unit: currency
representativeQueries:
- What were the repayments of senior debt this period?
- Can you tell me how much we paid back on senior loans?
- How much cash went out for senior debt repayments?
---

# Schema

Reports the `us-gaap:RepaymentsOfSeniorDebt` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
