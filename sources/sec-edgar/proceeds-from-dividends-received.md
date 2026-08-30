---
type: Financial Statement Concept
title: Proceeds from Dividends Received — SEC EDGAR
description: This measure indicates the dividends received on equity and other investments
  during the current period. It pertains to publicly traded companies or SEC filers
  that hold such investments. This measure is distinct as it specifically focuses
  on the income generated from dividends, rather than overall investment returns or
  cash flows. The value is reported in currency for the fiscal year.
tags:
- finance
- sec
- edgar
- us-gaap
- proceeds
- from
- dividends
- received
source: ./_access.md
taxonomy: us-gaap
concept: ProceedsFromDividendsReceived
periodType: duration
unit: currency
representativeQueries:
- How much did we receive in dividends this period?
- What are the proceeds from dividends received on our investments?
- Can you tell me the total dividends we received?
- What was the amount of dividends collected from our equity investments?
---

# Schema

Reports the `us-gaap:ProceedsFromDividendsReceived` concept (duration) per company, by fiscal period, from SEC filings. Query by `cik` via the linked source's `company_concept` operation; see [SEC EDGAR access](./_access.md).
