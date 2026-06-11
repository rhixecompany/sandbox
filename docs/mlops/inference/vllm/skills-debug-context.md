# Skill Audit: `vllm`

**Category:** mlops/inference  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\mlops\inference\vllm\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: serving-llms-vllm
title: Vllm
description: "vLLM: high-throughput LLM serving, OpenAI API, quantization."
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [vllm, torch, transformers]
platforms: [linux, macos]
metadata:
  hermes:
    tags: [vLLM, Inference Serving, PagedAttention, Continuous Batching, High Throughput, Production, OpenAI API, Quantization, Tensor Parallelism]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |

## Sections Present

- ✅ `## When to use`
- • `## Quick start`
- • `## Common workflows`
- • `## When to use vs alternatives`
- • `## Common issues`
- • `## Advanced topics`
- • `## Hardware requirements`
- • `## Resources`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
