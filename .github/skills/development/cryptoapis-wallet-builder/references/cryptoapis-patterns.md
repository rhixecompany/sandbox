# CryptoAPIs Wallet Builder Patterns

## Wallet Operations

```python
import httpx

class CryptoAPIsClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.cryptoapis.io/v2"
    
    def _headers(self):
        return {"X-API-Key": self.api_key, "Content-Type": "application/json"}

    async def create_wallet(self, blockchain: str, network: str, name: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/wallet-as-a-service/wallets",
                headers=self._headers(),
                json={"blockchain": blockchain, "network": network, "name": name}
            )
            return response.json()

    async def generate_address(self, wallet_id: str, blockchain: str, network: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/wallet-as-a-service/wallets/{wallet_id}/addresses",
                headers=self._headers(),
                json={"blockchain": blockchain, "network": network}
            )
            return response.json()

    async def create_transaction(self, wallet_id: str, to: str, amount: str, blockchain: str, network: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/wallet-as-a-service/wallets/{wallet_id}/transactions",
                headers=self._headers(),
                json={
                    "to": to,
                    "amount": amount,
                    "blockchain": blockchain,
                    "network": network,
                    "feePriority": "standard"
                }
            )
            return response.json()
```

## HD Wallet Sync

```python
async def sync_hd_wallet(wallet_id: str, blockchain: str, network: str):
    # Syncs all derived addresses for HD wallet
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/wallet-as-a-service/wallets/{wallet_id}/sync",
            headers=headers(),
            json={"blockchain": blockchain, "network": network}
        )
    return response.json()
```

## Webhook Setup

```python
async def create_webhook(url: str, events: list):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/webhooks",
            headers=headers(),
            json={"url": url, "events": events}
        )
    return response.json()
```