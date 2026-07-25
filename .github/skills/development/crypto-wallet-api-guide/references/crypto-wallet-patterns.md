# Crypto Wallet API Patterns

## Address Generation

```python
from cryptoapis import CryptoAPIs

api = CryptoAPIs(api_key="your_api_key")

# Generate deposit address for Bitcoin
address = api.blockchain.address.generate(
    blockchain="bitcoin",
    network="mainnet",
    label="user_123_deposit"
)
```

## Wallet Creation

```python
# Create HD wallet
wallet = api.wallet.create(
    name="user_wallet",
    blockchain="ethereum",
    network="mainnet"
)

# Get wallet details
details = api.wallet.get(wallet_id=wallet.id)
```

## Transaction Monitoring

```python
# List transactions for address
transactions = api.blockchain.address.transactions(
    blockchain="bitcoin",
    network="mainnet",
    address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
)

# Webhook for confirmations
async def handle_webhook(payload):
    if payload["event"] == "ADDRESS_TRANSACTION_CONFIRMED":
        await process_deposit(payload["data"])
```