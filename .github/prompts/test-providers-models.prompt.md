---
name: test-providers-models
title: "Test Providers & Models"
description: 'Inventory providers, discover models, benchmark accessible free models, '
  'compare providers, analyze rate limits/fallbacks, and create/update automation scripts.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- providers
- models
- benchmark
- testing
- fallback
trigger: /test-providers-models
formatter: default
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - user-communication-preferences
    - verification-before-completion
toolsets:
- file
- terminal
scripts: []
skills: []
plan: ''
---

# Test Providers & Models

## Context

- **Hermes config/profile:** use live `hermes auth list` + provider config as source of truth.
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Rules

1. Execute phases in order; do not reorder.
2. Treat rate-limit findings as volatile; re-check before depending on them.
3. If a benchmark path or script is missing, report the exact missing path instead of fabricating results.

## Phases

Full phase instructions live in `templates/test-providers-models/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 0 | Auth & Provider Inventory | all authorized providers captured and documented |
| 1 | Model Catalog Discovery | catalog entries documented per provider |
| 2 | Free Model Extraction | free-tier model table complete |
| 3 | Provider-by-Provider Benchmarking | benchmark outputs saved per provider/model |
| 4 | Cross-Provider Comparison & Report | comparison report generated and reviewed |
| 5 | Rate Limit & Fallback Chain Analysis | fallback recommendation completed |
| 6 | Script Creation & Automation | scripts runnable and preserved |

## Verification Checklist

- [ ] Phase 0 completed and verified
- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Phase 5 completed and verified
- [ ] Phase 6 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
