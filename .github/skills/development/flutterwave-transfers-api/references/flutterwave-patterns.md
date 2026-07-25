# Flutterwave Transfers API Patterns

## Authentication

```python
import httpx

async def get_flutterwave_auth():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.flutterwave.com/v3/transfers",
            headers={
                "Authorization": "Bearer YOUR_SECRET_KEY",
                "Content-Type": "application/json"
            }
        )
        return response.json()
```

## Create Transfer

```python
async def create_transfer(amount, currency, account_bank, account_number, reference):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.flutterwave.com/v3/transfers",
            headers={
                "Authorization": "Bearer YOUR_SECRET_KEY",
                "Content-Type": "application/json"
            },
            json={
                "account_bank": account_bank,
                "account_number": account_number,
                "amount": amount,
                "currency": currency,
                "reference": reference,
                "narration": "Transfer payment"
            }
        )
        return response.json()
```

## Verify Transfer

```python
async def verify_transfer(transfer_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.flutterwave.com/v3/transfers/{transfer_id}",
            headers={"Authorization": "Bearer YOUR_SECRET_KEY"}
        )
        return response.json()
```

## Bulk Transfers

```python
async def create_bulk_transfer(transfers, title):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.flutterwave.com/v3/bulk-transfers",
            headers={
                "Authorization": "Bearer YOUR_SECRET_KEY",
                "Content-Type": "application/json"
            },
            json={
                "title": title,
                "transfers": transfers
            }
        )
        return response.json()
```

## Webhook Handling

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook/flutterwave")
async def flutterwave_webhook(request: Request):
    payload = await request.json()
    # Verify hash signature
    # Process: transfer.completed, transfer.failed, etc.
    return {"status": "received"}
```