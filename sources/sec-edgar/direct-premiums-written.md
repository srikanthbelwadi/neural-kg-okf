---
type: Financial Statement Concept
title: Direct Premiums Written — SEC EDGAR
description: This measure indicates the total amount of premiums written by an entity
  before accounting for premiums ceded to other entities or assumed by the entity
  itself. It is relevant to a publicly traded company or SEC filer and provides insight
  into the company's insurance underwriting activities over a specific period. This
  measure is distinct from net premiums or other insurance-related metrics by focusing
  solely on the gross amount of premiums written. The value is reported in currency
  and reflects a duration value.
tags:
- finance
- sec
- edgar
- us-gaap
- direct
- premiums
- written
source: ./_access.md
taxonomy: us-gaap
concept: DirectPremiumsWritten
periodType: duration
unit: currency
representativeQueries:
- What is the total amount of direct premiums written?
- Can you tell me how much we wrote in premiums before any adjustments?
- What are the direct premiums we recorded this period?
- How much premium income did we generate before ceding?
---

# Schema

Reports the `us-gaap:DirectPremiumsWritten` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
