---
type: Financial Statement Concept
title: Partners' Capital Account, Distributions — SEC EDGAR
description: This measure captures the total distributions made to each class of partners,
  including general, limited, and preferred partners, during the fiscal year in a
  publicly traded company. It differs from other measures by encompassing all distributions
  rather than focusing on specific types like deferred compensation or option exercises.
  The total is reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- partners
- capital
- account
- distributions
source: ./_access.md
taxonomy: us-gaap
concept: PartnersCapitalAccountDistributions
periodType: duration
unit: currency
representativeQueries:
- What were the total distributions to each class of partners?
- Can you provide the distribution amounts for general, limited, and preferred partners?
- How much did each class of partners receive in distributions?
---

# Schema

Reports the `us-gaap:PartnersCapitalAccountDistributions` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
