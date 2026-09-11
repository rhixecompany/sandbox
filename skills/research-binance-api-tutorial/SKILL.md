---
name: research-binance-api-tutorial
title: Binance Spot API Research Digest
description: "Use when working with Binance Spot API: auth, endpoints, order types, rate limits, testnet. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [binance, api, crypto, research]
---

# Binance Spot API Research Digest

## Overview

Wraps `research/binance-api-tutorial/` (2 md files: step-by-step guide + official Spot API docs) with a CLI digest. Use when implementing Binance spot trading, reading docs, or recalling endpoints.

## When to Use

- Implementing Binance spot endpoints (candles, orders, account)
- Checking testnet setup or weight-based rate limits
- Answering questions about order types or auth (HMAC + timestamp)

## Workflow

### Phase 1: Digest

```bash
python scripts/research_binance_api_tutorial.py             # list files
python scripts/research_binance_api_tutorial.py --file "research/binance-api-tutorial/official-binance-spot-api-documentation-github.md"
```

### Phase 2: Apply

- Auth: `HMAC SHA256(signature=query+secret)`, timestamp within 1s recvWindow
- Base URLs: `https://api.binance.com` (spot prod), `https://testnet.binance.vision` (test)
- Rate limits: weight-based, 1200 req/min typical spot; backoff on 429/418
- Order types: LIMIT, MARKET, STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, TAKE_PROFIT_LIMIT, LIMIT_MAKER
- Always test on testnet first before prod keys

### Phase 3: Verify

- Run digest script; confirm expected section headings appear
- Cross-reference exact parameter names against the official docs file before coding

## Pitfalls

- Binance weights limits differ per endpoint — read the doc file's rate-limit table
- Never commit API keys; use testnet keys during development

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Facts used in code traced to a research file section

## References

- `research/binance-api-tutorial/binance-python-api-a-step-by-step-guide.md`
- `research/binance-api-tutorial/official-binance-spot-api-documentation-github.md`
- Script: `scripts/research_binance_api_tutorial.py` | Test: `scripts/tests/test_research_binance_api_tutorial.py`
