---
name: multi-task-model-tests-updated
description: 28 tasks; identical query per model; auth-gated — rebuilt 2026-09-07
template_type: model_testing
auth_gated: true
---

# Multi-task Model Testing Template

## Overview
Execute the same test tasks across all `:free` models to benchmark capabilities, latency, and quality.

## Test Query
`tasks` - A comprehensive prompt covering reasoning, code, and analysis capabilities.

## Per-Model Test Structure

### Model Configuration
- **Provider**: `<provider_name>`
- **Model ID**: `<model_id>:free` or `<provider>:<model_slug>`
- **Auth Status**: Valid / Rate-limited / Auth-failed / Exhausted (from catalog)
- **Probe Eligibility**: Only run if probe? = valid (not 429/401)

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
- **Full Response**: The model's complete output

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

1. Rank all 7 probed models by quality score
2. Select top 5 models for Hermes configuration
3. Configure primary model via `hermes config set model.default`
4. Configure fallback chain via `hermes fallback clear` + `hermes fallback add`
5. Verify with `hermes config check` and `hermes fallback list`
