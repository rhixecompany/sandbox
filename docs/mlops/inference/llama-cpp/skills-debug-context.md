# Skill Audit: `llama-cpp`

**Category:** mlops/inference  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\mlops\inference\llama-cpp\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: llama-cpp
title: Llama Cpp
description: llama.cpp local GGUF inference + HF Hub model discovery.
version: 2.1.2
author: Orchestra Research
license: MIT
dependencies: [llama-cpp-python>=0.2.0]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [llama.cpp, GGUF, Quantization, Hugging Face Hub, CPU Inference, Apple Silicon, Edge Deployment, AMD GPUs, Intel GPUs, NVIDIA, URL-first]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |

## Sections Present

- ✅ `## When to use`
- • `## Model Discovery workflow`
- • `## Quick start`
- • `## Python bindings (llama-cpp-python)`
- • `## Choosing a quant`
- • `## Extracting available GGUFs from a repo`
- • `## Search patterns`
- • `## Output format`
- • `## References`
- • `## Resources`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
