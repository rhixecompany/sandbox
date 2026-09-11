---
name: research-hermes-memory-files
title: Hermes Memory Architecture Research Digest
description: "Use when working with Hermes memory: SOUL.md/MEMORY.md/state.db layers, memory tool actions. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, memory, architecture, research]
---

# Hermes Memory Architecture Research Digest

## Overview

Wraps `research/hermes-memory-files/` (3 md files: luma-dock architecture, Nous persistent-memory docs, SOUL.md personality docs). Use when configuring memory layers or editing SOUL.md.

## When to Use

- Editing SOUL.md / MEMORY.md and needing the intended design
- Understanding the 3 memory layers (SOUL.md, MEMORY.md, state.db)
- Using the memory tool actions correctly (add/replace/remove, targets user/memory)

## Workflow

### Phase 1: Digest

```bash
python scripts/research_hermes_memory_files.py
python scripts/research_hermes_memory_files.py --file "research/hermes-memory-files/nous-research-hermes-persistent-memory.md"
```

### Phase 2: Apply

- Layers: Layer 1 SOUL.md (persona/boundaries), MEMORY.md (durable facts), state.db (session truth)
- Memory tool: two targets (user profile / agent memory) — choose per fact type
- SOUL.md content: identity, boundaries, style; keep it small and high-signal

### Phase 3: Verify

- After edits, inspect the system prompt or memory view to confirm the entry appears where intended
- Check state.db/session logs for memory tool actions if behavior is unexpected

## Pitfalls

- Putting task progress in MEMORY.md pollutes every session — keep only durable facts
- SOUL.md should not duplicate USER.md content (DRY)

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Memory edits align with the layer docs

## References

- `research/hermes-memory-files/luma-dock-hermes-memory-architecture.md`
- `research/hermes-memory-files/nous-research-hermes-persistent-memory.md`
- `research/hermes-memory-files/nous-research-hermes-personality-soul.md`
- Script: `scripts/research_hermes_memory_files.py` | Test: `scripts/tests/test_research_hermes_memory_files.py`
