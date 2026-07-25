---
name: paystack-dev-docs
title: "Paystack Developer Documentation"
description: "Use when integrating Paystack API — covers quick start (initialize transaction, verify payment), transfer recipients, transfers, identity verification, developer tools (libraries, no-code), webhooks, and demo projects."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [paystack, api, payments, transfers, identity, webhooks, sdk, developer, africa]
---
# Paystack Developer Documentation

## Purpose

Complete developer reference for Paystack API integration — payments, transfers, identity verification, and webhooks.

## When to Use

- Building Paystack payment integration
- Implementing transfers/payouts
- Adding identity verification
- Setting up webhooks
- Choosing SDK/no-code option

## When NOT to Use

- Business onboarding (use getting-started)
- Non-technical payment link creation
- Compliance document requirements

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug API errors, webhook failures, signature verification |
| `requesting-code-review` | Security review for payment handling |

## Workflow

### Phase 1: Quick Start — Accept Payments

**1. Initialize Transaction:**
```bash
curl https://api.paystack.co/transaction/initialize \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"email": "customer@email.com", "amount": 10000}'
```
Returns authorization URL for customer redirect.

**2. Verify Payment:**
```bash
curl https://api.paystack.co/transaction/verify/{reference} \
  -H "Authorization: Bearer ***"
```
Always verify on your server before fulfilling order.

### Phase 2: Send Money (Transfers)

**1. Create Transfer Recipient:**
```bash
curl https://api.paystack.co/transferrecipient \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"type": "nuban", "name": "John Doe", "account_number": "0123456789", "bank_code": "058", "currency": "NGN"}'
```

**2. Initiate Transfer:**
```bash
curl https://api.paystack.co/transfer \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"source": "balance", "amount": 10000, "recipient": "RCP_xxxxx", "reason": "Salary"}'
```

### Phase 3: Identity Verification

- **Verify Phone:** Confirm phone ownership
- **Verify Bank Account:** Resolve account number + bank code
- **Verify Card:** Check card validity

### Phase 4: Developer Tools

| Tool | Languages | Use Case |
|------|-----------|----------|
| **Libraries** | PHP, Python, Node.js, Ruby, Java, Go, .NET | Server-side integration |
| **No-code** | Payment links, invoices, plugins | Quick deployment |

### Phase 5: API Authentication

All calls require secret key:
```
Authorization: Bearer sk_live_xxxxxxxxxxxx
```

### Phase 6: Key Endpoints

| Endpoint | Purpose |
|----------|---------|
| POST /transaction/initialize | Start payment |
| GET /transaction/verify/{reference} | Confirm payment |
| POST /transferrecipient | Create payout recipient |
| POST /transfer | Initiate transfer |
| GET /transfer/{id} | Check transfer status |
| GET /bank | List banks |
| GET /bank/resolve | Resolve account number |
| POST /verification/phone | Verify phone |
| POST /verification/bank_account | Verify bank account |

### Phase 7: Webhook Events

- `charge.success`
- `transfer.success`
- `transfer.failed`
- `invoice.create`
- `subscription.create`

**Security:** Verify webhook signature using Paystack-Signature header.

### Phase 8: Error Codes

Common: insufficient_funds, invalid_account, rate_limit, signature_verification_failed

### Phase 9: Demo Projects

- **Gift Store (Vue):** E-commerce with Paystack checkout
- **Movie Ticket (Vue):** Event ticketing with payments

### Phase 10: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use PowerShell or WSL for curl commands")
    elif system == "linux":
        print("Linux: curl installed by default")
    elif system == "darwin":
        print("macOS: Use Terminal or iTerm2")
    return system
```

**Error handling:**
```python
import httpx
import asyncio

PAYSTACK_ERRORS = {
    "insufficient_funds": "Top up balance or check account",
    "invalid_account": "Check bank code + account number",
    "rate_limit": "Implement exponential backoff",
    "signature_verification_failed": "Check webhook secret and payload format",
    "already_used": "Idempotency — use unique reference per request",
}

async def paystack_with_retry(client, method, url, retries=3, **kwargs):
    for attempt in range(retries):
        try:
            response = await client.request(method, url, **kwargs)
            if response.status_code == 429:
                await asyncio.sleep(2 ** attempt)
                continue
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500 and attempt < retries - 1:
                await asyncio.sleep(2 ** attempt)
                continue
            error_data = e.response.json()
            error_message = error_data.get("message", "Unknown error")
            raise Exception(f"Paystack error: {error_message}")
```

## Pitfalls

- **Never trust client-side verification** — Always verify on server
- **Webhook replay attacks** — Implement idempotency
- **Test/live key mixing** — Separate environments strictly
- **Amount in kobo/cents** — Multiply by 100 for API

## Verification Checklist

- [ ] Server-side verification implemented
- [ ] Webhook signature verified
- [ ] Idempotency keys used for transfers
- [ ] Test transactions pass in sandbox
- [ ] Error handling for all failure codes
- [ ] PCI compliance maintained

## References

- `references/paystack-api-reference.md` — Full endpoint catalog
- `references/paystack-webhook-guide.md` — Webhook security and handling
- `references/paystack-libraries.md` — SDK usage examples
- `references/paystack-patterns.md` — Authentication, error handling

## Templates

- `templates/paystack-api-example.py` — Full payment flow example

## Scripts

- `scripts/paystack-test-flow.py` — Complete sandbox test