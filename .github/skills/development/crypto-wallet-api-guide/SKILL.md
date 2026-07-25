---
name: crypto-wallet-api-guide
title: "Crypto Wallet APIs Guide for Developers & Businesses"
description: "Use when evaluating wallet API providers — covers market context, API types (transactional, balance, management, custodial, non-custodial), MPC architecture, and major providers (Fireblocks, Portal, Cobo, Crypto APIs, BitGo)."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [wallet-api, mpc, custodial, non-custodial, fireblocks, portal, cobo, cryptoapis, bitgo, evaluation]
---
# Crypto Wallet APIs Guide for Developers & Businesses

## Purpose

Comprehensive guide for choosing and implementing wallet APIs. Covers market data, API categories, MPC technology, and provider comparison.

## When to Use

- Selecting wallet infrastructure for a product
- Comparing custodial vs non-custodial tradeoffs
- Understanding MPC-based key management
- Evaluating Fireblocks, Portal, Cobo, Crypto APIs, BitGo

## When NOT to Use

- Building custom key management (not using APIs)
- Single-chain embedded wallets
- Academic research only

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug provider integration issues |
| `requesting-code-review` | Security review of wallet integration |
| `writing-plans` | Plan migration between providers |

## Workflow

### Phase 1: Market Context (2026)

- Non-custodial wallet market: $6.43B (2025) → projected $45B by 2035
- 820 million active wallets globally
- 43.8% of $2.2B stolen (2024) due to private key compromises
- **Key insight:** Security is unforgiving — build vs buy decision critical

### Phase 2: Why Wallet APIs Matter

1. **Security is unforgiving** — Custom key management = high risk
2. **Scalability needs infrastructure** — APIs handle 100 → 100,000+ users
3. **Multi-chain is table stakes** — Ethereum, Solana, Bitcoin, L2s, EVM chains

### Phase 3: Wallet API Types

| API Type | Function | Use Case |
|----------|----------|----------|
| Transactional | Send/receive crypto | Payments, exchanges, bots |
| Balance & Info | Read balances, history | Portfolio trackers, tax tools |
| Wallet Management | Create wallets, addresses | Onboarding, treasury |
| Custodial | Provider holds keys | Beginner apps, regulated |
| Non-Custodial | User holds keys | Self-custody, DeFi, MPC |

### Phase 4: MPC (Multi-Party Computation)

**How it works:** Private key split into multiple shares held by separate parties. No single party ever has complete key.

**2026 MPC Stack:**
- Distributed Key Generation (DKG)
- Threshold Signature Scheme (TSS)
- Policy-Based Signing
- Transaction Simulation

**Major Providers:**
- Fireblocks (institutional)
- Portal (developer-focused)
- Cobo (WaaS)
- Crypto APIs (WaaS)
- BitGo (custody + API)

### Phase 5: Provider Comparison

| Provider | Model | Chains | Best For |
|----------|-------|--------|----------|
| Fireblocks | MPC Custodial | 50+ | Institutions, high volume |
| Portal | MPC Non-Custodial | 20+ | DeFi apps, user-owned keys |
| Cobo | Custodial WaaS | 80+ | Exchanges, custodial products |
| Crypto APIs | Custodial WaaS | 30+ | Wallet infrastructure |
| BitGo | Custodial + MPC | 100+ | Enterprise custody |

### Phase 6: Integration Checklist

- [ ] Provider selected for use case
- [ ] KYB/KYC completed
- [ ] Sandbox integration tested
- [ ] Webhook endpoints secured
- [ ] Disaster recovery plan (key recovery)
- [ ] Compliance (travel rule, sanctions)
- [ ] Fee model understood

## Pitfalls

- **Custodial lock-in** → Hard to migrate keys later
- **MPC ≠ magic** → Still need policy engine, recovery
- **Chain coverage gaps** → Verify target chains supported
- **Webhook reliability** → Implement idempotency, retry
- **Fee opacity** → Some providers markup network fees

## Verification Checklist

- [ ] Provider matches custody model requirement
- [ ] All target chains supported
- [ ] Sandbox integration complete
- [ ] Security audit passed
- [ ] Compliance requirements met

## References

- `references/provider-comparison.md` — Detailed feature matrix
- `references/mpc-deep-dive.md` — Technical MPC implementation
- `references/migration-guide.md` — Moving between providers
- `references/crypto-wallet-evaluation.md` — Provider evaluation checklist

## Templates

- `templates/wallet-provider-evaluation.md` — Provider selection worksheet

## Scripts

- `scripts/test-wallet-api.py` — Quick sandbox test script