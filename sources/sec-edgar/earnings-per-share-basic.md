---
type: Financial Statement Concept
title: Earnings Per Share, Basic — SEC EDGAR
description: This measure reports the amount of net income or loss for the period
  allocated per each share of common stock or unit outstanding during the reporting
  period for a publicly traded company or SEC filer. It is distinct from diluted earnings
  per share, as it does not account for potential dilution from convertible securities.
  The reporting is done as a duration value in per-share.
tags:
- finance
- sec
- edgar
- us-gaap
- earnings
- per
- share
- basic
source: ./_access.md
taxonomy: us-gaap
concept: EarningsPerShareBasic
periodType: duration
unit: per-share
representativeQueries:
- What is our basic earnings per share for this period?
- How much net income do we have per share of common stock?
- Can you provide the basic EPS for the reporting period?
---

# Schema

Reports the `us-gaap:EarningsPerShareBasic` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
