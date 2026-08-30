---
type: Financial Statement Concept
title: Excess Stock, Shares Issued — SEC EDGAR
description: Excess Stock, Shares Issued reports the number of excess stock shares
  that a publicly traded company has sold or granted to its shareholders. This measure
  specifically counts shares that exceed the authorized amount for issuance. It is
  distinct from shares outstanding, as it focuses solely on the excess portion rather
  than the total shares held by shareholders. The value is reported as an instant
  value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- excess
- stock
- shares
- issued
source: ./_access.md
taxonomy: us-gaap
concept: ExcessStockSharesIssued
periodType: instant
unit: shares
representativeQueries:
- What is the number of excess stock shares that have been issued?
- How many excess stock shares have been sold or granted to shareholders?
- Can you tell me the total issued amount of excess stock shares?
---

# Schema

Reports the `us-gaap:ExcessStockSharesIssued` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
