# Busha Quick Start Guide

> **Source:** https://docs.busha.io/guides/getting-started/quick-start
> **Retrieved:** 2026-06-01T00:00:00

---

## Overview

This guide walks through setting up a Busha Business Account, completing verification, enabling 2FA, and generating API keys.

## Step 1: Create Business Account

Option A: From existing personal account → Avatar dropdown → "Open a business account"
Option B: New registration at https://dash.busha.io/business/signup

## Step 2: Complete KYB Verification

Required for live API access:
- Business registration documents
- Ownership structure
- Company information

Status: "Pending Verification" → Email notification on approval

## Step 3: Enable 2FA

1. Go to Personal account → Settings → Security
2. Click Two Factor Authentication
3. Link authenticator app (Google Authenticator)
4. Confirm activation

## Step 4: Generate API Keys

1. Business dashboard → Settings → Developer tools → API Tokens
2. Click "Add New Token"
3. Name token, assign permissions
4. Enter 6-digit 2FA code
5. Copy key immediately (shown only once)

## Key Types

| Key Type | Use Case | Security |
|----------|----------|----------|
| Public Keys | Front-end apps, SDKs | Safe for client-side |
| Secret Keys | Server-side only | Must be confidential |

## Integration Flow

1. Generate auth token via identity endpoint
2. Validate customer account
3. Initiate transfer
4. Query transfer status

## Required Headers

- Authorization: Bearer {{ACCESS_TOKEN}}
- Content-Type: application/json
- X-Trace-Id: unique trace ID
- X-Idempotency-Key: unique idempotency key

---

*Extracted by web-research-pipeline v1.0.0*