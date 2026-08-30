---
type: Financial Statement Concept
title: Deposit Assets — SEC EDGAR
description: This measure reports the carrying amount of the asset transferred to
  a third party to serve as a deposit, typically as security against failure to perform
  under an agreement. It describes the financial assets held by a publicly traded
  company or SEC filer that are designated as deposits. This measure is specific to
  deposit assets, distinguishing it from other asset categories that may not serve
  as security deposits. The value is reported as an instant value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- deposit
- assets
source: ./_access.md
taxonomy: us-gaap
concept: DepositAssets
periodType: instant
unit: currency
representativeQueries:
- What is the carrying amount of our deposit assets?
- How much do we have in assets transferred as deposits?
- Can you tell me the value of assets held as security deposits?
- What is the total amount of assets we have as deposits with third parties?
---

# Schema

Reports the `us-gaap:DepositAssets` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
