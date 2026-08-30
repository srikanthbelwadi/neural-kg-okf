#!/usr/bin/env bash
# Verified Google Cloud / Gemini configuration for Neural KG (ARD + OKF)

export LLM_PROVIDER=gemini
export GEMINI_API_KEY="AIzaSyBV6zrG-rjyyzo6Gstfi_iG7SZMUC5vhUo"
export CHAT_MODEL="gemini-2.5-flash"
export EMBED_MODEL="gemini-embedding-001"
export RERANK_MODEL="gemini-2.5-flash"
export SYNTHESIS_MODEL="gemini-2.5-pro"

# Google Cloud BigQuery & Firebase project
export GOOGLE_CLOUD_PROJECT="path2life-core-10389"
export BIGQUERY_LOCATION="US"
