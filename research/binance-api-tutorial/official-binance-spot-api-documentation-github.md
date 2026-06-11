# Official Binance Spot API Documentation

> **Source:** https://github.com/binance/binance-spot-api-docs
> **Retrieved:** 2026-06-01T00:00:00

---

## Core Documentation Files

| File | Description |
|------|-------------|
| rest-api.md | Spot REST API – trading, account, market data |
| web-socket-api.md | Spot WebSocket API |
| web-socket-streams.md | Market Data WebSocket Streams |
| user-data-stream.md | User Data WebSocket Streams |
| sbe-market-data-streams.md | SBE Market Data Streams |
| fix-api.md | FIX API |
| enums.md | Enum definitions |
| errors.md | Error codes and messages |
| filters.md | Trading rules and filters |

## API Base URLs

| Environment | URL |
|-------------|-----|
| Production REST | https://api.binance.com |
| Production WS | wss://stream.binance.com:9443 |
| Testnet REST | https://testnet.binance.vision |
| Data API | https://data-api.binance.vision |

## Authentication

- API Key required for private endpoints
- HMAC SHA256 signature for signed endpoints
- Timestamp required (server time sync critical)
- `X-MBX-APIKEY` header for all authenticated requests

## Order Types

- LIMIT, MARKET, STOP_LOSS, STOP_LOSS_LIMIT
- TAKE_PROFIT, TAKE_PROFIT_LIMIT
- LIMIT_MAKER, TRAILING_STOP_MARKET

## Rate Limits (Weight-based)

| Limit Type | Weight |
|------------|--------|
| REQUEST_WEIGHT | 1200/min |
| ORDERS | 10/sec, 100,000/day |
| RAW_REQUESTS | 6,000/min |

## Error Codes

Common errors:
- -1021: Timestamp outside recvWindow
- -2010: Insufficient balance
- -1100: Illegal characters in parameter
- -1121: Invalid symbol

---

*Extracted by web-research-pipeline v1.0.0*