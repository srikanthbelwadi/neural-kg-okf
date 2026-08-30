---
type: Financial Statement Concept
title: Operating Lease, Payments — SEC EDGAR
description: This measure captures the total cash outflow related to operating lease
  payments made by publicly traded companies and SEC filers, excluding any costs associated
  with preparing another asset for its intended use. It reflects the ongoing financial
  commitments of the organization under operating leases, distinguishing it from other
  lease-related measures by omitting preparatory expenses. The value is reported as
  a duration in currency, indicating the cash flow over a specified period.
tags:
- finance
- sec
- edgar
- us-gaap
- operating
- lease
- payments
source: ./_access.md
taxonomy: us-gaap
concept: OperatingLeasePayments
periodType: duration
unit: currency
representativeQueries:
- What are the cash outflows from operating leases?
- Can you provide the amount paid for operating lease obligations?
- How much cash was spent on operating lease payments?
- What is the total cash outflow for operating leases?
---

# Schema

Reports the `us-gaap:OperatingLeasePayments` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
