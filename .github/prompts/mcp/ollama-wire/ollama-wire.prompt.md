---
name: ollama-wire
description: Wire a local ollama model into Hermes, OpenCode (oh-my-opencode), Codex, and Copilot. Detects models on disk, patches all 4 configs, verifies the wiring.
trigger: /ollama-wire
category: mcp
version: 1.0.0
author: Hermes Agent
license: MIT
tags: 
metadata: 
hermes: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
title: Ollama Wire (4-Agent)
---

# Ollama Wire (4-Agent)

Wire a local ollama model into the four AI agents used in the workspace.

## Steps

1. **Pull the model** (if not on disk):
   ```bash
   ollama pull qwen3-vl:2b
   ```

   As of 2026-08-29, best local model ≥200K context, vision, reasoning:
   - **`qwen3-vl:2b`** (1.9 GB, 256K ctx, vision+reasoning) — fits in 6 GB free
   - `gemma4:12b` (7.6 GB, 128K ctx) — needs 8+ GB free
   - `qwen3-vl:8b` (~5 GB, 256K ctx) — needs 6+ GB free

2. **Wire all 4 agents**:
   ```bash
   python scripts/ollama_wire.py --model qwen3-vl:2b
   ```

   The script patches:
   - `~/AppData/Local/hermes/config.yaml` (providers.ollama-launch.default_model)
   - `~/.config/opencode/opencode.json` (model.ollama-local)
   - `.codex/mcp.json` (mcpServers.ollama-local.env.OLLAMA_MODEL)
   - `.copilot/mcp.json` (mcpServers.ollama-local.env.OLLAMA_MODEL)

   Use `--dry-run` to preview.

3. **Verify**:
   ```bash
   ollama list | grep qwen3-vl:2b
   grep -A 3 "ollama-launch:" ~/AppData/Local/hermes/config.yaml
   cat ~/.config/opencode/opencode.json | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('model', {}).get('ollama-local', 'MISSING'))"
   cat .codex/mcp.json | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('mcpServers', {}).get('ollama-local', {}).get('env', {}).get('OLLAMA_MODEL', 'MISSING'))"
   ```

4. **Test hermes**:
   ```bash
   timeout 180 hermes chat -m qwen3-vl:2b --provider ollama-launch -q "Reply OK" --oneshot --ignore-rules
   ```

5. **Test ollama directly** (sanity):
   ```bash
   echo "exit" | ollama run qwen3-vl:2b "Reply OK"
   ```

## Pitfalls

- **Disk**: 27B+ models need 15-30 GB. Stick to 2B-4B on tight disks.
- **First-call latency**: ~60-90s for the first chat after pull (model load + agent init).
- **Title-gen 429**: Separate model generates session titles; 429 doesn't break main response.
- **Rollback**: Just rerun with the previous model name.
- **`ollama serve` must be running** before `hermes chat` works.

## Verification

## Goal
Wire a local ollama model into Hermes, OpenCode (oh-my-opencode), Codex, and Copilot. Detects models on disk, patches all 4 configs, verifies the wiring.

## Context

## Workflow

<content>

<content>

<content>

- [ ] All 4 configs reference the same model
- [ ] `ollama list` shows the model
- [ ] `hermes chat` returns a response
- [ ] No regression in other providers

See `~/AppData/Local/hermes/skills/devops/ollama-wire/SKILL.md` for the full skill.
```
# Prompt template
Execute the workflow defined in this file.
```
