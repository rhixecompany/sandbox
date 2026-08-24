# Comprehensive Context Files & Model Sync Implementation Plan

## Overview
Create/update SOUL.md, USER.md, MEMORY.md in SandBox root, update context files with multi-file change protocol, process test-providers-models.prompt.md with verified working models, and configure all AI agents accordingly.

## Current State Analysis
- **SOUL.md**: Exists at `C:/Users/Alexa/AppData/Local/hermes/SOUL.md` (12135 bytes), NOT in SandBox root
- **USER.md**: Exists in Hermes profiles, NOT in SandBox root
- **MEMORY.md**: Exists in Hermes profiles, NOT in SandBox root
- **.hermes.md**: Exists in SandBox root (113 lines, has multi-file protocol at lines 75-100)
- **AGENTS.md**: Exists in SandBox root (661 lines, canonical agent guidance)
- **CLAUDE.md**: Exists in SandBox root (6 lines, thin stub)
- **.cursorrules**: Exists in SandBox root (7 lines, thin stub)
- **test-providers-models.prompt.md**: Exists in `.github/prompts/` (239 lines, needs update with verified models)

## Files to Modify (8 total - triggers Multi-File Change Protocol)

| # | File | Action | Priority |
|---|------|--------|----------|
| 1 | `C:/Users/Alexa/Desktop/SandBox/SOUL.md` | Create (copy from Hermes root) | P0 |
| 2 | `C:/Users/Alexa/Desktop/SandBox/USER.md` | Create (pointer to Hermes) | P0 |
| 3 | `C:/Users/Alexa/Desktop/SandBox/MEMORY.md` | Create (pointer to Hermes) | P0 |
| 4 | `C:/Users/Alexa/Desktop/SandBox/.hermes.md` | Update (verify protocol present) | P0 |
| 5 | `C:/Users/Alexa/Desktop/SandBox/AGENTS.md` | Update (add protocol reference) | P1 |
| 6 | `C:/Users/Alexa/Desktop/SandBox/CLAUDE.md` | Update (add protocol reference) | P1 |
| 7 | `C:/Users/Alexa/Desktop/SandBox/.cursorrules` | Update (add protocol reference) | P1 |
| 8 | `C:/Users/Alexa/Desktop/SandBox/.github/prompts/test-providers-models.prompt.md` | Update (verified models only) | P0 |

## Phase 1: Core Context Files Creation (P0)

### Task 1.1: Create SOUL.md in SandBox Root
- **Source**: `C:/Users/Alexa/AppData/Local/hermes/SOUL.md`
- **Action**: Copy file to SandBox root
- **Verification**: `diff` confirms identical content
- **Timeline**: 5 min

### Task 1.2: Create USER.md in SandBox Root
- **Content**: Pointer file referencing `~/AppData/Local/hermes/profiles/default/USER.md` (or profile-specific)
- **Format**: Minimal frontmatter + pointer to canonical location
- **Timeline**: 5 min

### Task 1.3: Create MEMORY.md in SandBox Root
- **Content**: Pointer file referencing `~/AppData/Local/hermes/profiles/default/MEMORY.md`
- **Format**: Minimal frontmatter + pointer to canonical location
- **Timeline**: 5 min

### Task 1.4: Verify .hermes.md Protocol
- **Action**: Read current file, confirm Multi-File Change Protocol section (lines 75-100) is present and accurate
- **Verification**: Check protocol includes all 14 required skills
- **Timeline**: 5 min

## Phase 2: Context Files Enhancement (P1)

### Task 2.1: Update AGENTS.md
- **Action**: Add Multi-File Change Protocol reference in Section 10 (Safety Rules) or new section
- **Content**: Reference to `.hermes.md` protocol + 14-skill stack requirement
- **Timeline**: 10 min

### Task 2.2: Update CLAUDE.md
- **Action**: Add protocol reference line
- **Content**: `- Multi-file protocol (≥5 files): see .hermes.md lines 75-100`
- **Timeline**: 5 min

### Task 2.3: Update .cursorrules
- **Action**: Add protocol reference line
- **Content**: `- Multi-file protocol (≥5 files): see .hermes.md lines 75-100`
- **Timeline**: 5 min

## Phase 3: Test Providers Models Prompt Update (P0)

### Task 3.1: Analyze Current Verified Models
- **Source**: test-providers-models.prompt.md Context Block (lines 88-116)
- **Verified Working (2026-08-07 baseline)**:
  - `nemotron-3-ultra-free` (opencode-zen, 1M ctx, reasoning✓)
  - `nvidia/nemotron-3-ultra-550b-a55b:free` (openrouter, 1M ctx)
  - `nvidia/nemotron-3-super-120b-a12b:free` (openrouter, 1M ctx)
  - `gemini-2.5-flash` (gemini, 1M ctx, reasoning✓)
  - `nemotron-3-ultra` (ollama-cloud, 1M ctx)
  - `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (openrouter, 256K ctx)
  - `deepseek-v4-flash-free` (opencode-zen, 128K ctx, reasoning✓) — PRIMARY
- **Non-working**: deepseek, huggingface, nous, xai-oauth, openai-codex, copilot
- **No vision models** in free tier

### Task 3.2: Update Prompt with Current Verified Set
- **Action**: Update Context Block with latest verified models
- **Remove**: Stale/non-working providers from fallback chain
- **Ensure**: Deterministic ordering (vision → reasoning → context)
- **Timeline**: 15 min

### Task 3.3: Configure Hermes Primary & Fallback
- **Primary**: `opencode-zen` / `deepseek-v4-flash-free` (set on all 13 profiles)
- **Fallback chain**: `["opencode-zen", "openrouter", "gemini", "ollama-cloud"]`
- **Per-provider defaults**: Set via `hermes config set`
- **Commands**:
  ```bash
  hermes config set model.provider opencode-zen
  hermes config set model.default deepseek-v4-flash-free
  hermes config set fallback_providers '["opencode-zen","openrouter","gemini","ollama-cloud"]'
  hermes config set providers.opencode-zen.default_model deepseek-v4-flash-free
  hermes config set providers.openrouter.default_model "nvidia/nemotron-3-ultra-550b-a55b:free"
  hermes config set providers.gemini.default_model "gemini-2.5-flash"
  hermes config set providers.ollama-cloud.default_model "nemotron-3-ultra"
  ```
- **Timeline**: 10 min

## Phase 4: Agent Configuration Propagation (P1)

### Task 4.1: Sync Profile Configs
- **Script**: `~/AppData/Local/hermes/scripts/sync_profile_configs.py`
- **Action**: Propagate root config to all 13 profiles
- **Verification**: `hermes profile list` shows consistent models
- **Timeline**: 5 min

### Task 4.2: Update OpenCode Configuration
- **Target**: `~/.opencode/` and project `opencode.json`
- **Action**: Ensure model aligns with Hermes primary
- **Timeline**: 5 min

### Task 4.3: Update Codex Configuration
- **Target**: Codex auth/config
- **Action**: Verify alignment
- **Timeline**: 5 min

## Phase 5: Verification Gates (P0)

### Gate 1: Config Validation
- **Command**: `hermes config check`
- **Expected**: Pass
- **Criteria**: No errors, fallback_providers is YAML list

### Gate 2: YAML Structure Verification
- **Command**: 
  ```bash
  python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print(type(c['fallback_providers']), c['fallback_providers'])"
  ```
- **Expected**: `<class 'list'>` with 4 providers in correct order

### Gate 3: Model Resolution Test
- **Command**: `hermes config show`
- **Expected**: 
  - `model.provider = opencode-zen`
  - `model.default = deepseek-v4-flash-free`
  - `fallback_providers` shows list (not string)

### Gate 4: Profile Consistency
- **Command**: `hermes profile list`
- **Expected**: All profiles show `opencode-zen` / `deepseek-v4-flash-free`

### Gate 5: Prompt Library Update
- **File**: `docs/free-model-selection.md`
- **Action**: Update with new chain
- **Criteria**: Matches configured fallback chain

### Gate 6: File Existence & Content
- **Verify**: All 8 files exist with correct content
- **SOUL.md**: Matches Hermes root
- **USER.md/MEMORY.md**: Valid pointers
- **Context files**: Protocol references present

## Timeline & Milestones

| Milestone | Target | Duration | Dependencies |
|-----------|--------|----------|--------------|
| M1: Core files created | T+20min | 20 min | None |
| M2: Context files enhanced | T+35min | 15 min | M1 |
| M3: Prompt updated | T+50min | 15 min | None |
| M4: Hermes configured | T+60min | 10 min | M3 |
| M5: Profiles synced | T+65min | 5 min | M4 |
| M6: All gates pass | T+80min | 15 min | M5 |

**Total Estimated Time**: 80 minutes

## Resource Allocation

| Resource | Allocation |
|----------|------------|
| Primary Agent | Orchestration, file ops, config |
| Subagent 1 (delegate_task) | Verify model probes, test each provider |
| Subagent 2 (delegate_task) | Profile sync verification |
| Skills Used | All 14 from Multi-File Protocol |
| MCP Servers | filesystem, memory, sequential-thinking |

## Risk Assessment & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Config string-encoded fallback_providers | High | Medium | Repair via terminal Python one-liner |
| Profile sync drift | Medium | High | Run sync script, verify all 13 profiles |
| Stale model in prompt | Medium | Medium | Update prompt with live verified set |
| Missing USER.md/MEMORY.md in profiles | Low | Medium | Create placeholder pointers |
| Vision model gap | Certain | Low | Document degradation to reasoning→context |

## Verification Checklist (Final)

- [ ] All 8 files created/updated with correct content
- [ ] `hermes config check` passes
- [ ] `fallback_providers` is YAML list (not string)
- [ ] Primary model = opencode-zen/deepseek-v4-flash-free
- [ ] Fallback chain ordered: opencode-zen → openrouter → gemini → ollama-cloud
- [ ] Each fallback provider has working free default_model
- [ ] All 13 profiles synced to root config
- [ ] test-providers-models.prompt.md updated with verified set
- [ ] docs/free-model-selection.md updated
- [ ] No non-working providers in fallback chain
- [ ] Multi-file protocol referenced in all context files

## Execution Strategy

Use **subagent-driven-development** for parallel execution:
1. Subagent A: File creation/updates (Tasks 1.1-1.4, 2.1-2.3)
2. Subagent B: Prompt update & Hermes config (Tasks 3.1-3.3)
3. Subagent C: Profile sync & agent config (Tasks 4.1-4.3)
4. Main: Verification gates (Phase 5)

Each subagent gets full context, follows TDD, undergoes 2-stage review (spec compliance → quality).