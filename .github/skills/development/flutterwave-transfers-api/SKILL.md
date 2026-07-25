---
name: flutterwave-transfers-api
title: "Flutterwave Transfers API Introduction"
description: "Use when integrating Flutterwave Transfers for global fund transfers — covers authentication, account validation, transfer initiation, status querying, and required headers."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [flutterwave, transfers, api, payments, africa, global, fintech]
---
# Flutterwave Transfers API Introduction

## Purpose

Integrate Flutterwave Transfers for global fund transfers across bank accounts, mobile numbers, wallets, and cash pickups using the orchestrator flow.

## When to Use

- Building payout systems for Africa/global markets
- Automating bank transfers, mobile money, wallet transfers
- Implementing cash pickup functionality
- Multi-currency disbursement platforms

## When NOT to Use

- Card acquiring / payment collection (use Flutterwave Payments API)
- Non-transfer use cases
- Countries not supported by Flutterwave

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug auth tokens, idempotency, webhook failures |
| `test-driven-development` | Test transfer flows in sandbox before live |

## Workflow

### Phase 1: Prerequisites

1. **Onboard** at `https://onboarding.flutterwave.com/signup`
2. **Get credentials** → Client ID + Client Secret
3. **Understand flow** → One-time transfers (orchestrator) vs bulk (different flow)

### Phase 2: Transfer Flow (4 Steps)

#### Step 1: Generate Authorization Token

```bash
curl --location 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{YOUR_CLIENT_ID}}' \
  --data-urlencode 'client_secret={{YOUR_CLIENT_SECRET}}' \
  --data-urlencode 'grant_type=client_credentials'
```

Response: `access_token` (Bearer token, expires ~1 hour)

#### Step 2: Validate Customer Account

```bash
curl --request POST --url https://developersandbox-api.flutterwave.com/banks/account-resolve \
  --header 'content-type: application/json' \
  --data '{"account": {"code": "044", "number": "0690000040"}, "currency": "NGN"}'
```

Validates bank account exists before transfer.

#### Step 3: Initiate Transfer

```bash
curl --request POST --url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
  --header 'Authorization: Bearer ***' \
  --header 'Content-Type: application/json' \
  --header 'X-Trace-Id: {{TRACE_ID}}' \
  --header 'X-Idempotency-Key: {{IDEMPOTENCY_KEY}}' \
  --data '{
    "action": "instant",
    "payment_instruction": {
      "source_currency": "NGN",
      "amount": {"applies_to": "destination_currency", "value": 1000},
      "recipient": {"bank": {"account_number": "0122333334", "code": "044"}},
      "destination_currency": "NGN"
    },
    "type": "bank",
    "reference": "unique-ref-123"
  }'
```

#### Step 4: Query Transfer Status

```bash
curl --request GET --url 'https://developersandbox-api.flutterwave.com/transfers/{{TRANSFER_ID}}' \
  --header 'Authorization: Bearer ***'
```

### Phase 3: Required Headers (All Requests)

| Header | Purpose |
|--------|---------|
| `Authorization: Bearer ***` | OAuth token |
| `Content-Type: application/json` | JSON payload |
| `X-Trace-Id: unique-id` | Request tracing |
| `X-Idempotency-Key: unique-key` | Prevent duplicate transfers |

### Phase 4: Key Endpoints

| Step | Endpoint | Purpose |
|------|----------|---------|
| 1 | POST /token | Generate auth token |
| 2 | POST /banks/account-resolve | Validate account |
| 3 | POST /direct-transfers | Initiate transfer |
| 4 | GET /transfers/{id} | Query status |

### Phase 5: Error Codes

| Code | Type | Description |
|------|------|-------------|
| 201409 | REFERENCE_ALREADY_EXISTS | Duplicate transfer reference |

### Phase 6: Sandbox → Production

- [ ] Sandbox integration complete
- [ ] All error codes handled
- [ ] Idempotency keys generated per request
- [ ] Webhook endpoints configured
- [ ] Production credentials secured
| Proof of business | Account verification | Valid incorporation, director ID |

### Phase 7: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use python -m venv .venv for isolated env")
    elif system == "linux":
        print("Linux: Use sudo apt install python3-httpx or pip install httpx")
    elif system == "darwin":
        print("macOS: Use brew install python3 then pip install httpx")
    return system

# Error handling for Flutterwave API
import httpx
import asyncio

async def flutterwave_request(client, method, url, retries=3, **kwargs):
    for attempt in range(retries):
        try:
            response = await client.request(method, url, **kwargs)
            
            if response.status_code == 429:
                delay = 2 ** attempt
                await asyncio.sleep(delay)
                continue
            
            response.raise_for_status()
            data = response.json()
            
            if not data.get('status') or data.get('status') == 'error':
                raise Exception(data.get('message', 'Unknown API error'))
            
            return data
        except (httpx.TimeoutException, httpx.ConnectError) as e:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500 and attempt < retries - 1:
                await asyncio.sleep(2 ** attempt)
                continue
            raise
```

## Pitfalls

- **Token expiration** → Refresh before expiry; cache with TTL
- **Idempotency key reuse** → Causes REFERENCE_ALREADY_EXISTS; UUID per request
- **Account validation skip** → Failed transfers, wasted retries; always validate first
- **Currency mismatch** → Source/destination currency must match for NGN instant
- **Webhook verification** → Verify signatures; replay attacks possible

## Verification Checklist

- [ ] Auth token generated and cached
- [ ] Account validation succeeds
- [ ] Transfer initiates with 201/202
- [ ] Status query returns expected state
- [ ] Idempotency prevents duplicates
- [ ] Webhooks received and verified

## References

- `references/flutterwave-endpoints.md` — Complete endpoint reference
- `references/flutterwave-webhooks.md` — Webhook events and verification
- `references/flutterwave-currencies.md` — Supported currencies and corridors
- `references/flutterwave-patterns.md` — Code patterns and best practices

## Templates

- `templates/flutterwave-transfer-flow.py` — Complete transfer skeleton

## Scripts

- `scripts/flutterwave-test-transfers.py` — Sandbox transfer test