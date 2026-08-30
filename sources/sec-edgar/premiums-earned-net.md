---
type: Financial Statement Concept
title: Premiums Earned, Net — SEC EDGAR
description: This measure reports the net amount of premiums earned by a publicly
  traded company after accounting for premiums ceded to other entities and those assumed
  by the company. It distinguishes itself from gross premiums by focusing on the actual
  earnings from premiums, providing a clearer picture of revenue. The value is reported
  in currency and reflects a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- premiums
- earned
- net
source: ./_access.md
taxonomy: us-gaap
concept: PremiumsEarnedNet
periodType: duration
unit: currency
representativeQueries:
- What are our net premiums earned after ceding?
- How much did we earn in premiums after accounting for ceded and assumed premiums?
- Can you provide the total net premiums earned this period?
- What is the amount of premiums earned, net of cessions?
---

# Schema

Reports the `us-gaap:PremiumsEarnedNet` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
