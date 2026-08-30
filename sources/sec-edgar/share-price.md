---
type: Financial Statement Concept
title: Share Price — SEC EDGAR
description: This measure represents the price of a single share of a publicly traded
  company's stock that is available for sale. It provides a snapshot of the market
  value of the company's equity, reflecting investor sentiment and market conditions.
  This measure is distinct from other financial metrics that may aggregate share prices
  or focus on different aspects of stock performance. The value is reported as an
  instant value in per-share.
tags:
- finance
- sec
- edgar
- us-gaap
- share
- price
source: ./_access.md
taxonomy: us-gaap
concept: SharePrice
periodType: instant
unit: per-share
representativeQueries:
- What is the current share price of the company's stock?
- How much is one share of the company's stock selling for?
- Can you provide the price per share for the company's stock?
---

# Schema

Reports the `us-gaap:SharePrice` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
