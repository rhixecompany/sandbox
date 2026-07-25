---
name: crypto-wallet-quickstart
title: "Crypto Wallet API Quickstart (Cobo WaaS 2.0)"
description: "Use when setting up Cobo WaaS 2.0 for wallet creation, address generation, balance checking, and transactions — covers Python and JavaScript SDKs."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [cobo, wallet, waas, custodial, wallet-api, quickstart, python, javascript]
---
# Crypto Wallet API Quickstart (Cobo WaaS 2.0)

## Purpose

Get started with Cobo WaaS 2.0 for programmatic wallet management across 80+ blockchains and 3,000+ tokens.

## When to Use

- Building custodial wallet infrastructure
- Need multi-chain support (80+ chains)
- Python or JavaScript environment
- Enterprise wallet-as-a-service

## When NOT to Use

- Non-custodial/self-custody requirements
- Single-chain only (lighter alternatives exist)
- No KYB process capability

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug wallet creation, transaction failures |
| `requesting-code-review` | Security review for custodial keys |

## Workflow

### Phase 1: Prerequisites

1. **Cobo Account** → portal.cobo.com
2. **API Credentials** → API key + secret in Cobo Portal
3. **Environment** → Python 3.7+ or Node.js 14+
4. **Environment Selection** → Dev: `https://api.dev.cobo.com/v2`, Prod: `https://api.cobo.com/v2`

### Phase 2: SDK Installation

**Python:**
```bash
pip install cobo-waas2
```

**JavaScript:**
```bash
npm install @cobo/cobo-waas2 --save
```

### Phase 3: Authentication

**Python:**
```python
import cobo_waas2
configuration = cobo_waas2.Configuration(
    api_private_key="<your-api-secret>",
    host="https://api.dev.cobo.com/v2"
)
```

**JavaScript:**
```javascript
const CoboWaas2 = require('@cobo/cobo-waas2');
apiClient.setPrivateKey("<your-api-secret>");
apiClient.setEnv(CoboWaas2.Env.DEV);
```

### Phase 4: Create Wallet

```python
from cobo_waas2 import CreateCustodialWalletParams, WalletType, WalletSubtype

create_wallet_params = cobo_waas2.CreateWalletParams(
    actual_instance=CreateCustodialWalletParams(
        name="My First Wallet",
        wallet_type=WalletType.CUSTODIAL,
        wallet_subtype=WalletSubtype.ASSET,
    )
)
api_response = api_instance.create_wallet(create_wallet_params=create_wallet_params)
print(f"Wallet ID: {api_response.wallet_id}")
```

### Phase 5: Generate Deposit Address

```python
api_response = api_instance.create_address(
    wallet_id="<wallet-id>",
    chain_id="ETH"
)
print(f"Address: {api_response.address}")
```

### Phase 6: Check Balance

```python
balances = api_instance.list_token_balances_for_wallet(
    wallet_id="<wallet-id>"
)
```

### Phase 7: Send Transaction

```python
api_instance.create_transaction(
    wallet_id="<wallet-id>",
    chain_id="ETH",
    to_address="0x...",
    amount="0.1"
)
```

### Phase 8: Platform Detection

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use pip install cobo-waas2 in virtual environment")
    elif system == "linux":
        print("Linux: Ensure libffi-dev is installed for cobo SDK")
    elif system == "darwin":
        print("macOS: Use brew install libffi if needed")
    return system

# Set environment based on platform
def get_cobo_env():
    import os
    # Always start with dev/testnet for safety
    return os.getenv("COBO_ENV", "dev")
```

### Phase 9: Error Handling

```python
import cobo_waas2
from cobo_waas2.exceptions import ApiException

def handle_wallet_error(e: ApiException):
    status = e.status
    body = e.body
    
    if status == 400:
        return f"Bad request: {body}"
    elif status == 401:
        return "Authentication failed — check API credentials"
    elif status == 403:
        return "Permission denied — wallet access restricted"
    elif status == 404:
        return "Resource not found — check wallet ID/chain ID"
    elif status == 429:
        return "Rate limit exceeded — implement backoff"
    elif status >= 500:
        return f"Server error: {body} — retry with backoff"
    return f"Unknown error: {body}"

# Usage
try:
    wallet = api_instance.create_wallet(...)
except ApiException as e:
    print(f"Error: {handle_wallet_error(e)}")
```

## Pitfalls

- **Dev vs Prod** → Separate keys, separate endpoints
- **Wallet subtypes** → CUSTODIAL/ASSET vs MPC/USER — choose correctly
- **Chain ID format** → Use Cobo's chain IDs (e.g., "ETH", "BTC", "SOL")
- **Webhook verification** → Validate signatures for transaction callbacks
- **Rate limits** → Implement retry with exponential backoff

## Verification Checklist

- [ ] SDK installed and authenticated
- [ ] Wallet created successfully
- [ ] Deposit address generated for target chain
- [ ] Balance query returns expected tokens
- [ ] Test transaction completes on devnet
- [ ] Webhook receives transaction notifications

## References

- `references/cobo-endpoints.md` — Full API reference
- `references/cobo-chains.md` — Supported chains and IDs
- `references/cobo-webhooks.md` — Webhook events and verification

## Templates

- `templates/cobo-config.py` / `cobo-config.js` — Configuration templates

## Scripts

- `scripts/cobo-wallet-setup.py` — Complete wallet creation flow
- `scripts/cobo-health-check.py` — API connectivity test