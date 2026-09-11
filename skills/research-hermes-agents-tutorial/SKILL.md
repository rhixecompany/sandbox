---
name: research-hermes-agents-tutorial
title: Hermes Agent Research Digest
description: "Use when learning or building Hermes Agent: quickstart, architecture, agent loop, system prompt assembly. Digest CLI + research files."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, agents, ai, research]
---

# Hermes Agent Research Digest

## Overview

Wraps `research/hermes-agents-tutorial/` (3 md files: NetworkChuck course notes, deep-dive build-your-own guide, quickstart). Use when studying or extending Hermes agent behavior.

## When to Use

- Setting up Hermes for the first time (quickstart file)
- Understanding the agent loop and system prompt assembly order (deep-dive)
- Learning what makes Hermes different (course notes)

## Workflow

### Phase 1: Digest

```bash
python scripts/research_hermes_agents_tutorial.py
python scripts/research_hermes_agents_tutorial.py --file "research/hermes-agents-tutorial/hermes-agent-deep-dive-build-your-own-guide.md"
```

### Phase 2: Apply

- Installation + provider choice steps come from the quickstart
- Agent loop: read message → plan → tool call → observe → continue until done
- System prompt assembly order matters: SOUL → USER → tasks/skills (deep-dive has the exact chain)

### Phase 3: Verify

- Run `hermes --version` / first chat per quickstart
- After customizing SOUL.md, confirm the assembled prompt includes your layers in order

## Pitfalls

- Minimum context requirement varies by provider — quickstart lists it; don't under-provision
- Settings storage location differs per OS — follow quickstart paths

## Verification Checklist

- [ ] Digest script exits 0 for list and --file modes
- [ ] Claims about Hermes internals cited from deep-dive file

## References

- `research/hermes-agents-tutorial/hermes-agent-build-your-own-learning-ai-worker-networkchuck.md`
- `research/hermes-agents-tutorial/hermes-agent-deep-dive-build-your-own-guide.md`
- `research/hermes-agents-tutorial/hermes-agent-quickstart-guide.md`
- Script: `scripts/research_hermes_agents_tutorial.py` | Test: `scripts/tests/test_research_hermes_agents_tutorial.py`
