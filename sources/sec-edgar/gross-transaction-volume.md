---
type: Financial Statement Concept
title: Gross Billing, Agent Transaction — SEC EDGAR
description: This measure reports the total amount of consideration expected to be
  received as an agent for products and services transferred to customers by another
  party. It specifically focuses on the gross billing before any deductions for payments
  made to the product or service provider, distinguishing it from net revenue measures.
  The amount is reported as a duration value in currency, indicating the expected
  revenue over a specified period.
tags:
- finance
- sec
- edgar
- us-gaap
- gross
- transaction
- volume
source: ./_access.md
taxonomy: us-gaap
concept: GrossTransactionVolume
periodType: duration
unit: currency
representativeQueries:
- What are the gross billings from agent transactions?
- Can you tell me the expected consideration from agent sales?
- How much are we expecting to receive as an agent for products sold?
- What is the gross billing amount for agent transactions this period?
---

# Schema

Reports the `us-gaap:GrossTransactionVolume` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
