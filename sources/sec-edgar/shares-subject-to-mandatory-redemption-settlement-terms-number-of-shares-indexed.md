---
type: Financial Statement Concept
title: Financial Instruments Subject to Mandatory Redemption, Settlement Terms, Number
  of Shares Indexed — SEC EDGAR
description: This measure captures the number of shares to which a forward contract
  or an option indexed to the issuer's equity shares is linked. It pertains to financial
  instruments subject to mandatory redemption for a publicly traded company or SEC
  filer. This measure is distinct from other share metrics as it focuses specifically
  on indexed shares rather than total shares outstanding or other financial obligations.
  The value is reported as an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- shares
- subject
- mandatory
- redemption
source: ./_access.md
taxonomy: us-gaap
concept: SharesSubjectToMandatoryRedemptionSettlementTermsNumberOfSharesIndexed
periodType: instant
unit: shares
representativeQueries:
- What is the number of shares indexed to the forward contract?
- Can you tell me how many shares are tied to the option contract?
- How many shares does the contract reference for equity indexing?
- What is the share count for the indexed financial instrument?
---

# Schema

Reports the `us-gaap:SharesSubjectToMandatoryRedemptionSettlementTermsNumberOfSharesIndexed` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
