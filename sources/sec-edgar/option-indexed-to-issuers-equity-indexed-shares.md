---
type: Financial Statement Concept
title: Option Indexed to Issuer's Equity, Indexed Shares — SEC EDGAR
description: This measure reports the number of shares of the issuer's stock that
  an option contract is indexed to for a publicly traded company. It highlights the
  equity exposure related to the option, differentiating it from other financial instruments
  that may not be share-indexed. The value is reported as an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- option
- indexed
- issuers
- equity
source: ./_access.md
taxonomy: us-gaap
concept: OptionIndexedToIssuersEquityIndexedShares
periodType: instant
unit: shares
representativeQueries:
- How many shares are indexed to the issuer's equity in the option?
- What is the share count for the option contract linked to equity?
- Can you tell me the number of shares tied to the option?
---

# Schema

Reports the `us-gaap:OptionIndexedToIssuersEquityIndexedShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
