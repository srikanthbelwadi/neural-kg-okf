---
type: Financial Statement Concept
title: Net Assets — SEC EDGAR
description: This measure represents the total amount of net assets, which is calculated
  as total assets minus total liabilities, for a publicly traded company or SEC filer
  at a specific point in time. It provides a snapshot of the company's financial health
  and overall value. This measure is distinct from other asset-related metrics as
  it specifically focuses on net assets rather than gross assets or liabilities. The
  value is reported in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- assets
- net
source: ./_access.md
taxonomy: us-gaap
concept: AssetsNet
periodType: instant
unit: currency
representativeQueries:
- What are the net assets?
- Can you tell me the total amount of net assets?
- How much are the net assets after liabilities?
---

# Schema

Reports the `us-gaap:AssetsNet` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
