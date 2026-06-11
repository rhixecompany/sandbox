# Flutterwave Transfers API - Introduction

> **Source:** https://developer.flutterwave.com/docs/introduction-3
> **Retrieved:** 2026-06-01T00:00:00

---

## Overview

Flutterwave Transfers enables global fund transfers across bank accounts, mobile numbers, wallets, and cash pickups.

## Prerequisites

- API credentials from https://onboarding.flutterwave.com/signup
- This guide covers one-time transfers (orchestrator flow)

## Transfer Flow (4 Steps)

### Step 1: Generate Authorization Token

```bash
curl --location 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'client_id={{YOUR_CLIENT_ID}}' --data-urlencode 'client_secret={{YOUR_CLIENT_SECRET}}' --data-urlencode 'grant_type=client_credentials'
```

### Step 2: Validate Customer Account

```bash
curl --request POST --url https://developersandbox-api.flutterwave.com/banks/account-resolve --header 'content-type: application/json' --data '{
  "account": {"code": "044", "number": "0690000040"},
  "currency": "NGN"
}'
```

### Step 3: Initiate Transfer

```bash
curl --request POST --url 'https://developersandbox-api.flutterwave.com/direct-transfers' --header 'Authorization: Bearer {{ACCESS_TOKEN}}' --header 'Content-Type: application/json' --header 'X-Trace-Id: {{TRACE_ID}}' --header 'X-Idempotency-Key: {{IDEMPOTENCY_KEY}}' --data '{
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

### Step 4: Query Transfer Status

```bash
curl --request GET --url 'https://developersandbox-api.flutterwave.com/transfers/{{TRANSFER_ID}}' --header 'Authorization: Bearer {{ACCESS_TOKEN}}'
```

## Key Endpoints

| Step | Endpoint | Purpose |
|------|----------|---------|
| 1 | POST /token | Generate auth token |
| 2 | POST /banks/account-resolve | Validate bank account |
| 3 | POST /direct-transfers | Initiate transfer |
| 4 | GET /transfers/{id} | Query status |

## Required Headers

- Authorization: Bearer {{ACCESS_TOKEN}}
- Content-Type: application/json
- X-Trace-Id: unique trace ID
- X-Idempotency-Key: unique idempotency key

## Error Codes

| Code | Type | Description |
|------|------|-------------|
| 201409 | REFERENCE_ALREADY_EXISTS | Duplicate transfer reference |

---

*Extracted by web-research-pipeline v1.0.0*