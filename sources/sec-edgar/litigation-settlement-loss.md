---
type: Financial Statement Concept
title: Litigation Settlement, Loss — SEC EDGAR
description: This measure indicates the total loss incurred by a publicly traded company
  from litigation settlements awarded to other parties, representing the financial
  impact of legal disputes. It specifically excludes claims within an insurance entity's
  normal claims settlement process, distinguishing it from other litigation loss measures.
  The loss is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- litigation
- settlement
- loss
source: ./_access.md
taxonomy: us-gaap
concept: LitigationSettlementLoss
periodType: duration
unit: currency
representativeQueries:
- What is the loss from litigation settlement?
- How much did we lose in the litigation settlement?
- Can you provide the amount awarded to the other party in the lawsuit?
---

# Schema

Reports the `us-gaap:LitigationSettlementLoss` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
