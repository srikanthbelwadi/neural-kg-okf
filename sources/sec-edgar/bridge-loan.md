---
type: Financial Statement Concept
title: Bridge Loan — SEC EDGAR
description: This measure represents short-term financing that is expected to be repaid
  relatively quickly, such as through a subsequent longer-term loan, for a publicly
  traded company or SEC filer. It is distinct from long-term debt, as it focuses on
  financing that is intended for immediate or near-term use. The reporting is done
  as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- bridge
- loan
source: ./_access.md
taxonomy: us-gaap
concept: BridgeLoan
periodType: instant
unit: currency
representativeQueries:
- What is the amount of our current bridge loan?
- How much short-term financing do we have outstanding?
- Can you tell me the total for our bridge financing?
---

# Schema

Reports the `us-gaap:BridgeLoan` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
