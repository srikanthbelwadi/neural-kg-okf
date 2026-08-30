---
type: Financial Statement Concept
title: Estimated Litigation Liability — SEC EDGAR
description: This measure represents the aggregate carrying amount of estimated litigation
  liabilities for a publicly traded company, accounting for known or probable losses
  from litigation, including associated costs like attorneys' fees. It is reported
  as an instant value in currency, reflecting the company's financial obligations
  related to legal matters. This measure is specific to litigation liabilities and
  does not encompass other types of liabilities or expenses.
tags:
- finance
- sec
- edgar
- us-gaap
- litigation
- reserve
source: ./_access.md
taxonomy: us-gaap
concept: LitigationReserve
periodType: instant
unit: currency
representativeQueries:
- What is the estimated litigation liability for known cases?
- Can you tell me the total estimated liability from litigation we expect?
- How much do we estimate we might owe in litigation costs?
---

# Schema

Reports the `us-gaap:LitigationReserve` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
