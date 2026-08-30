---
type: Financial Statement Concept
title: Order Flow Fees — SEC EDGAR
description: This measure quantifies the expense incurred by a publicly traded company
  for the cost of executing orders through other broker-dealers, known as order flow
  fees. It reflects the costs associated with trading activities, distinguishing it
  from other operational expenses that may not pertain to order execution. The reported
  value is in currency and reflects the duration of the expense over a specified period.
tags:
- finance
- sec
- edgar
- us-gaap
- order
- flow
- fees
source: ./_access.md
taxonomy: us-gaap
concept: OrderFlowFees
periodType: duration
unit: currency
representativeQueries:
- What are the order flow fees we incurred this period?
- Can you tell me the amount we spent on order flow fees?
- How much did we pay for other broker-dealers' executions of orders?
- What is the total expense for order flow fees?
---

# Schema

Reports the `us-gaap:OrderFlowFees` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
