---
name: research-uk-earning-sites
title: UK Earning Sites Research Digest
description: "Use when researching UK money-making sites: comparison, 2026 market findings. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [uk, research, earning-sites, comparison]
---

# UK Earning Sites Research Digest

## Overview

Wraps the root-level research files: `research/uk-earning-sites-comparison.md` and `research/uk-money-earning-sites-research-2026.md`. Use when evaluating UK earning opportunities (surveys, cashback, microtasks).

## When to Use

- Comparing UK earning sites and their payout models
- Citing the 2026 research findings in content or planning
- Deciding which categories (surveys, cashback, microtasks) fit a goal

## Workflow

### Phase 1: Digest

```bash
python scripts/research_uk_earning_sites.py
python scripts/research_uk_earning_sites.py --file "research/uk-earning-sites-comparison.md"
```

### Phase 2: Apply

- Read the comparison table for payout thresholds/rates per site category
- Use the 2026 research file for market context and trends
- Keep data claims tied to the file date; refresh research before publishing stale numbers

### Phase 3: Verify

- Cross-check any site claim against the source file section before reuse

## Pitfalls

- Earning-site landscape changes fast — always check the research date before citing

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Claims trace to a section in one of the two md files

## References

- `research/uk-earning-sites-comparison.md`
- `research/uk-money-earning-sites-research-2026.md`
- Script: `scripts/research_uk_earning_sites.py` | Test: `scripts/tests/test_research_uk_earning_sites.py`
