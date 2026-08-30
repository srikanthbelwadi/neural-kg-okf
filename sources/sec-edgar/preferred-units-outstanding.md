---
type: Financial Statement Concept
title: Preferred Units, Outstanding — SEC EDGAR
description: This measure indicates the total number of preferred units that are currently
  outstanding for a publicly traded company, meaning these shares are held by investors
  and not held in the company's treasury. It provides a snapshot of the equity that
  is actively owned by shareholders. This measure differs from issued units, as it
  excludes any shares that may have been repurchased or are otherwise not in circulation.
  The value is reported as an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- preferred
- units
- outstanding
source: ./_access.md
taxonomy: us-gaap
concept: PreferredUnitsOutstanding
periodType: instant
unit: shares
representativeQueries:
- What is the number of preferred units outstanding?
- Can you provide the total number of preferred units currently held?
- How many preferred units are still outstanding?
- What is the count of preferred units that are not yet redeemed?
---

# Schema

Reports the `us-gaap:PreferredUnitsOutstanding` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
