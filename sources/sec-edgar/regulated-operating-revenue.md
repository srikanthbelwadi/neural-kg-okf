---
type: Financial Statement Concept
title: Regulated Operating Revenue — SEC EDGAR
description: This measure captures the total amount of regulated operating revenues
  recognized during a reporting period by a publicly traded company. It specifically
  pertains to revenues that are regulated, distinguishing it from unregulated revenues.
  The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- regulated
- operating
- revenue
source: ./_access.md
taxonomy: us-gaap
concept: RegulatedOperatingRevenue
periodType: duration
unit: currency
representativeQueries:
- What is the total regulated operating revenue recognized this period?
- How much revenue did we generate from regulated operations?
- Can you provide the total amount of our regulated operating revenue?
---

# Schema

Reports the `us-gaap:RegulatedOperatingRevenue` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
