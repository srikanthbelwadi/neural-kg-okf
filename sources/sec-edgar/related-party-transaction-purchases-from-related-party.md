---
type: Financial Statement Concept
title: Related Party Transaction, Purchases from Related Party — SEC EDGAR
description: This measure captures the total purchases made during the reporting period
  from related parties, excluding any transactions that are eliminated in consolidated
  financial statements. It is relevant to a publicly traded company or SEC filer and
  provides insight into the nature of transactions with related entities. This measure
  is distinct from other purchase metrics, as it specifically focuses on related party
  transactions. The reported value is expressed in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- related
- party
- transaction
- purchases
source: ./_access.md
taxonomy: us-gaap
concept: RelatedPartyTransactionPurchasesFromRelatedParty
periodType: duration
unit: currency
representativeQueries:
- What purchases did we make from related parties this period?
- Can you list the transactions with related parties?
- How much did we spend on purchases from related parties?
- What are the related party purchases for this financial period?
---

# Schema

Reports the `us-gaap:RelatedPartyTransactionPurchasesFromRelatedParty` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
