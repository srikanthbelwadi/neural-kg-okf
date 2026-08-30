---
type: Financial Statement Concept
title: Loan Processing Fee — SEC EDGAR
description: This measure captures the total expenses paid for obtaining loans by
  a publicly traded company or SEC filer, including application and origination fees.
  It specifically counts costs associated with the loan acquisition process. This
  measure is focused on loan processing expenses, distinguishing it from other financial
  expenses that may not relate directly to loan procurement. The value is reported
  as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- loan
- processing
- fee
source: ./_access.md
taxonomy: us-gaap
concept: LoanProcessingFee
periodType: duration
unit: currency
representativeQueries:
- What are the loan processing fees we incurred?
- Can you tell me the expenses related to obtaining loans?
- How much did we spend on application and origination fees?
- What is the total for loan processing expenses?
---

# Schema

Reports the `us-gaap:LoanProcessingFee` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
