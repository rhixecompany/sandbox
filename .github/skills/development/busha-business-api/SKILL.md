---
name: busha-business-api
title: "Busha Business API: A Primer"
description: "Use when understanding Busha Business API capabilities for African/global stablecoin and digital asset infrastructure — covers buy/sell, send/receive, convert, customer management, and request-quote-execute pattern."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [busha, api, business, africa, stablecoins, digital-assets, fintech, payments]
---
# Busha Business API Primer

## Purpose

Understand Busha Business API for programmatic access to stablecoins and digital assets infrastructure — targeted at African and global businesses.

## When to Use

- Evaluating Busha for business payments
- Building stablecoin integration
- Understanding request-quote-execute pattern
- Comparing African fintech APIs

## When NOT to Use

- Personal/consumer trading
- Technical API integration (use dev docs)
- Non-African markets without stablecoin needs

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug quote expiration, settlement failures |
| `requesting-code-review` | Security review for financial transactions |

## Workflow

### Phase 1: Core Capabilities

Busha Business API provides programmatic access to:

1. **Buy and Sell** — Convert between local currencies (NGN, KES) and digital assets
2. **Send and Receive** — Move stablecoins and digital assets globally
3. **Convert** — Swap between stablecoins and digital assets
4. **Customer & Wallet Management** — Onboard merchants, retrieve addresses, check balances

### Phase 2: Request-Quote-Execute Pattern

**Phase 1: Request and Quote**
- Request quote (e.g., buy 1 BTC with NGN)
- Busha returns guaranteed rate valid for several minutes

**Phase 2: Acceptance and Execution**
- User accepts quote
- Busha validates and reserves assets

**Phase 3: Settlement and Confirmation**
- Assets allocated to user wallet
- Blockchain transaction recorded
- Webhook notification sent

### Phase 3: Use Cases

| Use Case | Description |
|----------|-------------|
| Crypto Exchanges | Backend liquidity and wallet operations |
| Remittance Services | Stablecoin settlement layer |
| Payroll Platforms | Pay contractors in digital assets |
| Savings & Investment Apps | Execute crypto trades |
| Payment Processors | Accept stablecoin payments |

### Phase 4: Technical Details

- **Protocol:** REST with JSON
- **Authentication:** API keys in headers
- **HTTPS-only**
- **Idempotency keys** for retries
- **Webhook-driven** updates
- **Rate limits:** Generous defaults

### Phase 5: Pricing

- Flat, transaction-based pricing
- No setup fees or monthly minimums
- Pay only for transactions processed

### Phase 6: Onboarding Path

1. Create business account
2. Complete KYB (48-72 hours)
3. Access sandbox environment
4. Build integration
5. Test in sandbox
6. Go live with production keys

**Typical integration time:** 1-2 weeks

## Pitfalls

- **Quote expiration** — Several minutes only; handle gracefully
- **KYB required** — Cannot go live without approval
- **Webhook reliability** — Implement idempotency
- **Currency pairs** — Verify supported pairs for target markets

## Verification Checklist

- [ ] Business account created
- [ ] KYB documents prepared
- [ ] Sandbox access granted
- [ ] Integration pattern understood
- [ ] Webhook endpoints designed

## References

- `references/busha-endpoints.md` — API endpoint reference
- `references/busha-webhooks.md` — Webhook events and verification
- `references/busha-currencies.md` — Supported currencies and pairs