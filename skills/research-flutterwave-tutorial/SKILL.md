---
name: research-flutterwave-tutorial
title: Flutterwave Transfers API Research Digest
description: "Use when sending money via Flutterwave Transfers API: 4-step flow, endpoints, headers. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [flutterwave, payments, transfers, africa]
---

# Flutterwave Transfers API Research Digest

## Overview

Wraps `research/flutterwave-tutorial/flutterwave-transfers-api-introduction.md`. Use when integrating Flutterwave disbursements (transfers to bank/mobile money).

## When to Use

- Implementing payout/transfer flows via Flutterwave
- Checking required headers, endpoints, and the transfer flow order
- Troubleshooting transfer status checks

## Workflow

### Phase 1: Digest

```bash
python scripts/research_flutterwave_tutorial.py
python scripts/research_flutterwave_tutorial.py --file "research/flutterwave-tutorial/flutterwave-transfers-api-introduction.md"
```

### Phase 2: Apply

- Transfer flow (4 steps): init → validate recipient → execute transfer → confirm status
- Required headers: authorization (Bearer secret key), content-type; verify exact names in the file
- Key endpoints: transfers create/status — pull exact paths from the research doc

### Phase 3: Verify

- Run transfer to a test recipient with minimal amount
- Poll status endpoint until terminal state; handle pending/failed distinctly

## Pitfalls

- Some recipients/currencies require pre-registration — validate before execute
- Webhook or polling? Research doc notes the recommended confirmation path

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Endpoint names/headers match the research doc before coding

## References

- `research/flutterwave-tutorial/flutterwave-transfers-api-introduction.md`
- Script: `scripts/research_flutterwave_tutorial.py` | Test: `scripts/tests/test_research_flutterwave_tutorial.py`
