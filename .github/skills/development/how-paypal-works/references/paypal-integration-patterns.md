# PayPal Integration Patterns

## Authentication

```python
import httpx

async def get_access_token(client_id: str, client_secret: str, sandbox: bool = True):
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
async def create_order(token: str, amount: str, currency: str = "USD", sandbox: bool = True):
    base = "https://api-m.sandbox.paypal.com" if sandbox else "https://api-m.paypal.com"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base}/v2/checkout/orders",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json={
                "intent": "CAPTURE",
                "purchase_units": [{
                    "amount": {"currency_code": currency, "value": amount}
                }]
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

## Webhook Verification

```python
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, webhook_id: str, cert_url: str) -> bool:
    # In production, fetch and verify PayPal's certificate
    # For now, basic check
    expected = hmac.new(
        webhook_id.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```

## Error Handling

```python
ERROR_MAP = {
    "INVALID_RESOURCE_ID": "Order not found",
    "PERMISSION_DENIED": "Insufficient permissions",
    "INTERNAL_SERVER_ERROR": "PayPal internal error - retry",
    "RATE_LIMIT_REACHED": "Too many requests - backoff"
}

def handle_paypal_error(response: dict):
    details = response.get("details", [])
    for detail in details:
        issue = detail.get("issue")
        if issue in ERROR_MAP:
            return ERROR_MAP[issue]
    return "Unknown error"
```

## Rate Limits

- 100 requests/second per app
- 30 requests/second per token
- Use exponential backoff on 429