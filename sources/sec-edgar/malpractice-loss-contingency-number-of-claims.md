---
type: Financial Statement Concept
title: Malpractice Loss Contingency, Number of Claims — SEC EDGAR
description: This measure counts the total number of outstanding malpractice claims
  at the end of the accounting period for a publicly traded company or SEC filer.
  It specifically provides a snapshot of the claims that have not yet been resolved.
  This measure is distinct from financial metrics that report costs or liabilities,
  as it focuses solely on the quantity of claims rather than their financial implications.
  It is reported as a pure count.
tags:
- finance
- sec
- edgar
- us-gaap
- malpractice
- loss
- contingency
- number
source: ./_access.md
taxonomy: us-gaap
concept: MalpracticeLossContingencyNumberOfClaims
periodType: instant
unit: pure
representativeQueries:
- How many malpractice claims are outstanding at the end of the period?
- What is the total number of malpractice claims we have?
- Can you tell me the number of outstanding malpractice claims?
---

# Schema

Reports the `us-gaap:MalpracticeLossContingencyNumberOfClaims` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
