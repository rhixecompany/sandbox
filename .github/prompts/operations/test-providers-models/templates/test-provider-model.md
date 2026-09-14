---
name: test-providers-model-template
title: Test Provider Model Template
description: "Template for testing individual provider models"
category: testing
---

# Test {{provider_name}} {{model_name}}

## Goal
Test the {{model_name}} model from {{provider_name}} with the canonical
self-profile prompt and record capabilities, quality, and performance.

## Context
- Provider: {{provider_name}}
- Model: {{model_name}}
- Capabilities: {{capabilities}}
- Probe prompt: `hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released`
- Provider status: {{provider_status}}

## Workflow
1. Read `hermes auth list` and stop if {{provider_name}} is rate-limited (`rate-limited`, `429`, `too many requests`, quota exhaustion, or throttling evidence).
2. Execute the canonical test via `hermes chat --provider {{provider_name}} --model {{model_name}} -q "hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released" --oneshot`.
3. If the request returns a rate-limit error, mark the provider rate-limited and skip its remaining models.
4. Measure response quality, latency, and accuracy; record the result in the test catalog.

## Verification
- Response captured and scored
- Latency measured
- Quality rating assigned
- Rate-limited providers are explicitly skipped and never selected for fallback.
