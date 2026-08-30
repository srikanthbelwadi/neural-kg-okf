---
type: Financial Statement Concept
title: Cash, FDIC Insured Amount — SEC EDGAR
description: This measure indicates the amount of cash deposited in financial institutions
  that is insured by the Federal Deposit Insurance Corporation as of the balance sheet
  date. It is relevant to publicly traded companies and provides insight into the
  safety of cash holdings. This measure is distinct from total cash holdings as it
  specifically focuses on insured amounts, reported in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- cash
- insured
- amount
source: ./_access.md
taxonomy: us-gaap
concept: CashFDICInsuredAmount
periodType: instant
unit: currency
representativeQueries:
- What is the amount of cash that is FDIC insured?
- Can you tell me how much of our cash is insured by the FDIC?
- How much cash do we have that is covered by FDIC insurance?
---

# Schema

Reports the `us-gaap:CashFDICInsuredAmount` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
