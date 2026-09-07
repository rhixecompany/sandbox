---
name: test-providers-model-template
title: Test Provider Model Template
description: "Template for testing individual provider models"
category: testing
---

# Test {{provider_name}} {{model_name}}

## Goal
Test the {{model_name}} model from {{provider_name}} for capabilities, quality, and performance.

## Context
- Provider: {{provider_name}}
- Model: {{model_name}}
- Capabilities: {{capabilities}}

## Workflow
1. Execute test task via hermes chat --provider {{provider_name}} --model {{model_name}} --oneshot
2. Measure response quality, latency, and accuracy
3. Record results in the test catalog

## Verification
- Response captured and scored
- Latency measured
- Quality rating assigned
