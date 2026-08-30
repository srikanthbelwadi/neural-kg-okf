---
type: Financial Statement Concept
title: FIFO Inventory Amount — SEC EDGAR
description: FIFO Inventory Amount reports the value of inventory using the FIFO (first
  in, first out) method at the reporting date, particularly when multiple valuation
  methods are used. This measure is relevant to publicly traded companies and reflects
  their inventory valuation practices. It is distinct from other inventory measures
  as it specifically pertains to the FIFO method rather than average cost or LIFO
  methods. The value is reported in currency as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- inventory
- amount
source: ./_access.md
taxonomy: us-gaap
concept: FIFOInventoryAmount
periodType: instant
unit: currency
representativeQueries:
- What is the FIFO inventory amount at the reporting date?
- Can you tell me how much FIFO inventory we have?
- What is the total value of FIFO inventory on the balance sheet?
- How much inventory is valued using FIFO method?
---

# Schema

Reports the `us-gaap:FIFOInventoryAmount` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
