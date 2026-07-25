# Paystack Error Handling

## HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process response |
| 400 | Bad Request | Check request format/params |
| 401 | Unauthorized | Verify API keys |
| 404 | Not Found | Check endpoint/resource ID |
| 422 | Validation Error | Check error details in response |
| 500 | Server Error | Retry with exponential backoff |
| 503 | Service Unavailable | Retry with exponential backoff |

## Common Error Responses

### Validation Error (422)
```json
{
  "status": false,
  "message": "Validation failed",
  "errors": {
    "email": ["The email field is required."],
    "amount": ["The amount must be at least 100."]
  }
}
```

### Authentication Error (401)
```json
{
  "status": false,
  "message": "Invalid API key",
  "errors": {}
}
```

## Retry Strategy

```python
import asyncio
import httpx

async def paystack_request_with_retry(client, method, url, **kwargs):
    max_retries = 3
    base_delay = 1.0
    
    for attempt in range(max_retries):
        try:
            response = await client.request(method, url, **kwargs)
            
            if response.status_code == 429:
                # Rate limited
                retry_after = int(response.headers.get("Retry-After", 60))
                await asyncio.sleep(retry_after)
                continue
                
            if response.status_code >= 500:
                # Server error - retry
                delay = base_delay * (2 ** attempt)
                await asyncio.sleep(delay)
                continue
                
            return response
            
        except httpx.RequestError as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            await asyncio.sleep(delay)
    
    raise Exception("Max retries exceeded")
```

## Idempotency

```python
# Always include idempotency key for mutations
headers = {
    "Authorization": f"Bearer {secret_key}",
    "Content-Type": "application/json",
    "Idempotency-Key": "unique-transaction-id-123"
}
```

## Webhook Verification

```python
import hmac
import hashlib

def verify_paystack_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha512
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```

## Common Integration Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Transaction not found" | Wrong reference | Verify reference matches |
| "Amount must be >= 100" | Amount in Naira not kobo | Multiply by 100 |
| "Invalid API key" | Sandbox key in production | Use correct environment keys |
| Webhook timeout | Slow processing | Respond 200 quickly, process async |