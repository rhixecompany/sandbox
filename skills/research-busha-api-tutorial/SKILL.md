---
name: research-busha-api-tutorial
title: Busha Business API Research Digest
description: "Use when working with Busha Business API: request-quote-execute, KYB, 2FA, payouts. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [busha, api, crypto, nigeria]
---

# Busha Business API Research Digest

## Overview

Wraps `research/busha-api-tutorial/` (2 md files: primer + quick start). Use when integrating Busha Business API for crypto buy/sell/payout in Nigeria.

## When to Use

- Requesting quotes and executing crypto trades via Busha API
- Onboarding: business account, KYB verification, 2FA, API key generation
- Building payout/transfer flows

## Workflow

### Phase 1: Digest

```bash
python scripts/research_busha_api_tutorial.py
python scripts/research_busha_api_tutorial.py --file "research/busha-api-tutorial/busha-business-api-a-primer.md"
```

### Phase 2: Apply

- Core pattern: Request → Quote → Execute (request quote first, execute within validity window)
- Account setup order per quick start: create business account → KYB → enable 2FA → generate API keys
- Key capabilities: quotes, orders, payouts — confirm exact endpoint names from the primer

### Phase 3: Verify

- Digest both files; map each needed operation to a documented endpoint
- Test on sandbox/live keys with minimal amounts before scaling

## Pitfalls

- Quote validity expires — execute promptly, never cache quotes
- KYB must complete before live trading; 2FA required for key generation

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Integration steps trace to quick-start steps 1-4

## References

- `research/busha-api-tutorial/busha-business-api-a-primer.md`
- `research/busha-api-tutorial/busha-quick-start-guide.md`
- Script: `scripts/research_busha_api_tutorial.py` | Test: `scripts/tests/test_research_busha_api_tutorial.py`
