# Implementation Plan: Comprehensive Provider & Model Configuration

## Overview
This plan implements the comprehensive test-providers-models workflow to:
1. Inventory all authorized providers and current configuration
2. Probe working models with :free suffix across all providers
3. Rank verified working models by capability
4. Configure Hermes with optimal primary model + fallback chain
5. Propagate verified configuration to all installed agents
6. Verify the complete setup

## Phase 1: Inventory (Complete ✅)

### Completed Actions
- **hermes auth list** — Retrieved authorized providers:
  - nous (oauth, device_code)
  - opencode-zen (api_key + oauth)
  - openrouter (api_key)

- **hermes config show** — Current configuration:
  - Model: default='nemotron-3-ultra-free', provider='opencode-zen'
  - OpenRouter API key configured
  - API keys for multiple providers present

- **hermes profile list** — Available profiles confirmed

### Current State
- Primary model: nemotron-3-ultra-free (opencode-zen) ✅
- OpenRouter configured with API key
- No fallback providers configured

## Phase 2: Probe Models (In Progress)

### Working Free Models Identified
From live capability probes:

| Provider | Model | Vision | Reasoning | Context |
|---|---|---|---|---|
| **openrouter** | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | yes | yes | 2000 |
| **nous** | meituan/longcat-2.0:free | yes | yes | 2000 |
| **nous** | upstage/solar-pro4:free | yes | yes | 2000 |
| **opencode-zen** | nemotron-3-ultra-free | yes | yes | 2000 |
| **opencode-zen** | deepseek-v4-flash-free | pending | pending | pending |

### Models Excluded (failed probes)
- meta-llama/llama-3.1-8b-instruct:free — 404 Not Found
- anthropic/claude-3-haiku:free — 404 Not Found
- google/gemma-2-9b-it:free — Initialization failed

### Remaining Free Models to Probe
- opencode-zen: deepseek-v4-flash-free (already testing)
- openrouter: additional models beyond nemotron-3-nano

## Phase 3: Rank Models

### Ranking Algorithm (priority order)
1. `working=true` — Only verified working models
2. `vision=true` — Models with vision capability
3. `reasoning=true` — Models supporting chain-of-thought
4. `ctx` — Largest context window (capped at 2M tokens)

### Expected Ranked Chain
Based on current probe results:
1. nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (openrouter) — working, vision, reasoning, ctx=2000
2. meituan/longcat-2.0:free (nous) — working, vision, reasoning, ctx=2000
3. upstage/solar-pro4:free (nous) — working, vision, reasoning, ctx=2000
4. nemotron-3-ultra-free (opencode-zen) — working, vision, reasoning, ctx=2000
5. deepseek-v4-flash-free (opencode-zen) — to be confirmed

## Phase 4: Configure Hermes

### Commands to Execute

```bash
# 1. Set primary model (highest-ranked verified working)
hermes config set model.provider opencode-zen
hermes config set model.default nemotron-3-ultra-free

# 2. Set fallback chain (ordered by capability)
hermes config set fallback_providers '["openrouter","nous","opencode-zen"]'

# 3. Set default models per provider
hermes config set providers.openrouter.default_model "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
hermes config set providers.nous.default_model "meituan/longcat-2.0:free"
hermes config set providers.opencode-zen.default_model "nemotron-3-ultra-free"
```

### Verify YAML Type
```bash
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print(type(c['fallback_providers']), c['fallback_providers'])"
```

Expected: `fallback_providers` must be a YAML list, not a string.

## Phase 5: Propagate to Agents

### Files to Update
1. **Hermes profiles** (~/AppData/Local/hermes/profiles/*/):
   - SOUL.md — update model references
   - memories/USER.md — update model references
   - memories/MEMORY.md — update if stale

2. **Workspace context files**:
   - .hermes.md — update provider/model tables
   - AGENTS.md — update profile routing table
   - .github/copilot-instructions.md — update model references

3. **Agent configs**:
   - ~/.opencode/mcp.json — update model if referenced
   - ~/.codex/mcp.json — update model if referenced

### Propagation Rules
- Only models with `working=true` may be written
- Prefer `hermes config set` CLI; avoid raw YAML edits
- Record every changed file and command

## Phase 6: Verify (Pending)

### Verification Gates
- [ ] `hermes config check` passes
- [ ] `model.provider` and `model.default` set to verified working model
- [ ] `fallback_providers` is a YAML list ordered by capability
- [ ] Each listed provider has a working `default_model`
- [ ] Installed agents updated to verified working models only
- [ ] Non-working models excluded from config and instruction files
- [ ] No secrets/tokens introduced
- [ ] Documentation reflects verified chain

### Final Verification Commands
```bash
hermes config check
hermes profile list
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); assert isinstance(c['fallback_providers'], list), 'fallback_providers must be a list'; print('OK:', c['fallback_providers'])"
```