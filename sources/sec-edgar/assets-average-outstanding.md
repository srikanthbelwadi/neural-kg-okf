---
type: Financial Statement Concept
title: Assets, Average Outstanding — SEC EDGAR
description: This measure reports the average amount outstanding of both interest-earning
  and noninterest-earning assets for a publicly traded company or SEC filer. It provides
  a comprehensive view of the company's asset base, encompassing all types of assets
  that contribute to its financial position. This measure is broader than those focusing
  solely on interest-earning or noninterest-earning assets, as it combines both categories.
  The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- assets
- average
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: AssetsAverageOutstanding
periodType: duration
unit: currency
representativeQueries:
- What is the average amount of all assets?
- Can you provide the average for total assets?
- How much are the average outstanding assets?
- What’s the average for interest-earning and noninterest-earning assets?
---

# Schema

Reports the `us-gaap:AssetsAverageOutstanding` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
