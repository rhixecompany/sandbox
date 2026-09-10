---
name: opencode-omo-workspace-config
description: Workspace-level OpenCode and Oh-My-OpenCode configuration — enhanced for larger context tokens (200k), longer/high-compression compaction, best-model routing (Nemotron-3 Ultra, Inkling for reasoning, DeepSeek Flash for speed), DRY plugin synchronization, and multi-stage verification.
version: 2.0.0
author: Sisyphus / Hermes Agent
platforms: [windows, macos, linux]
required_plugins:
  - oh-my-openagent@latest
  - opencode-antigravity-auth@latest
  - superpowers@git+https://github.com/obra/superpowers.git#main
optional_plugins:
  - context-engineing
  - cli-enhancements
  - tui-enhancements
  - eagle-eye
  - cronalytics
  - weather
  - telegram-bot
---

# Workspace OMO / OpenCode Configuration Skill

When configuring this workspace, read `.opencode/opencode.json` (canonical) and `.omo/config.json` (OMO layer) together. They are designed to stay in sync via shared plugin arrays and model routing definitions.

## Key Enhancements Applied

- Context: `200000` tokens (large)
- Compaction: `high` compression, `15000` line history, `500` line threshold
- Model routing: Best accuracy (Nemotron-3 Ultra 550B), reasoning (Inkling), speed (DeepSeek Flash)
- Plugins: superpowers, cli-enhancements, context-engineing, tui-enhancements enabled
- DRY: `.omo/templates/` for reusable patterns; `.hermes.md` overrides highest

## Verification

Run `.opencode` smoke tests: `python -m pytest tests/test_opencode_smoke.py -v -k "status" -n 0`
Check `.omo/config.json` syntax: `python -c "import json; json.load(open('.omo/config.json'))"`
