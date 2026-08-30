---
type: Financial Statement Concept
title: Collateralized Agreements — SEC EDGAR
description: This measure encompasses the total value of collateralized agreements,
  which includes securities purchased under agreements to resell, borrowed securities,
  and secured demand notes. It pertains to publicly traded companies that engage in
  collateralized transactions. This measure is distinct from other financial asset
  measures as it specifically focuses on collateralized agreements rather than general
  asset holdings. The value is reported in currency as an instant value.
tags:
- finance
- sec
- edgar
- us-gaap
- collateralized
- agreements
source: ./_access.md
taxonomy: us-gaap
concept: CollateralizedAgreements
periodType: instant
unit: currency
representativeQueries:
- What is the total of our collateralized agreements?
- Can you tell me about the collateralized agreements we have in place?
- How much do we have in collateralized agreements including repos and secured notes?
---

# Schema

Reports the `us-gaap:CollateralizedAgreements` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
