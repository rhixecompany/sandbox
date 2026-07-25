# Paystack Developer Patterns

## Authentication

```python
import httpx

async def get_paystack_auth():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.paystack.co/oauth/token",
            data={
                "grant_type": "client_credentials",
                "client_id": "your_client_id",
                "client_secret": "your_client_secret"
            }
        )
        return response.json()["access_token"]
```

## Transaction Initialization

```python
async def initialize_transaction(amount, email, reference):
    token = await get_paystack_auth()
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.paystack.co/transaction/initialize",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "amount": amount * 100,  # In kobo
                "email": email,
                "reference": reference
            }
        )
        return response.json()
```

## Verification

```python
async def verify_transaction(reference):
    token = await get_paystack_auth()
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.paystack.co/transaction/verify/{reference}",
            headers={"Authorization": f"Bearer {token}"}
        )
        return response.json()
```

## Webhooks

```python
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.post("/webhook/paystack")
async def paystack_webhook(request: Request):
    payload = await request.json()
    # Verify signature
    # Process event: charge.success, transfer.success, etc.
    return {"status": "ok"}
```

## Error Handling

```python
# Common error codes
ERRORS = {
    "insufficient_funds": "Customer has insufficient funds",
    "card_declined": "Card was declined",
    "expired_card": "Card has expired",
    "invalid_pin": "Invalid PIN entered"
}
```