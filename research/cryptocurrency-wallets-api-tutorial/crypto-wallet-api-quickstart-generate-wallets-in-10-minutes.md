# Crypto Wallet API Quickstart: Generate Wallets in 10 Minutes

> **Source:** https://www.cobo.com/post/crypto-wallet-api-quickstart
> **Retrieved:** 2026-06-01T00:00:00

---

## What Is a Crypto Wallet API?

A crypto wallet API enables programmatic wallet creation, address generation, and transaction management without building blockchain infrastructure.

**Cobo WaaS 2.0** supports 80+ blockchains and 3,000+ tokens via unified endpoints.

## Prerequisites

1. Cobo Account: Sign up at portal.cobo.com
2. API Credentials: Generate API key + secret in Cobo Portal
3. Dev environment: Python 3.7+ or Node.js 14+

## SDK Installation

Python:
```bash
pip install cobo-waas2
```

JavaScript:
```bash
npm install @cobo/cobo-waas2 --save
```

## Authentication

Python:
```python
import cobo_waas2
configuration = cobo_waas2.Configuration(
    api_private_key="<your-api-secret>",
    host="https://api.dev.cobo.com/v2"
)
```

JavaScript:
```javascript
const CoboWaas2 = require('@cobo/cobo-waas2');
apiClient.setPrivateKey("<your-api-secret>");
apiClient.setEnv(CoboWaas2.Env.DEV);
```

## Create Wallet

Python:
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

## Generate Deposit Address

```python
api_response = api_instance.create_address(
    wallet_id="<wallet-id>",
    chain_id="ETH"
)
print(f"Address: {api_response.address}")
```

## Check Balance

```python
balances = api_instance.list_token_balances_for_wallet(
    wallet_id="<wallet-id>"
)
```

## Send Transaction

```python
api_instance.create_transaction(
    wallet_id="<wallet-id>",
    chain_id="ETH",
    to_address="0x...",
    amount="0.1"
)
```

---

*Extracted by web-research-pipeline v1.0.0*