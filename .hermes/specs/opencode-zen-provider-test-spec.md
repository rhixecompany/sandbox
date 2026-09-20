---
name: opencode-zen-provider-test
title: "OpenCode-Zen Provider Model Test"
description: "Test all opencode-zen provider models via API to find working ones, then configure Hermes fallback"
version: 1.0.0
date_created: 2026-09-17
status: In progress
goal: Test opencode-zen models → identify working 3 → clear Hermes fallback → configure best 3
---

# OpenCode-Zen Provider Model Test Spec

## Goal

Test all opencode-zen provider models via curl/python with API key + URL, log models that return valid responses, then clear and configure Hermes fallback with best 3 working models.

## Requirements

- REQ-001: Read OPENCODE_ZEN_API_KEY and OPENCODE_ZEN_BASE_URL from `$HOME/AppData/Local/hermes/.env`
- REQ-002: Test each model with 3 prompts: identity, capabilities, reasoning
- REQ-003: Valid response = HTTP 200 + non-empty JSON with expected fields (model, choices, message/content)
- REQ-004: Log all results (model, prompt_type, response_time, valid, error)
- REQ-005: Clear existing fallback_providers in hermes config.yaml
- REQ-006: Configure best 3 working models as fallback chain
- REQ-007: Never expose API keys in output, logs, or artifacts
- REQ-008: Use clarify for all questions and approvals

## Test Prompts

| #   | Type         | Prompt                                                                                                                                                                         |
| --- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Identity     | "What is your model name and who created you? Respond in JSON: {model, creator, type}"                                                                                         |
| 2   | Capabilities | "What are your top 3 capabilities? Respond in JSON: {capabilities: [c1, c2, c3]}"                                                                                              |
| 3   | Reasoning    | "Solve: If a train leaves station A at 60mph and another leaves station B at 80mph toward A 200 miles apart, when do they meet? Respond in JSON: {answer, reasoning, formula}" |

## Valid Response Criteria

- HTTP status = 200
- Non-empty body
- JSON parseable
- Contains `choices` or `message` or `content` field
- Response time < 30s

## Models to Test (from opencode-zen pool)

1. `openrouter/thinkingmachines/inkling:free` (current default)
2. `deepseek-v4-flash-free` (current opencode-zen default)
3. All models in opencode-zen pool

## Deliverables

1. `results/opencode-zen-test-results.json` — all model test results
2. `results/opencode-zen-best-3.md` — best 3 working models ranked
3. Updated `config.yaml` — fallback_providers cleared and set to best 3
