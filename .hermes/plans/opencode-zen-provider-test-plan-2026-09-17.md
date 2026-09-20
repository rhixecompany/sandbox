---
goal: "OpenCode-Zen Provider Model Test + Hermes Fallback Config"
status: In progress
date_created: 2026-09-17
owner: Alexander E Iseghohi
tags: [opencode-zen, provider, fallback, config]
---

# OpenCode-Zen Provider Test Plan

## Goal

Test all opencode-zen models → log working ones → clear Hermes fallback → configure best 3.

## Phases

### Phase 1: READ CONFIG

- Read .env for API key + URL
- Read opencode.json for model list
- Extract all unique models from opencode-zen pool
- Gate: Have model list + credentials

### Phase 2: TEST MODELS

- For each model, send 3 prompts (identity, capabilities, reasoning)
- Log: model, prompt_type, status, response_time, valid, error
- Gate: All models tested

### Phase 3: ANALYZE RESULTS

- Rank models by valid responses / total prompts
- Select top 3 with highest success rate + fastest response
- Gate: Best 3 identified

### Phase 4: CONFIGURE FALLBACK

- Read current hermes config.yaml
- Clear fallback_providers
- Set best 3 as new fallback chain
- Gate: Config validated

### Phase 5: VERIFY

- Run hermes status to confirm fallback
- Run test prompt through Hermes to confirm working
- Gate: Fallback working

## Tasks

| ID  | Owner   | Description                                | Dependencies |
| --- | ------- | ------------------------------------------ | ------------ |
| T1  | default | Read .env + opencode.json → extract models | None         |
| T2  | default | Test all models with 3 prompts each        | T1           |
| T3  | default | Analyze results, rank, select best 3       | T2           |
| T4  | default | Clear + rewrite Hermes fallback_providers  | T3           |
| T5  | default | Verify with hermes status + test prompt    | T4           |

## Gates

- [ ] G1: Model list extracted from opencode-zen pool
- [ ] G2: All models tested with 3 prompts each
- [ ] G3: Best 3 models ranked and selected
- [ ] G4: Hermes fallback_providers cleared and set to best 3
- [ ] G5: Hermes status confirms fallback chain

## Deliverables

1. `results/opencode-zen-test-results.json`
2. `results/opencode-zen-best-3.md`
3. Updated `config.yaml` with new fallback_providers
