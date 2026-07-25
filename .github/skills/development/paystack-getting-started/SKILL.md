---
name: paystack-getting-started
title: "Getting Started with Paystack"
description: "Use when onboarding to Paystack for accepting payments — covers account creation, KYB compliance, integration options (no-code, low-code, pro-code), and features."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [paystack, payments, africa, onboarding, kyb, integration, invoices, recurring]
---
# Getting Started with Paystack

## Purpose

Complete onboarding guide for Paystack — from account creation to accepting payments across Africa.

## When to Use

- Setting up Paystack for business
- Choosing integration approach
- Understanding compliance requirements
- Evaluating Paystack features

## When NOT to Use

- Developer API reference (separate docs)
- Technical webhook handling
- Advanced customization

## Skills Required

| Skill | Purpose |
|-------|---------|
| `executing-plans` | Follow sequential onboarding steps |
| `systematic-debugging` | Debug integration issues |

## Workflow

### Phase 1: Three Steps to Get Started

**Step 1: Create Account** (Free, few minutes)
- Business name
- Full name
- Email
- Phone number
- Business type

**Step 2: Submit Compliance Documents**
- Requirements vary by location and business type
- Review within 48 hours
- Once approved → start accepting payments

**Step 3: Integrate with Paystack**
- No-code: Payment links, invoices
- Low-code: Pre-built checkout
- Pro-code: Full API integration

### Phase 2: Features

- Automated recurring payments
- Customized invoices
- Digital receipts
- Multi-currency support
- Real-time reporting

### Phase 3: Testing & Go-Live

**Sandbox Testing:**
```bash
# Test with sandbox keys
TEST_SECRET_KEY=sk_test_xxx
TEST_PUBLIC_KEY=pk_test_xxx
```

**Production Checklist:**
- [ ] Account approved
- [ ] Integration tested in sandbox
- [ ] Production keys configured
- [ ] First live transaction successful

## Pitfalls

- KYB delays — Prepare documents in advance
- Currency limitations — Verify supported currencies for target markets
- Webhook failures — Implement retry logic and idempotency
- Test vs live keys — Don't mix environments

## Verification Checklist

- [ ] Account approved
- [ ] Integration tested in sandbox
- [ ] Production keys configured
- [ ] First live transaction successful

## References

- `references/paystack-dashboard-guide.md` — Dashboard navigation
- `references/paystack-compliance.md` — Document requirements by country
- `references/paystack-webhooks.md` — Event types and handling
- `references/paystack-error-handling.md` — Error codes and retry strategy

## Templates

- `templates/paystack-integration-checklist.md` — Production readiness checklist

## Scripts

- `scripts/paystack-test-transaction.py` — Sandbox test script