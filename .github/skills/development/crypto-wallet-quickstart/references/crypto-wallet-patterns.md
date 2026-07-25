# Crypto Wallet Quickstart Patterns

## Cobo WaaS 2.0 Setup

```python
import httpx

class CryptoWalletClient:
    def __init__(self, api_key: str, secret: str):
        self.api_key = api_key
        self.secret = secret
        self.base_url = "https://api.cobo.com/v2"
    
    async def create_wallet(self, chain: str, name: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/wallets",
                headers=self._headers(),
                json={"chain": chain, "name": name}
            )
            return response.json()
    
    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
```

## Deposit Address Generation

```python
async def generate_deposit_address(wallet_id: str, chain: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/wallets/{wallet_id}/addresses",
            headers=headers(),
            json={"chain": chain}
        )
        return response.json()
```

## Balance Query

```python
async def get_balance(wallet_id: str, chain: str, token: str = None):
    params = {"chain": chain}
    if token:
        params["token"] = token
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{base_url}/wallets/{wallet_id}/balance",
            headers=headers(),
            params=params
        )
        return response.json()
```

## Transaction Creation

```python
async def create_transaction(wallet_id: str, to: str, amount: str, chain: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/wallets/{wallet_id}/transactions",
            headers=headers(),
            json={"to": to, "amount": amount, "chain": chain}
        )
        return response.json()
```