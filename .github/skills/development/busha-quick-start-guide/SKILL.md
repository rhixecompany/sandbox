---
name: busha-quick-start-guide
title: "Busha Quick Start Guide"
description: "Use when setting up Busha Business API — covers account creation, KYB verification, 2FA, API key generation, and integration flow."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [busha, quickstart, africa, stablecoins, business, api, kyb]
---
# Busha Quick Start Guide

## Purpose

Step-by-step guide to onboard and integrate with Busha Business API for stablecoin and digital asset operations in African and global markets.

## When to Use

- Onboarding a new business to Busha
- Setting up API integration for payments/transfers
- Learning Busha's request-quote-execute pattern

## When NOT to Use

- Personal/retail crypto trading (use Binance, Coinbase)
- Non-African markets without stablecoin needs
- Instant integration without KYB completion

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug authentication, webhook, idempotency issues |
| `test-driven-development` | Test integration in sandbox before live |

## Workflow

### Phase 1: Account Setup

1. **Create Business Account**
   - Option A: Existing personal → Avatar dropdown → "Open a business account"
   - Option B: New registration at `https://dash.busha.io/business/signup`

2. **Complete KYB Verification** (48-72 hours)
   - Business registration documents
   - Ownership structure
   - Company information
   - Status: "Pending Verification" → Email on approval

3. **Enable 2FA**
   - Personal account → Settings → Security
   - Two Factor Authentication → Google Authenticator
   - Confirm activation

4. **Generate API Keys**
   - Business dashboard → Settings → Developer tools → API Tokens
   - "Add New Token" → Name, assign permissions
   - Enter 2FA code → **Copy immediately (shown once)**

**Key Types**
| Type | Use Case | Security |
|------|----------|----------|
| Public | Front-end apps, SDKs | Client-side safe |
| Secret | Server-side only | Must be confidential |

### Phase 2: Integration Flow (Request-Quote-Execute)

**Step 1: Generate Auth Token**
```bash
curl --location 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'client_id={{CLIENT_ID}}' \
  --data-urlencode 'client_secret={{CLIENT_SECRET}}' \
  --data-urlencode 'grant_type=client_credentials'
```

**Step 2: Validate Customer Account**
```bash
curl --request POST --url https://developersandbox-api.flutterwave.com/banks/account-resolve \
  --header 'content-type: application/json' \
  --data '{"account": {"code": "044", "number": "0690000040"}, "currency": "NGN"}'
```

**Step 3: Initiate Transfer**
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

**Step 4: Query Status**
```bash
curl --request GET --url 'https://developersandbox-api.flutterwave.com/transfers/{{TRANSFER_ID}}' \
  --header 'Authorization: Bearer ***'
```

### Phase 3: Required Headers (All Requests)

- `Authorization: Bearer ***`
- `Content-Type: application/json`
- `X-Trace-Id: unique trace ID`
- `X-Idempotency-Key: unique idempotency key`

### Phase 4: Error Codes

| Code | Type | Description |
|------|------|-------------|
| 201409 | REFERENCE_ALREADY_EXISTS | Duplicate transfer reference |

### Phase 5: Go-Live Checklist

- [ ] KYB approved
- [ ] Sandbox integration tested
- [ ] Idempotency keys generated per request
- [ ] Webhook endpoints configured
- [ ] Production API keys secured
- [ ] Compliance review passed

## Pitfalls

- **Idempotency key reuse** → Causes REFERENCE_ALREADY_EXISTS; UUID per request
- **2FA on API key creation** → Code shown only once; save immediately
- **KYB required** — Cannot go live without approval
- **Webhook reliability** — Implement idempotency, retry logic

## Verification Checklist

- [ ] Auth token generated and cached
- [ ] Account validation succeeds
- [ ] Transfer initiates with 201/202
- [ ] Status query returns expected state
- [ ] Idempotency prevents duplicates
- [ ] Webhooks received and verified

## References

- `references/busha-endpoints.md` — Complete endpoint reference
- `references/busha-webhooks.md` — Webhook events and verification
- `references/busha-currencies.md` — Supported currencies and corridors