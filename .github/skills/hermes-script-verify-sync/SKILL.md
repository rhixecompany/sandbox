---
name: hermes-script-verify-sync
title: Cross-Platform Sync Verification
description: "Verify Hermes/Codex/OpenCode config parity across profiles."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, scripts, devops, sync, verification, multi-agent]
metadata:
  hermes:
    tags: [hermes, scripts, devops, sync, verification]
    related_skills: [multi-agent-sync, hermes-profiles]
    script_path: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\scripts\\verify_sync.py"
---

# Cross-Platform Sync Verification Skill

## Overview

Verifies that Hermes, Codex CLI, and OpenCode configurations are in sync across all profiles. Checks MCP servers, skills, hooks, plugins, models, and toolsets.

## When to Use

- After modifying Hermes config or profiles
- Before starting multi-agent work
- CI/CD gate for config drift detection
- Debugging "works in Hermes but not Codex" issues

## Script Interface

**Path:** `$LOCALAPPDATA/hermes/scripts/verify_sync.py`

```bash
# Full verification (dry-run)
MSYS_NO_PATHCONV=1 python3 verify_sync.py

# JSON output for automation
MSYS_NO_PATHCONV=1 python3 verify_sync.py --json
```

## Checks Performed (10)

1. Hermes config.yaml exists and parses
2. Codex ~/.codex/config.toml exists and parses
3. OpenCode ~/.opencode/opencode.json exists and parses
4. All 21 MCP servers defined in Hermes config
5. Skill counts match (Hermes 657 ≈ Codex 656 ≈ OpenCode 656)
6. Hooks parity (session-logger, session-auto-commit, governance-audit)
7. Profile count: 6 profiles + default
8. Model pins match across agents
9. Toolset availability
10. OpenCode CLI functional + auth

## Skills Required

| Skill | Purpose |
|---|---|
| `multi-agent-sync` | Sync skills/plugins/hooks/profiles |
| `hermes-profiles` | Profile identity & state |
| `hermes-diagnostic-repair` | Diagnose provider chain failures |

## Workflow

### Phase 1: Load Configs
1. Parse Hermes config.yaml
2. Parse Codex config.toml
3. Parse OpenCode opencode.json

### Phase 2: Compare
1. Count skills in each agent's skill dir
2. Enumerate MCP servers in each config
3. Verify hook versions match
4. Check profile blocks exist

### Phase 3: Test
1. Run `opencode.cmd --version`
2. Run `opencode.cmd auth list`
3. Compare model pins

### Phase 4: Report
1. Print PASSES/ERRORS summary
2. Exit code 0 if all pass, 1 otherwise

## Verification Checklist

- [ ] All 10 checks execute without exception
- [ ] Skill count diff ≤ 2 (acceptable drift)
- [ ] All 21 MCP servers present in Hermes
- [ ] OpenCode CLI returns 0 exit code
- [ ] JSON output valid for automation

## Pitfalls

- **MSYS paths**: Use `MSYS_NO_PATHCONV=1` prefix from git-bash
- **OpenCode timeout**: CLI may hang on first run; 5s timeout in script
- **Config formats**: Hermes=YAML, Codex=TOML, OpenCode=JSON
- **Profile sync**: Hermes has 7 profiles; Codex/OpenCode use single config