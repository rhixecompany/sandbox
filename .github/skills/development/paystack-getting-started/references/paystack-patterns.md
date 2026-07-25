# Paystack Getting Started Patterns

## Quick Setup

```python
import httpx

class PaystackClient:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.base_url = "https://api.paystack.co"
    
    def _headers(self):
        return {"Authorization": f"Bearer {self.secret_key}", "Content-Type": "application/json"}

    async def initialize_transaction(self, email: str, amount: int, reference: str):
        """Amount in kobo (multiply by 100)"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/transaction/initialize",
                headers=self._headers(),
                json={"email": email, "amount": amount, "reference": reference}
            )
            return response.json()

    async def verify_transaction(self, reference: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/transaction/verify/{reference}",
                headers=self._headers()
            )
            return response.json()

    async def create_transfer_recipient(self, name: str, account_number: str, bank_code: str, currency: str = "NGN"):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/transferrecipient",
                headers=self._headers(),
                json={
                    "type": "nuban",
                    "name": name,
                    "account_number": account_number,
                    "bank_code": bank_code,
                    "currency": currency
                }
            )
            return response.json()

    async def initiate_transfer(self, amount: int, recipient_code: str, reference: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/transfer",
                headers=self._headers(),
                json={
                    "source": "balance",
                    "amount": amount,
                    "recipient": recipient_code,
                    "reference": reference
                }
            )
            return response.json()
```

## Webhook Handler

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook/paystack")
async def paystack_webhook(request: Request):
    payload = await request.json()
    # Verify x-paystack-signature header
    event = payload.get("event")
    
    if event == "charge.success":
        data = payload["data"]
        # Process successful payment
        print(f"Payment successful: {data['reference']}")
    elif event == "transfer.success":
        # Process successful transfer
        pass
    
    return {"status": "received"}
```

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Bad request |
| 401 | Unauthorized |
| 404 | Not found |
| 422 | Validation error |
| 500 | Server error |