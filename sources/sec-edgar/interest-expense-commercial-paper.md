---
type: Financial Statement Concept
title: Interest Expense, Commercial Paper — SEC EDGAR
description: This measure captures the amount of interest expense incurred on commercial
  paper by a publicly traded company or SEC filer. It is reported as a duration value
  in currency. This measure is distinct as it specifically focuses on commercial paper,
  which is a short-term borrowing instrument, rather than other forms of debt.
tags:
- finance
- sec
- edgar
- us-gaap
- interest
- expense
- commercial
- paper
source: ./_access.md
taxonomy: us-gaap
concept: InterestExpenseCommercialPaper
periodType: duration
unit: currency
representativeQueries:
- What is the interest expense on our commercial paper?
- How much interest are we incurring for commercial paper?
- Can you tell me the total interest expense related to commercial paper?
---

# Schema

Reports the `us-gaap:InterestExpenseCommercialPaper` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
