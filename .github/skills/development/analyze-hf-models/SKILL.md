---
name: analyze-hf-models
title: Analyze HF Models
description: Analyzes HuggingFace model configurations and metadata
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - huggingface
  - models
  - analysis
---

# Analyze HF Models

## Overview

Wrapper skill for the `analyze_hf_models.py` script in `~/AppData/Local/hermes/scripts/`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/analyze_hf_models.py`

**Usage:**

```bash
python analyze_hf_models.py [options]
```

## When to Use

- When you need to inspect or analyze HuggingFace model metadata
- When comparing model configurations across versions

## When NOT to Use

- When you need to download or train models
- For simple model search (use HuggingFace Hub directly)

## Workflow

### Phase 1: Setup

Ensure `huggingface_hub` is installed and API token is configured if needed.

### Phase 2: Execute

Run the script with model identifiers or search terms.

### Phase 3: Analyze Results

Review the output for configuration differences or metadata patterns.

## Verification Checklist

- [ ] Script runs without import errors
- [ ] Model metadata is correctly parsed
- [ ] Output is structured and readable
- [ ] API rate limits are respected
- [ ] Results match expected model configurations

## Pitfalls

- Rate limiting from HuggingFace API may slow analysis
- Large model lists may require pagination handling
