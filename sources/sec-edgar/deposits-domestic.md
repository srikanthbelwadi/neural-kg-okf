---
type: Financial Statement Concept
title: Deposits, Domestic — SEC EDGAR
description: This measure reports the total aggregate of all domestic interest-bearing
  and noninterest-bearing deposit liabilities held by a publicly traded company or
  SEC filer. It specifically captures the company's liabilities related to deposits,
  distinguishing it from other types of liabilities. This measure is broader than
  specific deposit categories, as it includes both interest-bearing and noninterest-bearing
  deposits. The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- deposits
- domestic
source: ./_access.md
taxonomy: us-gaap
concept: DepositsDomestic
periodType: instant
unit: currency
representativeQueries:
- What are the domestic deposits we have?
- Can you tell me the total of all domestic deposit liabilities?
- What is the amount of our domestic interest-bearing and noninterest-bearing deposits?
---

# Schema

Reports the `us-gaap:DepositsDomestic` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
