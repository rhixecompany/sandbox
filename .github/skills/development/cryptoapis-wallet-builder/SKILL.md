---
name: cryptoapis-wallet-builder
title: "Build Crypto Wallets using CryptoAPIs"
description: "Use when building crypto wallet infrastructure with CryptoAPIs — covers deposit address generation, wallet transactions, HD wallet sync, and why use APIs for wallet development."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [cryptoapis, wallet, blockchain, hd-wallet, deposit-address, transactions, api]
---
# Build Crypto Wallets using CryptoAPIs

## Purpose

Build crypto wallet infrastructure with CryptoAPIs — covers deposit address generation, wallet transactions, HD wallet sync, and API benefits.

## When to Use

- Building wallet-as-a-service infrastructure
- Need multi-chain support (100+ endpoints)
- Want to focus on app logic, not blockchain infrastructure
- Enterprise security requirements (ISO, GDPR, TÜV)

## When NOT to Use

- High-performance/low-latency requirements (use native OpenCV)
- Non-Pi platforms
- Production facial recognition (use specialized SDKs)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug WebRTC signaling, OpenCV.js loading, camera access |
| `executing-plans` | Multi-component setup (UV4L + web server + signaling) |

## Workflow

### Phase 1: Key Takeaways

- Crypto wallets store blockchain addresses and private keys
- APIs streamline wallet development — focus on app logic
- CryptoAPIs provides 100+ endpoints for wallet development

### Phase 2: Core Endpoints

**Generate Deposit Address**
- Create new receiving addresses within a wallet
- Docs: https://developers.cryptoapis.io/technical-documentation/api/wallet-as-a-service/generating/generate-deposit-address

**Create Transaction from Wallet**
- Initiate transactions from entire wallet (not single address)
- Docs: https://developers.cryptoapis.io/technical-documentation/api/wallet-as-a-service/transactions/create-coins-transaction-request-from-wallet

**Sync HD Wallet (xPub, yPub, zPub)**
- Automatically synchronize Hierarchical Deterministic wallets
- Docs: https://developers.cryptoapis.io/technical-documentation/api/blockchain-data/hd-wallets/sync-hd-wallet-xpub-ypub-zpub

### Phase 3: Why Use APIs?

- Faster time-to-market
- Scalability across blockchains
- Enterprise security (ISO, GDPR, TÜV certified)
- Focus on innovation, not infrastructure

### Phase 4: Supported Blockchains

Bitcoin, Ethereum, Litecoin, Bitcoin Cash, Dogecoin, Dash, and many more.

### Phase 5: Platform Considerations

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: set environment variables via set API_KEY=xxx")
    elif system == "linux":
        print("Linux: export API_KEY=xxx or use .env files")
    elif system == "darwin":
        print("macOS: same as Linux for env vars")
    return system

# Test with sandbox
def get_cryptoapis_url(use_testnet: bool = True):
    if use_testnet:
        return "https://api.cryptoapis.io/v2"  # Testnet
    return "https://api.cryptoapis.io/v2"  # Mainnet (same URL, different API key)
```

### Phase 6: Error Handling

```python
import httpx
import asyncio

class CryptoAPIsError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code}: {message}")

ERROR_CODES = {
    400: "Bad Request — Check parameters",
    401: "Unauthorized — Invalid API key",
    404: "Not Found — Resource doesn't exist",
    422: "Validation Error — Check request body",
    429: "Rate Limited — Implement exponential backoff",
    500: "Server Error — Retry with backoff",
}

async def cryptoapis_request(client, method, url, **kwargs):
    for attempt in range(3):
        try:
            response = await client.request(method, url, **kwargs)
            if response.status_code == 429:
                delay = 2 ** attempt
                await asyncio.sleep(delay)
                continue
            if response.status_code >= 500:
                await asyncio.sleep(2 ** attempt)
                continue
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error = ERROR_CODES.get(e.response.status_code, "Unknown error")
            raise CryptoAPIsError(e.response.status_code, error)
        except httpx.RequestError as e:
            if attempt == 2:
                raise ConnectionError(f"Network error: {e}")
            await asyncio.sleep(1)
```

## Pitfalls

- **Custodial model** — CryptoAPIs holds keys; not for self-custody
- **API rate limits** — Implement exponential backoff
- **Chain-specific params** — Each blockchain has unique transaction fields
- **Testnet vs mainnet** — Separate API keys and endpoints

## Verification Checklist

- [ ] Deposit address generation works
- [ ] Transaction creation returns valid txid
- [ ] HD wallet sync captures all derived addresses
- [ ] Webhook receives confirmed transactions
- [ ] Error handling for chain-specific failures

## References

- `references/cryptoapis-endpoints.md` — Full endpoint catalog
- `references/cryptoapis-webhooks.md` — Webhook events and verification
- `references/cryptoapis-chains.md` — Per-chain parameter reference
- `references/cryptoapis-patterns.md` — Code patterns and error handling

## Templates

- `templates/hd-wallet-config.json` — Sync configuration
- `templates/cryptoapis-client-config.py` — Client initialization template

## Scripts

- `scripts/cryptoapis-address-generator.py` — Bulk address generation
- `scripts/cryptoapis-test-connection.py` — API connectivity test