---
type: Financial Statement Concept
title: Taxes and Licenses — SEC EDGAR
description: This measure reports the total amount of tax expenses incurred by a publicly
  traded company or SEC filer, excluding income, excise, production, and property
  taxes, as well as licenses and fees not related to production. It provides a focused
  view of tax liabilities that are not part of the standard income tax calculations.
  This measure is distinct from broader tax measures as it specifically excludes certain
  types of taxes, reported as a duration value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- taxes
- and
- licenses
source: ./_access.md
taxonomy: us-gaap
concept: TaxesAndLicenses
periodType: duration
unit: currency
representativeQueries:
- What is the total tax expense excluding income and property taxes?
- Can you tell me the amount for taxes and licenses not related to production?
- How much did we incur in taxes and licenses this period?
- What is the total amount of tax expenses excluding income taxes?
---

# Schema

Reports the `us-gaap:TaxesAndLicenses` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
