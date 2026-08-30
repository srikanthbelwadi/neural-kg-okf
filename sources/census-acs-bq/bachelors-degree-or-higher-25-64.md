---
type: US Census ACS (BigQuery) — County & State Demographics Measure (BigQuery)
title: Bachelors Degree Population (bachelors_degree_or_higher_25_64) — US Census
  ACS (BigQuery) — County & State Demographics
description: Rank, filter, and aggregate by bachelors degree population (bachelors_degree_or_higher_25_64)
  using Google Cloud BigQuery.
tags:
- census-acs-bq
- bigquery
- ranking
- aggregate
- population
- bachelors-degree-or-higher-25-64
source: ./_access.md
bq:
  table: bigquery-public-data.census_bureau_acs.county_2018_5yr
  field: bachelors_degree_or_higher_25_64
  entity_field: geo_id
  entity_kind: fips
  source: US Census ACS (BigQuery) — County & State Demographics
  unit: count
  name_table: bigquery-public-data.geo_us_boundaries.counties
  name_key: geo_id
  name_field: county_name
representativeQueries:
- counties with highest college educated population
---

# Schema & Access

Provides SQL ranking and filtering for `bachelors_degree_or_higher_25_64` (Bachelors Degree Population) over `bigquery-public-data.census_bureau_acs.county_2018_5yr`.
