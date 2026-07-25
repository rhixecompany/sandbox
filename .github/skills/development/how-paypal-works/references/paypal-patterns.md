# PayPal Integration Patterns

## OAuth Token

```python
import httpx

async def get_paypal_token(client_id: str, client_secret: str, sandbox: bool = True):
    base = "https://api-m.sandbox.paypal.com" if sandbox else "https://api-m.paypal.com"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base}/v1/oauth2/token",
            auth=(client_id, client_secret),
            data={"grant_type": "client_credentials"}
        )
        return response.json()["access_token"]
```

## Create Order

```python
async def create_order(token: str, amount: str, currency: str, intent: str = "CAPTURE", sandbox: bool = True):
    base = "https://api-m.sandbox.paypal.com" if sandbox else "https://api-m.paypal.com"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base}/v2/checkout/orders",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={
                "intent": intent,
                "purchase_units": [{"amount": {"currency_code": currency, "value": amount}}]
            }
        )
        return response.json()
```

## Capture Payment

```python
async def capture_order(token: str, order_id: str, sandbox: bool = True):
    base = "https://api-m.sandbox.paypal.com" if sandbox else "https://api-m.paypal.com"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base}/v2/checkout/orders/{order_id}/capture",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        return response.json()
```

## Webhooks

```python
from fastapi import FastAPI, Request, HTTPException
import hashlib
import hmac

app = FastAPI()

@app.post("/webhook/paypal")
async def paypal_webhook(request: Request):
    payload = await request.body()
    # Verify signature
    transmission_id = request.headers.get("paypal-transmission-id")
    timestamp = request.headers.get("paypal-transmission-time")
    cert_url = request.headers.get("paypal-cert-url")
    auth_algo = request.headers.get("paypal-auth-algo")
    signature = request.headers.get("paypal-transmission-sig")
    
    # Verify using PayPal's certificate
    # Process event: CHECKOUT.ORDER.APPROVED, PAYMENT.CAPTURE.COMPLETED, etc.
    return {"status": "ok"}
```