---
name: research-paypal-tutorial
title: PayPal Research Digest
description: "Use when understanding PayPal: setup, payment options, rewards, how it works. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [paypal, payments, research]
---

# PayPal Research Digest

## Overview

Wraps `research/paypal-tutorial/` (2 md files: how PayPal works US, getting started). Use when explaining PayPal mechanics or building merchant flows.

## When to Use

- Answering how PayPal works (setup, payment options, rewards)
- Guiding a user through sign-up and first payment
- Planning merchant checkout integration basics

## Workflow

### Phase 1: Digest

```bash
python scripts/research_paypal_tutorial.py
python scripts/research_paypal_tutorial.py --file "research/paypal-tutorial/how-paypal-works-paypal-us.md"
```

### Phase 2: Apply

- Setup: personal vs business account; link bank/card
- Payment options covered: checkout, Pay Later, rewards (per file)
- Getting-started file covers sign-up order and first transaction

### Phase 3: Verify

- Cross-check any payment-method claims against both files before publishing content

## Pitfalls

- PayPal feature availability differs by country — keep claims US-scoped per source

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Explanations trace to source files

## References

- `research/paypal-tutorial/how-paypal-works-paypal-us.md`
- `research/paypal-tutorial/how-to-get-started-with-paypal.md`
- Script: `scripts/research_paypal_tutorial.py` | Test: `scripts/tests/test_research_paypal_tutorial.py`
