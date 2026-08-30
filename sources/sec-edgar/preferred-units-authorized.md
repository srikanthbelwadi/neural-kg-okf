---
type: Financial Statement Concept
title: Preferred Units, Authorized — SEC EDGAR
description: This measure counts the total number of preferred units that a publicly
  traded company is authorized to issue, as specified in its corporate charter. It
  provides insight into the potential equity structure of the organization, indicating
  how many preferred shares can be created. This measure is distinct from issued or
  outstanding units, as it reflects the maximum limit set by the company rather than
  the actual shares that have been issued or are currently held by investors. The
  value is reported as an instant value in shares.
tags:
- finance
- sec
- edgar
- us-gaap
- preferred
- units
- authorized
source: ./_access.md
taxonomy: us-gaap
concept: PreferredUnitsAuthorized
periodType: instant
unit: shares
representativeQueries:
- How many preferred units are authorized to be issued?
- Can you provide the number of preferred units that can be issued?
- What is the total number of preferred units authorized?
- How many preferred units are allowed for issuance?
---

# Schema

Reports the `us-gaap:PreferredUnitsAuthorized` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
