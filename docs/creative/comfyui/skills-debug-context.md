# Skill Audit: `comfyui`

**Category:** creative  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\creative\comfyui\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: comfyui
title: Comfyui
description: "Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli for lifecycle and direct REST/WebSocket API for execution."
version: 5.1.0
author: [kshitijk4poor, alt-glitch, purzbeats]
license: MIT
platforms: [macos, linux, windows]
compatibility: "Requires ComfyUI (local, Comfy Desktop, or Comfy Cloud) and comfy-cli (auto-installed via pipx/uvx by the setup script)."
prerequisites:
  commands: ["python3"]
setup:
  help: "Run scripts/hardware_check.py FIRST to decide local vs Comfy Cloud; then scripts/comfyui_setup.sh auto-installs locally (or use Cloud API key for platform.comfy.org)."
metadata:
  hermes:
    tags:
      - comfyui
      - image-generation
      - stable-diffusion
      - flux
      - sd3
      - wan-video
      - hunyuan-video
      - creative
      - generative-ai
      - video-generation
    related_skills: [stable-diffusion-image-generation, image_gen]
    category: creative
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |

## Sections Present

- • `## What's in this skill`
- ✅ `## When to Use`
- • `## Architecture: Two Layers`
- • `## Quick Start`
- • `## Core Workflow`
- • `## Decision Tree`
- • `## Setup & Onboarding`
- • `## Image Upload (img2img / Inpainting)`
- • `## Cloud Specifics`
- • `## Queue & System Management`
- • `## Pitfalls`
- ✅ `## Workflow`
- • `## Overview`
- • `## Verification Checklist`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
