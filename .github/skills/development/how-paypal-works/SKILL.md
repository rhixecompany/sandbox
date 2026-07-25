---
name: how-paypal-works
title: "How PayPal Works (PayPal US)"
description: "Use when understanding PayPal's payment options, rewards, security, and business solutions from the official PayPal US site — covers setup, payment methods, cashback, and PayPal Open."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [paypal, payments, digital-wallet, cashback, business, security, rewards]
---
# How PayPal Works (PayPal US)

## Purpose

Official PayPal US overview of how PayPal works for consumers and businesses — setup, payment methods, rewards, security, and business solutions.

## When to Use

- Integrating PayPal as payment method
- Building checkout flows with PayPal
- Understanding PayPal rewards for user incentives
- Evaluating PayPal Open for business

## When NOT to Use

- PayPal developer API integration (different docs)
- Technical implementation
- Non-US markets (features vary)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug payment failures, webhook issues |
| `requesting-code-review` | Security review for payment integration |

## Workflow

### Phase 1: Setup

1. Create account (email + phone + password)
2. Set up PayPal Debit Card (5% cash back category)
3. Link bank account for PayPal Balance
4. Download PayPal app

### Phase 2: Payment Options

- Debit/credit cards (Visa, Mastercard, Discover, Amex)
- Bank accounts
- PayPal Balance
- PayPal Debit Card
- PayPal Cashback Mastercard (3% on PayPal, 1.5% other)
- Pay Later installment options

### Phase 3: Rewards

- **5% cash back** (up to $1,000/month) with PayPal Debit Card
- Exclusive brand offers via app
- **3% cash back** with PayPal Cashback Mastercard on PayPal purchases
- **1.5% cash back** on all other purchases

### Phase 4: Security

- Encrypted transactions
- Early fraud detection
- Purchase Protection for eligible items
- Real-time app alerts

### Phase 5: Business Solutions (PayPal Open)

- Accept Payments
- Risk & Operations management
- Financial Services

## Pitfalls

- Category restrictions on 5% cash back
- Currency conversion fees for international
- Merchant fees for receiving payments
- Account limitations can freeze funds

## Verification Checklist

- [ ] Account created and verified
- [ ] Payment methods linked
- [ ] Rewards understood
- [ ] Security features enabled
- [ ] Business account set up (if applicable)

## References

- `references/paypal-consumer-fees.md` — Fee schedule
- `references/paypal-business-features.md` — PayPal Open details
- `references/paypal-security-features.md` — Protection policies
- `references/paypal-integration-patterns.md` — REST API patterns

## Templates

- `templates/paypal-integration-checklist.md` — Production readiness checklist

## Scripts

- `scripts/paypal-test-webhook.py` — Webhook verification test