---
type: Financial Statement Concept
title: Members' Equity — SEC EDGAR
description: This measure reports the total amount of ownership interest held by members
  in a limited liability company (LLC). It describes the equity stake attributable
  to the parent entity, indicating the financial interest of its members. This measure
  is distinct from total assets or liabilities, as it specifically focuses on ownership
  equity rather than overall financial position. The value is reported as an instant
  value in currency.
tags:
- finance
- sec
- edgar
- us-gaap
- members
- equity
source: ./_access.md
taxonomy: us-gaap
concept: MembersEquity
periodType: instant
unit: currency
representativeQueries:
- What is the amount of members' equity in the LLC?
- Can you tell me about the ownership interest in the limited liability company?
- What is the total equity attributable to the parent entity in the LLC?
- How much is the members' equity in the company?
---

# Schema

Reports the `us-gaap:MembersEquity` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
