# Paystack Webhook Events

## Event Types

| Event | Description | Data |
|-------|-------------|------|
| `charge.success` | Payment successful | Transaction object |
| `charge.failed` | Payment failed | Transaction object |
| `transfer.success` | Transfer completed | Transfer object |
| `transfer.failed` | Transfer failed | Transfer object |
| `transfer.reversed` | Transfer reversed | Transfer object |
| `subscription.create` | Subscription created | Subscription object |
| `subscription.disable` | Subscription cancelled | Subscription object |
| `invoice.create` | Invoice generated | Invoice object |
| `invoice.payment_failed` | Invoice payment failed | Invoice object |

## Payload Structure

```json
{
  "event": "charge.success",
  "data": {
    "id": 12345,
    "reference": "ref_xxx",
    "amount": 10000,
    "currency": "NGN",
    "status": "success",
    "customer": {"email": "user@example.com"},
    "paid_at": "2024-01-15T10:30:00.000Z"
  }
}
```

## Verification

```python
import hmac
import hashlib

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha512).hexdigest()
    return hmac.compare_digest(expected, signature)
```

## Best Practices

1. **Respond quickly** — 2xx within 5s, else retry
2. **Idempotency** — Process each event once (use event ID)
3. **Queue processing** — Offload to background worker
4. **Retry logic** — Exponential backoff for failures
5. **Logging** — Log all webhooks for debugging