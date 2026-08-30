---
type: Financial Statement Concept
title: Security Sold Short, Shares — SEC EDGAR
description: This measure reports the total number of securities that a publicly traded
  company or SEC filer has sold short as of the end of the reporting period. It reflects
  the company's short selling activities, which can indicate market expectations or
  strategies. This measure is distinct from other investment metrics as it specifically
  focuses on short positions rather than long investments or overall investment holdings.
  The value is reported in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- investment
- sold
- not
- yet
source: ./_access.md
taxonomy: us-gaap
concept: InvestmentSoldNotYetPurchasedBalanceShares
periodType: instant
unit: shares
representativeQueries:
- How many securities have been sold short?
- Can you provide the number of shares sold short?
- What is the count of securities in the short position?
---

# Schema

Reports the `us-gaap:InvestmentSoldNotYetPurchasedBalanceShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
