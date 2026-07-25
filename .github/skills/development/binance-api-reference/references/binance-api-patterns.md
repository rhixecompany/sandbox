# Binance API Reference Patterns

## REST API Endpoints

### Market Data
```python
# Get ticker
GET /api/v3/ticker/24hr?symbol=BTCUSDT

# Get klines
GET /api/v3/klines?symbol=BTCUSDT&interval=1h&limit=100

# Get order book
GET /api/v3/depth?symbol=BTCUSDT&limit=100
```

### Account (Signed)
```python
import hmac
import hashlib
import time

def sign_params(params, secret):
    query = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    signature = hmac.new(secret.encode(), query.encode(), hashlib.sha256).hexdigest()
    return {**params, "signature": signature}

# Get account info
GET /api/v3/account?timestamp=...&signature=...
```

## WebSocket Streams

```python
import asyncio
import websockets
import json

async def binance_ws(symbol):
    url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"
    async with websockets.connect(url) as ws:
        async for msg in ws:
            data = json.loads(msg)
            print(f"{data['s']}: {data['p']} @ {data['q']}")

asyncio.run(binance_ws("btcusdt"))
```

## Rate Limits

| Endpoint | Weight | Limit |
|----------|--------|-------|
| /api/v3/ticker/24hr | 1 | 1200/min |
| /api/v3/klines | 1 | 1200/min |
| /api/v3/account | 10 | 1200/min |
| /api/v3/order | 1 | 50/sec |

## Error Codes

| Code | Meaning |
|------|---------|
| -1000 | Unknown error |
| -1001 | Disconnected |
| -1002 | Unauthorized |
| -1003 | Too many requests |
| -1013 | Invalid quantity |
| -1015 | Too many new orders |
| -1021 | Timestamp outside recvWindow |
| -1022 | Invalid signature |
| -2010 | Insufficient balance |
| -2011 | Order would trigger immediately |
| -2013 | Order does not exist |
| -2014 | API key format invalid |
| -2015 | Invalid API key |