---
type: Financial Statement Concept
title: Forward Contract Indexed to Issuer's Equity, Indexed Shares — SEC EDGAR
description: This measure counts the number of shares of the issuer's stock that a
  forward contract is indexed to, specifically for a publicly traded company. It provides
  insight into the equity exposure associated with the forward contract, distinguishing
  it from other financial instruments that may not be indexed to shares. The reported
  value is an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- forward
- contract
- indexed
- issuers
source: ./_access.md
taxonomy: us-gaap
concept: ForwardContractIndexedToIssuersEquityIndexedShares
periodType: instant
unit: shares
representativeQueries:
- How many shares are indexed to the issuer's equity in the forward contract?
- What is the share count for the forward contract linked to equity?
- Can you tell me the number of shares tied to the forward contract?
---

# Schema

Reports the `us-gaap:ForwardContractIndexedToIssuersEquityIndexedShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
