---
type: Financial Statement Concept
title: Liabilities, Average Amount Outstanding — SEC EDGAR
description: This measure captures the average amount outstanding of both interest-bearing
  and noninterest-bearing liabilities for a publicly traded company or SEC filer.
  It provides insight into the company's total obligations, encompassing all types
  of liabilities that impact its financial health. This measure is broader than those
  focusing solely on interest-bearing or noninterest-bearing liabilities, as it combines
  both categories. The value is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- liabilities
- average
- amount
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: LiabilitiesAverageAmountOutstanding
periodType: duration
unit: currency
representativeQueries:
- What is the average amount of all liabilities?
- Can you tell me the average for total liabilities?
- How much are the average outstanding liabilities?
- What’s the average for interest-bearing and noninterest-bearing liabilities?
---

# Schema

Reports the `us-gaap:LiabilitiesAverageAmountOutstanding` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
