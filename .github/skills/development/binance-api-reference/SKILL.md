---
name: binance-api-reference
title: "Binance Spot API Reference"
description: "Use when needing official Binance Spot API endpoint specifications — REST API, WebSocket streams, authentication, rate limits, error codes, and enums."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [binance, api, reference, trading, cryptocurrency, rest, websocket]
---
# Binance Spot API Reference

## Purpose

Official Binance Spot API documentation reference for developers. Covers all endpoints, authentication, WebSocket streams, and error handling.

## When to Use

- Looking up exact endpoint parameters and responses
- Implementing custom Binance client (not using python-binance/CCXT)
- Debugging API integration issues
- Understanding rate limits and error codes

## When NOT to Use

- Quick trading bot (use python-binance or CCXT instead)
- Non-Binance exchanges
- High-level trading strategy design

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Trace API errors to root cause |
| `requesting-code-review` | Validate API integration before production |

## Workflow

### Phase 1: Authentication & Basics

**Base URLs**
| Environment | REST | WebSocket |
|-------------|------|-----------|
| Production | `https://api.binance.com` | `wss://stream.binance.com:9443` |
| Testnet | `https://testnet.binance.vision` | `wss://testnet.binance.vision` |
| Data API | `https://data-api.binance.vision` | — |

**Authentication**
- API Key required for private endpoints
- HMAC SHA256 signature for signed endpoints
- Timestamp required (server time sync critical)
- Header: `X-MBX-APIKEY: <api_key>`

### Phase 2: REST API Endpoints

**Market Data (Public)**
```
GET /api/v3/exchangeInfo     # Trading rules, symbols
GET /api/v3/ticker/price     # Current price
GET /api/v3/ticker/24hr      # 24hr statistics
GET /api/v3/depth            # Order book
GET /api/v3/trades           # Recent trades
GET /api/v3/klines           # Candlestick data
```

**Account (Private, Signed)**
```
GET /api/v3/account          # Balances, permissions
GET /api/v3/openOrders       # Open orders
POST /api/v3/order           # Place order
DELETE /api/v3/order         # Cancel order
GET /api/v3/order            # Query order
GET /api/v3/myTrades         # Trade history
```

### Phase 3: WebSocket Streams

**Market Streams (Public)**
- `<symbol>@trade` — Individual trades
- `<symbol>@depth<levels>` — Order book (5, 10, 20 levels)
- `<symbol>@kline_<interval>` — Candlesticks
- `<symbol>@ticker` — 24hr ticker
- `!ticker@arr` — All tickers

**User Data Stream (Private)**
1. `POST /api/v3/userDataStream` → get `listenKey`
2. Connect: `wss://stream.binance.com:9443/ws/<listenKey>`
3. Keepalive: `PUT /api/v3/userDataStream` every 30 min
4. Close: `DELETE /api/v3/userDataStream`

**Events:** `outboundAccountPosition`, `executionReport`, `balanceUpdate`

### Phase 4: Rate Limits & Errors

**Weight Limits**
| Limit | Weight |
|-------|--------|
| REQUEST_WEIGHT | 1200/min |
| ORDERS | 10/sec, 100,000/day |
| RAW_REQUESTS | 6,000/min |

**Common Errors**
| Code | Meaning |
|------|---------|
| -1021 | Timestamp outside recvWindow |
| -2010 | Insufficient balance |
| -1100 | Illegal characters in parameter |
| -1121 | Invalid symbol |

### Phase 5: Implementation Checklist

- [ ] Time sync before signed requests
- [ ] Weight tracking per endpoint
- [ ] Exponential backoff on 429/418
- [ ] listenKey keepalive for user stream
- [ ] Signature generation matches exactly
- [ ] recvWindow appropriate (5000-60000ms)

## Pitfalls

- **Signed vs unsigned confusion** — Account endpoints need signature; market data doesn't
- **Parameter ordering** — Signature includes all parameters in query string order
- **WebSocket reconnection** — Implement exponential backoff + listenKey refresh
- **Testnet data reset** — Testnet clears periodically; don't rely on persistent state

## Verification Checklist

- [ ] All target endpoints documented with params/responses
- [ ] Authentication flow works end-to-end
- [ ] WebSocket connects and receives events
- [ ] Error codes mapped to handling logic
- [ ] Rate limit tracking implemented

## References

- `references/rest-api-endpoints.md` — Full endpoint catalog
- `references/websocket-streams.md` — Stream payloads
- `references/enums.md` — Order types, sides, timeInForce values
- `references/filters.md` — Symbol filters (LOT_SIZE, PRICE_FILTER, etc.)
- `references/errors.md` — Complete error code reference
- `references/binance-api-patterns.md` — Code patterns for REST and WebSocket

## Templates

- `templates/binance-integration-checklist.md` — Production readiness checklist

## Scripts

- `scripts/binance-api-test.py` — Connectivity test script