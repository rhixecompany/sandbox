---
name: binance-python-api-tutorial
title: "Binance Python API Tutorial"
description: "Use when learning Binance Spot API with python-binance library — covers authentication, REST endpoints, WebSocket streaming, testnet usage, and security best practices."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [binance, python, api, trading, cryptocurrency, tutorial]
---
# Binance Python API Tutorial

## Purpose

Guide for programmatic trading on Binance using the `python-binance` library. Covers setup, authentication, key endpoints, WebSocket streams, and production safety.

## When to Use

- Building trading bots or portfolio trackers
- Learning Binance REST/WebSocket APIs
- Integrating Binance into financial applications
- Testnet development before live trading

## When NOT to Use

- Other exchanges (use CCXT for multi-exchange)
- Non-Python environments
- Production trading without proper risk management

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug API errors, rate limits, signature issues |
| `test-driven-development` | Write tests for order logic before live trading |

## Workflow

### Phase 1: Setup & Authentication

1. **Create Binance account** → Enable 2FA
2. **Generate API keys** → Profile → API Management → Create API
3. **Set permissions** → Enable Spot Trading, disable Withdrawals for safety
4. **Install library** → `pip install python-binance`
5. **Configure environment** → Store keys in `.env` (never hardcode)

```python
import os
from binance.client import Client

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)
```

### Phase 2: Core REST Operations

**Account & Market Data**
```python
# Account info (requires signature)
account = client.get_account()

# Symbol ticker
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

# Order book depth
depth = client.get_order_book(symbol="BTCUSDT", limit=100)
```

**Trading Operations**
```python
# Place LIMIT order
order = client.create_order(
    symbol="BTCUSDT",
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_LIMIT,
    timeInForce=Client.TIME_IN_FORCE_GTC,
    quantity=0.001,
    price="50000"
)

# Check open orders
open_orders = client.get_open_orders(symbol="BTCUSDT")

# Cancel order
client.cancel_order(symbol="BTCUSDT", orderId=order["orderId"])
```

### Phase 3: WebSocket Real-Time Streams

```python
from binance import ThreadedWebsocketManager

def handle_socket_message(msg):
    if msg["e"] == "trade":
        print(f"Trade: {msg['s']} @ {msg['p']} qty={msg['q']}")

twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
twm.start()
twm.start_trade_socket(callback=handle_socket_message, symbol="BTCUSDT")
# twm.join()  # block main thread
```

### Phase 4: Testnet Development

```python
testnet_client = Client(api_key, api_secret, testnet=True)
# Base URL: https://testnet.binance.vision/api
```

### Phase 5: Production Safety Checklist

- [ ] Rate limit handling (1200 weight/min, 10 orders/sec)
- [ ] Timestamp synchronization (recvWindow)
- [ ] Error handling for -1021, -2010, -1100, -1121
- [ ] IP whitelisting configured
- [ ] Withdrawal permissions disabled on API key
- [ ] Order validation before placement
- [ ] Idempotency for order retries

## Pitfalls

- **Timestamp drift** → Sync with `client.get_server_time()` before signed requests
- **Rate limit bans** → Implement exponential backoff; respect `X-MBX-USED-WEIGHT` header
- **Float precision** → Use `Decimal` for quantities/prices; Binance rejects scientific notation
- **Testnet ≠ Production** → Separate API keys, different base URLs, reset data periodically
- **WebSocket reconnection** → Handle disconnections; use `ThreadedWebsocketManager` auto-reconnect

## Verification Checklist

- [ ] Environment variables loaded (not hardcoded)
- [ ] Testnet orders place successfully
- [ ] WebSocket receives real-time trades
- [ ] Rate limit headers monitored
- [ ] Error codes handled gracefully
- [ ] No withdrawal permissions on trading keys

## References

- `references/binance-api-endpoints.md` — Complete endpoint reference
- `references/python-binance-patterns.md` — Common code patterns
- `references/error-codes.md` — Binance error code meanings

## Templates

- `templates/.env.example` — Environment variable template
- `templates/testnet-config.py` — Testnet client configuration

## Scripts

- `scripts/sync-time.py` — Server time synchronization utility
- `scripts/rate-limit-monitor.py` — Weight usage tracker