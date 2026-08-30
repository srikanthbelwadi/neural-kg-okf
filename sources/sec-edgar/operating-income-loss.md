---
type: Financial Statement Concept
title: Operating Income (Loss) — SEC EDGAR
description: This measure reflects the net operating income or loss for a publicly
  traded company, calculated by deducting operating expenses from operating revenues.
  It provides insight into the company's operational efficiency and profitability,
  distinguishing it from net income measures that may include non-operating items.
  The value is reported in currency and reflects the duration of the income or loss
  over a specified period.
tags:
- finance
- sec
- edgar
- us-gaap
- operating
- income
- loss
source: ./_access.md
taxonomy: us-gaap
concept: OperatingIncomeLoss
periodType: duration
unit: currency
representativeQueries:
- What is our operating income or loss for the period?
- Can you tell me the net result of our operating revenues minus expenses?
- How much operating income did we generate this period?
- What is the total operating income or loss for the reporting period?
---

# Schema

Reports the `us-gaap:OperatingIncomeLoss` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
