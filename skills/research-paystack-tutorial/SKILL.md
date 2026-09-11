---
name: research-paystack-tutorial
title: Paystack Research Digest
description: "Use when integrating Paystack: getting started, developer docs, charges, webhooks. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [paystack, payments, nigeria, api]
---

# Paystack Research Digest

## Overview

Wraps `research/paystack-tutorial/` (2 md files: getting started + developer documentation). Use when accepting payments in Nigeria/West Africa via Paystack.

## When to Use

- Setting up a Paystack account and first payment
- Building checkout with Paystack API (init → redirect → verify)
- Handling webhooks and transaction verification

## Workflow

### Phase 1: Digest

```bash
python scripts/research_paystack_tutorial.py
python scripts/research_paystack_tutorial.py --file "research/paystack-tutorial/getting-started-with-paystack.md"
```

### Phase 2: Apply

- Standard flow: initialize transaction (amount, email) → redirect to authorization URL → verify with reference
- Secret/public key pair; keep secret server-side
- Developer docs file holds endpoint details and webhook guidance

### Phase 3: Verify

- Test charge with Paystack test keys + test card from developer docs
- Verify transaction status via the verify endpoint before fulfilling orders

## Pitfalls

- Amounts are in kobo (minor units) — multiply naira by 100
- Only trust server-side verification, never client-side callbacks

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Charge flow matches developer-docs file

## References

- `research/paystack-tutorial/getting-started-with-paystack.md`
- `research/paystack-tutorial/paystack-developer-documentation.md`
- Script: `scripts/research_paystack_tutorial.py` | Test: `scripts/tests/test_research_paystack_tutorial.py`
