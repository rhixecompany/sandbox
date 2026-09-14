---
name: multi-task-model-tests
description: 28 tasks; identical self-profile query per model; provider-level auth-gated probes
template_type: model_testing
auth_gated: true
---

# Multi-task Model Testing Template

## Overview

Execute the same test tasks across all `:free` models to benchmark capabilities, latency, and quality. Keep catalog rows for audit history, but do not request a model when its provider is rate-limited.

## Test Query

`hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released`

## Provider Eligibility Gate

1. Run `hermes auth list` before the probe batch.
2. Normalize the output case-insensitively. Treat `rate-limited`, `429`, `too many requests`, `usage_limit_reached`, quota exhaustion, and throttling evidence as provider-level rate limits.
3. Skip every model for a rate-limited provider. Do not invoke `hermes chat`, retry, rank, or configure any of those models.
4. If a live request returns a rate-limit error, stop that provider's remaining models and mark those rows `provider_rate_limited`.

## Per-Model Test Structure

### Model Configuration

- **Provider**: `<provider_name>`
- **Model ID**: `<model_id>:free` or `<provider>:<model_slug>`
- **Auth Status**: Valid / Rate-limited / Auth-failed / Exhausted (from catalog)
- **Probe Eligibility**: Run only after the provider passes the auth preflight

### Test Tasks (same for all models)

#### Task 1: Reasoning

`Solve this logic puzzle: "If all Bloops are Razzies and no Razzie is a Gloob, can a Bloop ever be a Gloob? Explain your reasoning step by step."`

#### Task 2: Code Generation

`Write a Python function that implements a binary search algorithm on a sorted list. Include docstring and type hints.`

#### Task 3: Analysis

`Analyze the time complexity of quicksort and compare it to mergesort. Include best, average, and worst-case scenarios.`

#### Task 4: Creative Writing

`Write a 3-sentence story about a robot discovering emotions, using vivid imagery.`

#### Task 5: Reasoning Challenge

`If today is Monday, what day of the week will it be 100 days from now? Show your calculation.`

## Response Capture Format

For each model, capture:

- **Model ID**: `<provider>:<model>`
- **Latency (seconds)**: Time from request to first token
- **Quality Score**: 1-10 rating on relevance, correctness, completeness
- **Vision Support**: ✅/❌ (if applicable)
- **Reasoning Support**: ✅/❌ (if applicable)
- **Error Type**: none / rate_limit / auth_error / timeout / other
- **Provider Skip**: `provider_rate_limited` when no request was made for this model
- **Full Response**: The model's complete output for eligible requests only

## Ranking Criteria (Phase 4)

1. **Quality**: Overall correctness and completeness of responses
2. **Latency**: Time to first token and full response generation
3. **Reasoning Support**: Presence and quality of reasoning in responses
4. **Context Window**: Effective use of context length
5. **Max Output**: Utilization of maximum output tokens

### Score Formula

`score = (1 if reasoning == yes) + (1 if context_length >= 32000) + (1 if max_output >= 4096) + (1 if exit == 0) + (1 if recent_knowledge_cutoff)`

Max = 5. Tiebreak by lowest latency.

## Phase 4: Final Ranking & Configuration

1. Rank eligible, successful model rows by quality score.
2. Exclude `status=skipped`, `provider_rate_limited=true`, and any provider currently marked rate-limited.
3. Select the top eligible models for Hermes configuration.
4. Configure the primary and fallback chain.
5. Verify with `hermes config check` and `hermes fallback list`.

Rate-limited providers remain cataloged for audit history but never enter ranking or fallback configuration.
