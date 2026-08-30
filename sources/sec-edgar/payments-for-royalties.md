---
type: Financial Statement Concept
title: Payments for Royalties — SEC EDGAR
description: This measure captures the total cash paid by a publicly traded company
  for royalties during a specific period. It focuses on the outflow of cash related
  to royalty agreements, distinguishing it from income measures by its expense nature.
  The value is reported in currency and reflects a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- payments
- for
- royalties
source: ./_access.md
taxonomy: us-gaap
concept: PaymentsForRoyalties
periodType: duration
unit: currency
representativeQueries:
- What is the total amount paid for royalties this period?
- How much cash did we spend on royalties recently?
- Can you tell me the cash outflow for royalties during the current period?
- What is the amount of cash paid for royalty expenses?
---

# Schema

Reports the `us-gaap:PaymentsForRoyalties` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
