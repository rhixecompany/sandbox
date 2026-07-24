---
name: test-providers-models
title: Test Providers & Models
project_path: C:\Users\Alexa\Desktop\SandBox
description: Inventory configured providers/models in Hermes config; validate availability publicly; extract free-tier candidates; benchmark only if enabled; report results to docs/; parallel-safe reads.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets: - file - terminal - browser - skills
scripts: []
skills: - using-superpowers - user-communication-preferences - plans-and-specs - executing-plans - verification-before-completion - subagent-driven-development
formatter: default
plan: |
  ### Phase 1: Configuration Inventory
  - Parse Hermes config.yaml: `C:\Users\Alexa\AppData\Local\hermes\config.yaml`
  - Extract provider definitions, model lists, authentication details
  - Save raw config data: `docs/providers/raw-config.json`

  ### Phase 2: Public Validation Checks
  - For each provider, run read-only availability checks:
    - Health endpoint: GET /health or equivalent
    - Model listing endpoint: GET /models or equivalent
    - Free model filtering: identify models with zero-cost access
  - Record responses: `docs/providers/validation-responses.json`

  ### Phase 3: Free Model Extraction
  - Process validation results
  - Filter to zero-cost models only
  - Extract model metadata: name, capabilities, limits, pricing
  - Generate free-model inventory: `docs/providers/free-models-inventory.json`

  ### Phase 4: Benchmark (Conditional)
  - If benchmarking enabled: `hermes config get providers.benchmark.enabled` returns true
  - Run latency/performance tests for a subset of models
  - Record results: `docs/providers/benchmark-results.json`

  ### Phase 5: Report Generation
  - Compile comprehensive report: `docs/providers/provider-inventory-report.md`
  - Include: provider status, model counts, free model highlights, benchmark results

  ### Phase 6: Progress Tracking
  - Update orchestrator progress tracker
  - Log phase completion

dependencies: - skill:using-superpowers - skill:user-communication-preferences - skill:plans-and-specs - skill:executing-plans - skill:verification-before-completion - skill:subagent-driven-development
project_path: C:\Users\Alexa\Desktop\SandBox
tags: - inventory - benchmark - report
trigger: /test-providers-models
metadata:
  related_skills: [using-superpowers, user-communication-preferences, plans-and-specs, executing-plans, verification-before-completion, subagent-driven-development]
  workspace_path: C:\Users\Alexa\Desktop\SandBox
  output_dir: C:\Users\Alexa\Desktop\SandBox\docs\providers
  config_path: C:\Users\Alexa\AppData\Local\hermes\config.yaml
  inventory_report: docs/providers/provider-inventory-report.md
  validation_log: docs/providers/validation-responses.json
  free_models_inventory: docs/providers/free-models-inventory.json
  benchmark_results: docs/providers/benchmark-results.json
---

# Test Providers & Models

## Overview

Inventory Hermes providers and models, validate public availability, extract free-tier candidates, and generate comprehensive reports for the workspace.

## Phase 1: Configuration Inventory

1. **Parse Hermes configuration**
   - Execute: `hermes config read C:\Users\Alexa\AppData\Local\hermes\config.yaml`
   - Extract provider definitions, model configurations
   - Convert to structured JSON: `docs/providers/raw-config.json`

2. **Validate config structure**
   - Ensure providers have required fields: name, type, models, auth
   - Verify model schema: name, capabilities, limits, pricing
   - Write validation report: `docs/providers/config-validation.json`

## Phase 2: Public Validation Checks

1. **Run read-only availability tests**
   - For each provider endpoint:
     - Perform health checks
     - List available models
     - Record response codes and latency
   - Store all responses: `docs/providers/validation-responses.json`

2. **Model filtering**
   - Identify zero-cost models from validation results
   - Categorize by: free tier, pay-per-use, enterprise
   - Mark validation status: healthy, degraded, unavailable

## Phase 3: Free Model Extraction

1. **Process validation data**
   - Filter for free tier models only
   - Extract metadata: name, description, limits, constraints

2. **Generate inventory**
   - Create structured inventory: `docs/providers/free-models-inventory.json`
   - Include provider reference and model accessibility details

## Phase 4: Benchmark (Conditional)

1. **Check benchmarking flag**
   - If `hermes config get providers.benchmark.enabled` is true
   - Proceed with benchmark execution; otherwise skip

2. **Execute benchmark suite**
   - Run concurrency tests for selected models
   - Measure response times and throughput
   - Store results: `docs/providers/benchmark-results.json`

## Phase 5: Report Generation

1. **Compile provider inventory report**
   - Document overall provider health status
   - List active providers and their model counts
   - Highlight free model capabilities
   - Include benchmark results (if available)
   - Output: `docs/providers/provider-inventory-report.md`

2. **Update progress tracker**
   - Log phase completion
   - Record any warnings or errors

## Exit Condition

Test Providers & Models phase completes when:

- All providers inventoried and validated
- Free models identified and documented
- Conditional benchmarking completed (if enabled)
- Comprehensive report generated
- Progress tracker updated
- All artifacts saved in `docs/providers/`

## Notes

- This phase validates both local configuration and remote provider availability
- Emphasizes read-only checks to respect provider rate limits
- Parallel-safe execution for provider health checks
- Focus on zero-cost model discovery for cost-effective operations
- Comprehensive reporting ensures transparency across Hermes ecosystem
