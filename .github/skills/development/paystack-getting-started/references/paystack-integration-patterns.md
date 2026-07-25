# Paystack Integration Patterns

## Authentication

```python
import httpx

async def get_auth_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.paystack.co/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": "your_client_id",
                "client_secret": "your_client_secret"
            }
        )
        return response.json()["access_token"]
```

## Creating Transfers

```python
async def create_transfer(access_token: str, amount: int, recipient: str, reference: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.paystack.co/transfer",
            headers={"Authorization": f"Bearer {access_token}"},
            json={
                "source": "balance",
                "amount": amount,  # In kobo
                "recipient": recipient,
                "reference": reference
            }
        )
        return response.json()
```

## Webhook Verification

```python
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha512).hexdigest()
    return hmac.compare_digest(expected, signature)
```