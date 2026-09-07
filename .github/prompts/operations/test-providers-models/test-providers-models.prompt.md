---
name: test-providers-models
title: Test Providers Models
description: "Test all Hermes auth providers, rank models by capabilities, and configure Hermes with the top 5"
version: 2.1.0
author: Hermes Agent
license: MIT
tags: [qa, testing, providers, models, benchmarking]
metadata:
  hermes:
    tags: [qa, testing, providers, models, benchmarking]
toolsets:
  - hermes-cli
  - web
category: operations
trigger: test-providers-models
---

# Test Providers Models

## Goal
Execute all available Hermes auth providers to test each model's capabilities, rank the top 5, and configure Hermes with the best model and fallback chain.

## Context
This prompt tests every auth provider configured in Hermes by running `hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list`, then executing each `:free` model via `hermes chat --provider --model -q --oneshot` in the background, ranking results, and configuring Hermes.

## Workflow

### Phase 1: Discovery
1. Run `hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list`
2. Extract all auth provider URLs and documentation URLs
3. Run `/web-research-pipeline` for each provider to find best practices
4. Web-extract all documentation pages as markdown

### Phase 2: Catalog
1. Create `test-providers-models-free-suffix-catalog.md` with all `:free` models
2. Include: provider name, model name, vision, reasoning, context window, flags
3. Use hermes insights to populate capabilities

### Phase 3: Testing
1. Create multi-tasks for testing each model
2. Execute `hermes chat --provider "provider name" --model "model name" -q "tasks" --oneshot` in background without timeout
3. Each model gets the same test tasks
4. Capture responses, latency, quality scores

### Phase 4: Ranking & Configuration
1. Rank all models by quality, speed, capabilities
2. Select top 5 models
3. Configure Hermes model via `hermes config set model.default` with top-ranked model
4. Configure fallback with remaining 4 via `hermes fallback clear` then `hermes fallback add`
5. Run `/prompts-judge` on test-providers-models.prompt.md to verify score ≥ 98

### Phase 5: Verification
1. Verify all sessions from the test run
2. Confirm top 5 ranking is accurate
3. Verify Hermes config is updated correctly
4. Verify fallback chain is working

## Verification
- [ ] All auth providers discovered and documented
- [ ] All `:free` models cataloged with capabilities
- [ ] All models tested via `hermes chat --oneshot`
- [ ] Top 5 ranked and configured as default
- [ ] Remaining 4 configured as fallback chain
- [ ] `/prompts-judge` returns score ≥ 98
- [ ] All new sessions audited and ranked
