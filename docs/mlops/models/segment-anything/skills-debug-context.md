# Skill Audit: `segment-anything`

**Category:** mlops/models  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\mlops\models\segment-anything\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: segment-anything-model
title: Segment Anything
description: "SAM: zero-shot image segmentation via points, boxes, masks."
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [segment-anything, transformers>=4.30.0, torch>=1.7.0]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multimodal, Image Segmentation, Computer Vision, SAM, Zero-Shot]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |
| MINOR | C3 | Table pipe count inconsistency: {3, 4, 6} |

## Sections Present

- • `## When to use SAM`
- • `## Quick start`
- • `## Core concepts`
- • `## Interactive segmentation`
- • `## Automatic mask generation`
- • `## Batched inference`
- • `## ONNX deployment`
- • `## Common workflows`
- • `## Output format`
- • `## Performance optimization`
- • `## Common issues`
- • `## References`
- • `## Resources`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
- Fix `C3`: Table pipe count inconsistency: {3, 4, 6}
