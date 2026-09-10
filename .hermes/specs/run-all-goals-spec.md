---
name: run-all-goals-spec
title: "Run All Goals — Specification (Phases 5-11)"
description: |
  Detailed specification for run-all-goals phases 5-11: diagnostic repair, model tests,
  agent sync, cleanup, config sync, git push, judge verification.
version: 1.0.0
author: Alexa
license: MIT
tags: [spec, run-all-goals, diagnostic, model-test, agent-sync, cleanup, git]
status: approved
linked_plan: master-skill-library-remediation
---

# Run All Goals — Specification (Phases 5-11)

## Phase 5: Diagnostic Repair

### Requirements
- `hermes doctor --fix` exits with code 0
- All 11 MCP servers test PASS
- All hooks registered and approved
- All plugins enabled and functional
- Profile switching works (adminbot, code-architect, default, etc.)
- Tooling MCP servers (python-quality, tooling-config, tooling-lint) connected

### Acceptance Criteria
| Check | Command | Expected |
|-------|---------|----------|
| Doctor | `hermes doctor --fix` | Exit 0, no errors |
| MCP Test | `hermes mcp test all` | All 11 PASS |
| Hooks | `hermes hooks list` | 4+ active, 0 failed |
| Plugins | `hermes plugins list` | 3+ enabled |
| Profiles | `hermes profile use adminbot && hermes profile use default` | Switches cleanly |
| Tooling MCP | `hermes mcp test python-quality && hermes mcp test tooling-config && hermes mcp test tooling-lint` | All PASS |

---

## Phase 6: Free Model Tests + Report

### Requirements
- Test all `:free` models on OpenRouter
- Test all free models on opencode-zen
- Generate markdown report with emoji, table format
- Report includes: capabilities, vision, reasoning, speed, context window
- Configure best primary + fallback chain in config.yaml

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| OpenRouter models tested | ≥10 free models |
| OpenCode-Zen models tested | ≥5 free models |
| Report format | Emoji markdown table |
| Report sections | Capabilities, Vision, Reasoning, Speed, Context |
| Config updated | Primary + 2 fallbacks configured |

---

## Phase 7: Agent Sync (5 Agents)

### Requirements
Sync hooks, skills, plugins, instructions to:
1. `.github/copilot` (GitHub Copilot)
2. `.codex` (OpenAI Codex)
3. `.opencode` (OpenCode)
4. `.hermes` (Hermes - current)
5. `.cursor` (Cursor IDE)

### Acceptance Criteria
| Asset Type | All 5 Identical? |
|------------|------------------|
| Hooks | Yes |
| Skills | Yes |
| Plugins | Yes |
| Instructions | Yes |
| Config files | Yes |

---

## Phase 8: Cleanup & Consolidation

### Requirements
Delete/clean:
- `.enhance/`, `.goals/`, `.hermes_diagnostics/`, `.mcp/`, `.*_cache/`, `.worktrees/`
- `*.json`, `*.log`, `*.txt` temp files in root
- Convert `*.mjs` → `*.mts`
- Update `package.json`, `tsconfig.json`, `pyproject.toml`, `requirements.txt`

### Acceptance Criteria
| Check | Expected |
|-------|----------|
| Temp dirs removed | 0 temp dirs remain |
| Temp files removed | 0 temp files remain |
| mjs→mts | All converted |
| Configs updated | All current |

---

## Phase 9: Config/Scripts Sync

### Requirements
- Sync `.env` across profiles (use `hermes config set` only)
- Sync `config.yaml` via CLI
- Sync `quick_commands.json`
- Verify all 7 profiles consistent

### Acceptance Criteria
| Config | Synced? |
|--------|---------|
| .env | Yes |
| config.yaml | Yes |
| quick_commands.json | Yes |
| All 7 profiles | Yes |

---

## Phase 10: Git Push (3 Branches)

### Requirements
- Commit to `clean-development`
- Push to `origin/clean-development`
- Verify `development` branch
- Verify `production` branch
- Tag release

### Acceptance Criteria
| Branch | Pushed? |
|--------|---------|
| clean-development | Yes |
| development | Yes |
| production | Yes |
| Tag | Created |

---

## Phase 11: Judge Scores ≥ 99

### Requirements
Run all 7 judges on relevant artifacts:
- `plans-judge` on `.hermes/plans/*.md`
- `specs-judge` on `.hermes/specs/*.md`
- `prompts-judge` on `.github/prompts/**/*.prompt.md`
- `skill-judge` on all skills
- `hooks-judge` on hooks
- `plugins-judge` on plugins
- `scripts-judge` on `scripts/`

### Acceptance Criteria
| Judge | Score ≥ 99? |
|-------|-------------|
| plans-judge | Yes |
| specs-judge | Yes |
| prompts-judge | Yes |
| skill-judge | Yes |
| hooks-judge | Yes |
| plugins-judge | Yes |
| scripts-judge | Yes |

---

## Cross-Phase Dependencies

| Phase | Depends On |
|-------|------------|
| 6 | 5 (doctor must pass) |
| 7 | 5 (profiles must work) |
| 8 | 5 (clean workspace) |
| 9 | 5, 8 (configs after cleanup) |
| 10 | 9 (configs synced) |
| 11 | All prior (artifacts must exist) |

---

## Verification Scripts

```bash
# Phase 5
python scripts/verify_phase5.py

# Phase 6
python scripts/verify_phase6.py

# Phase 7
python scripts/verify_phase7.py

# Phase 8
python scripts/verify_phase8.py

# Phase 9
python scripts/verify_phase9.py

# Phase 10
python scripts/verify_phase10.py

# Phase 11
python scripts/verify_all_judges.py
```