---
type: Financial Statement Concept
title: Shares, Issued — SEC EDGAR
description: This measure counts the total number of shares of stock that have been
  issued by a publicly traded company as of the balance sheet date. It includes shares
  that were previously outstanding but are now held in the treasury. This measure
  is distinct from other share counts as it specifically focuses on issued shares
  rather than outstanding or authorized shares. The value is reported as an instant
  value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- shares
- issued
source: ./_access.md
taxonomy: us-gaap
concept: SharesIssued
periodType: instant
unit: shares
representativeQueries:
- How many shares have been issued as of the balance sheet date?
- Can you provide the total number of issued shares?
- What is the count of shares issued, including treasury shares?
---

# Schema

Reports the `us-gaap:SharesIssued` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
