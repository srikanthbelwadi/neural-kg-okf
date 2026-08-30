---
type: Financial Statement Concept
title: Shares, Outstanding — SEC EDGAR
description: This measure counts the number of shares that are currently outstanding,
  meaning they have been issued and are not held in treasury or cancelled. It applies
  to publicly traded companies and provides a snapshot of the equity available to
  shareholders. This measure is distinct from total shares issued, as it excludes
  shares that are not actively available in the market. The count is reported in shares
  as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- shares
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: SharesOutstanding
periodType: instant
unit: shares
representativeQueries:
- How many shares are currently outstanding?
- What is the total number of shares issued that are not held in treasury?
- Can you tell me the count of outstanding shares?
- What is the number of shares that are currently active and not canceled?
---

# Schema

Reports the `us-gaap:SharesOutstanding` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
