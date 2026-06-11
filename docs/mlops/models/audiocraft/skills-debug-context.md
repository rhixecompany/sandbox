# Skill Audit: `audiocraft`

**Category:** mlops/models  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\mlops\models\audiocraft\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: audiocraft-audio-generation
title: Audiocraft
description: "AudioCraft: MusicGen text-to-music, AudioGen text-to-sound."
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [audiocraft, torch>=2.0.0, transformers>=4.30.0]
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Multimodal, Audio Generation, Text-to-Music, Text-to-Audio, MusicGen]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |
| MINOR | C3 | Table pipe count inconsistency: {3, 4, 5} |

## Sections Present

- • `## When to use AudioCraft`
- • `## Quick start`
- • `## Core concepts`
- • `## MusicGen usage`
- • `## MusicGen-Style usage`
- • `## AudioGen usage`
- • `## EnCodec usage`
- • `## Common workflows`
- • `## Performance optimization`
- • `## Common issues`
- • `## References`
- • `## Resources`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
- Fix `C3`: Table pipe count inconsistency: {3, 4, 5}
