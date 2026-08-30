---
type: Financial Statement Concept
title: Employee Stock Ownership Plan (ESOP), Number of Suspense Shares — SEC EDGAR
description: This measure reports the number of suspense shares in an Employee Stock
  Ownership Plan (ESOP) for a publicly traded company. It specifically counts shares
  that have not yet been allocated or released to participants, distinguishing it
  from allocated shares. The value is reported in shares as an instant value, reflecting
  the status at a specific point in time.
tags:
- finance
- sec
- edgar
- us-gaap
- employee
- stock
- ownership
- plan
source: ./_access.md
taxonomy: us-gaap
concept: EmployeeStockOwnershipPlanESOPNumberOfSuspenseShares
periodType: instant
unit: shares
representativeQueries:
- How many suspense shares are currently in the ESOP?
- What is the number of shares that have not yet been allocated in the ESOP?
- Can you tell me the total number of suspense shares in the Employee Stock Ownership
  Plan?
---

# Schema

Reports the `us-gaap:EmployeeStockOwnershipPlanESOPNumberOfSuspenseShares` concept (instant) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
