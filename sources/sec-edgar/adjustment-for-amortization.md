---
type: Financial Statement Concept
title: Amortization — SEC EDGAR
description: This measure indicates the total amount of noncash expense charged against
  earnings by a publicly traded company to allocate the cost of assets over their
  estimated remaining economic lives. It specifically pertains to amortization, distinguishing
  it from depreciation or other expense measures that may not involve asset allocation.
  The value is reported as a duration value in currency, reflecting the total expense
  over the reporting period.
tags:
- finance
- sec
- edgar
- us-gaap
- adjustment
- for
- amortization
source: ./_access.md
taxonomy: us-gaap
concept: AdjustmentForAmortization
periodType: duration
unit: currency
representativeQueries:
- What is the total amortization expense for this period?
- How much did we allocate for asset amortization this quarter?
- Can you break down the amortization charged against earnings?
- What is the recurring noncash expense for amortization?
---

# Schema

Reports the `us-gaap:AdjustmentForAmortization` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
