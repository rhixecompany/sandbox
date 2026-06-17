# 2026-06-16 Ecosystem Audit & Enhancement Plan

## Goal
Comprehensive audit, enhancement, and verification of the entire Hermes Agent local ecosystem: skills, profiles, context files, markdown artifacts, and system health.

## Scope
| Area | Path | Items |
|------|------|-------|
| Local skills | `C:\Users\Alexa\AppData\Local\hermes\skills\` | 352 SKILL.md files |
| Profiles | `C:\Users\Alexa\AppData\Local\hermes\profiles\` | 7 profiles |
| Context files | `C:\Users\Alexa\Desktop\SandBox\` | AGENTS.md, .hermes.md, PLAN.md, SESSION_REPORT.md |
| Docs | `C:\Users\Alexa\Desktop\SandBox\docs\` | ~1,267 markdown files |
| Root MD files | `C:\Users\Alexa\Desktop\SandBox\` | 38 markdown files |
| Global SOUL/MEMORY | `C:\Users\Alexa\AppData\Local\hermes\` | SOUL.md, MEMORY.md |

## Constraints
- **Strict sequential**: Each phase must complete before the next begins ("only then" rule)
- **Conservative**: Read before edit, backup before destructive ops
- **DRY**: No cross-file duplication; reference, don't copy
- **Verification**: Every change verified on disk before claiming success

---

## Phase 1: Skill-Judge All Local Skills (Score ≥80 Gate)

### 1.1 — Inventory & Batch Audit
- **Action**: Run skill-judge across all 352 local skills in batches of 7
- **Output**: `judge_results/batch_001_results.md` through final batch
- **Scoring**: Use skill-judge v1.1.0 — 5 dimensions, 100 pts max
- **Gate**: Identify all skills scoring <80

### 1.2 — Categorize Failures
| Category | Score Range | Action |
|----------|-------------|--------|
| 🔴 Rewrite | <40 | Full rewrite needed |
| ⚠️ Major fix | 40-59 | Content depth + structure |
| 🔧 Minor fix | 60-79 | Frontmatter, references, pitfalls |

### 1.3 — Remediate Below-Threshold Skills
- **Priority order**: Rewrite → Major fix → Minor fix
- **Fix template per skill**:
  1. Add missing frontmatter fields (name, title, description, version, author, license, tags)
  2. Add Skills Required table
  3. Add phased workflow (≥3 phases)
  4. Add Pitfalls section
  5. Add Verification Checklist
  6. Create reference files (references/, templates/, scripts/) where applicable
  7. Move content >250 lines to reference files
- **Verification**: Re-judge each patched skill; confirm score ≥80

### 1.4 — Planning Skills Special Check
**Skills**: `brainstorming`, `plans-and-specs`, `prompt-planning-orchestration`
**Required elements**:
- [ ] Goals clearly stated
- [ ] Subgoals/phases decomposed
- [ ] Personas defined (who uses this skill)
- [ ] Personality/tone guidance
- [ ] Profile selection guidance (which profile to use)
- [ ] Reference files: references/, templates/, scripts/ as needed
- [ ] Optional vs required vs suggested references clearly labeled

**Current gaps**:
- `brainstorming`: No Skills Required table, no pitfalls, no verification checklist
- `plans-and-specs`: No Skills Required table, no pitfalls section, 289 lines (over limit)
- `prompt-planning-orchestration`: Has structure but no Skills Required table, no reference files

### 1.5 — Reference Files Audit
- **Action**: For each skill, verify all cited reference files exist and are substantive (>3 lines)
- **Create missing**: references/, templates/, scripts/ as needed
- **Delete orphaned**: Reference files not cited by any SKILL.md

---

## Phase 2: Clean Stale/Invalid/Unused Markdown Files

### 2.1 — Catalog All Markdown Files
- **Root**: `C:\Users\Alexa\Desktop\SandBox\*.md` (38 files)
- **Docs**: `C:\Users\Alexa\Desktop\SandBox\docs\*.md` (~1,267 files)

### 2.2 — Classify Each File
| Category | Criteria | Action |
|----------|----------|--------|
| **Active** | Referenced by AGENTS.md, .hermes.md, or a skill | Keep |
| **Stale** | Not referenced, outdated content, superseded | Delete |
| **Invalid** | Malformed, empty, broken frontmatter | Delete |
| **Unused** | No inbound references, no unique content | Delete |
| **Reference** | Referenced by planning/execution skills | Keep |

### 2.3 — Specific Candidates for Deletion
**Root-level** (review first):
- `HERMES_PROFILE_REPORT.md` — superseded by hermes-profiles skill
- `HERMES_SYNC_REPORT.md` — superseded
- `judge_batch_*.md` (28 files) — audit artifacts, superseded by final report
- `remediation_verification_2026-06-14.md` — superseded
- `skills_audit_final_report.md` — superseded by new audit
- `sample.prompt.md` — unclear purpose
- `su.md` — unclear purpose

**Docs-level** (review first):
- All `*-context.md` files (100+ files) — session artifacts, not reference docs
- All `*-fix-issues-context.md`, `*-verify-context.md` — session artifacts
- All `*-complete*.md`, `*-completion*.md` — session reports
- All `phase*-*.md` — phase logs from prior sessions
- All `batch*-*.md` — batch audit artifacts
- `skills-debug-context.md` in skill subdirs — debug artifacts
- `dev-init-*` files — prior session artifacts
- `bash-scripts-*` files — prior session artifacts
- `prompt-builder-*` files — prior session artifacts
- `context-map-*` files — prior session artifacts
- `enhance-markdown-*` files — prior session artifacts
- `boost-prompt-*` files — prior session artifacts
- `ai-prompt-engineering-safety-review-*` files — prior session artifacts

### 2.4 — Execute Deletion
- **Preview**: List all files to delete, grouped by category
- **Confirm**: User approval required before any deletion
- **Execute**: Delete in batches, verify after each batch
- **Document**: Record deleted files in plan log

---

## Phase 3: Debug, Enhance & Verify AGENTS.md and .hermes.md

### 3.1 — AGENTS.md Audit
**File**: `C:\Users\Alexa\Desktop\SandBox\AGENTS.md`
**Check**:
- [ ] Session start rule present and correct
- [ ] MCP preference rule present
- [ ] Profile selection table complete (7 profiles)
- [ ] Python scripts rule present
- [ ] Structure matches project conventions
- [ ] No stale references
- [ ] SESSION_REPORT.md rolling summary rule present

**Enhancements needed**:
- Add reference to new audit plan
- Verify all 15+ subproject AGENTS.md files still exist and are unique

### 3.2 — .hermes.md Audit
**File**: `C:\Users\Alexa\Desktop\SandBox\.hermes.md`
**Check**:
- [ ] Profile table complete and accurate
- [ ] MCP servers list matches actual config
- [ ] Hooks list matches actual hooks
- [ ] Plugins list matches actual plugins
- [ ] Verification gates present
- [ ] Strict Rules section present
- [ ] No DRY violations with AGENTS.md

**Enhancements needed**:
- Verify MCP server list against `hermes config check`
- Verify hooks against `C:\Users\Alexa\AppData\Local\hermes\hooks\`
- Verify plugins against config.yaml

---

## Phase 4: Hermes Profiles — Create, Enhance, Debug, Verify

### 4.1 — Profile Inventory
| Profile | SOUL.md | USER.md | MEMORY.md | Status |
|---------|---------|---------|-----------|--------|
| default | ✅ | ✅ (586B) | ✅ (586B) | Enhance USER.md |
| code-architect | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |
| adminbot | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |
| creative-director | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |
| exec-assistant | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |
| patient-tutor | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |
| research-analyst | ✅ | ⚠️ (133B, minimal) | ✅ | Enhance USER.md |

### 4.2 — Enhance Minimal USER.md Files
**Problem**: 6 profiles have identical 133-byte USER.md (single preference line). Need profile-specific identity + model info.

**Enhance each with**:
- Identity section (Name, OS, Shell)
- Active Model & Providers (profile-specific)
- Execution Preferences (profile-specific additions)
- Reference to SOUL.md

**Priority**: default and code-architect first (most-used profiles)

### 4.3 — Enhance SOUL.md Files
**Check each profile SOUL.md for**:
- [ ] Profile identity section present
- [ ] Parent SOUL.md reference present
- [ ] Profile-specific rules present
- [ ] DRY compliance (no duplication of parent standards)
- [ ] Line count ≤25 (minimal profile SOUL.md pattern)

**Current state**: All 6 non-default profiles already follow the minimal pattern ✅

### 4.4 — Verify Profile Configs
- [ ] `hermes config check` passes
- [ ] All profiles have valid config.yaml
- [ ] Provider chain correct per profile
- [ ] Skills synced across profiles

---

## Phase 5: Provider Enumeration

### 5.1 — Cross-Reference 4 Sources
1. **Active provider**: `grep -A 3 "^model:" ~/.hermes/config.yaml`
2. **Defined provider blocks**: `grep -A 2 "^  [a-z]" ~/.hermes/config.yaml`
3. **Env credential keys**: `grep -oP '^[A-Z_]+_KEY[^=]*' ~/.hermes/.env`
4. **Fallback chain**: `grep -A 10 "^fallback_providers:" ~/.hermes/config.yaml`

### 5.2 — Assembly Table
| Provider | Where Defined | Env Key | Key Present | Role |
|----------|---------------|---------|-------------|------|
| (populate from actual config) | | | | |

### 5.3 — Verify
- [ ] All providers have valid credentials
- [ ] Fallback chain is correct
- [ ] No stale/orphaned provider blocks

---

## Phase 6: System Maintenance

### 6.1 — Disk Health
```bash
df -h /c/Users/Alexa | tail -1
du -sh /c/Users/Alexa/AppData/Local/hermes/{logs,sessions,checkpoints,skills}
```

### 6.2 — Memory Health
```bash
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md  # <2200
wc -c /c/Users/Alexa/AppData/Local/hermes/profiles/*/memories/USER.md  # <1375 each
```

### 6.3 — Log Analysis
- Check errors.log for: initial connection failed, connection lost, Out of diskspace, 429, 402/401
- Rotate/truncate if needed

### 6.4 — MCP Server Health
- Verify all 10 MCP servers reachable
- Check for stale connections

### 6.5 — Hermes Version
- Current: v0.16.0 (2026.6.5)
- Update available: 2 commits behind
- **Action**: `uv pip install --upgrade hermes-agent` (after backup)

---

## Phase 7: Hermes Tools

### 7.1 — Toolset Inventory
```bash
hermes tools list
```

### 7.2 — Verify Core Toolsets Enabled
| Toolset | Expected |
|---------|----------|
| web | ✅ |
| terminal | ✅ |
| file | ✅ |
| skills | ✅ |
| memory | ✅ |
| delegation | ✅ |
| cronjob | ✅ |
| browser | ✅ |
| vision | ✅ |

---

## Phase 8: Operator Policy

### 8.1 — Verify Backup Protocol
- Config edits: `cp config.yaml config.yaml.$(date +%s)` before changes
- Memory edits: handled by `memory` tool internally
- Destructive ops: `git status`, `git stash list` first

### 8.2 — Verify Validation Protocol
- Config: `hermes config check`
- Memories: `scripts/validate_memories.py`
- YAML: `python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"`

### 8.3 — Verify Deletion Protocol
- Never delete skills/plugins/hooks without `absorbed_into` or explicit confirmation
- Cron jobs: `hermes cron remove <id>` (never guess IDs)
- Sessions: `hermes sessions prune --older-than 30`

---

## Phase 9: Personality Enhance & Verify

### 9.1 — Global SOUL.md
**File**: `C:\Users\Alexa\AppData\Local\hermes\SOUL.md`
**Check**:
- [ ] Identity & tone clear (OWL persona)
- [ ] 5 core rules present
- [ ] File operations section present
- [ ] Code quality standards present
- [ ] Response style DO/DON'T present
- [ ] Security DO/DON'T present
- [ ] Workspace paths correct

### 9.2 — Per-Profile Personality
- [ ] default: Pragmatic senior engineer (OWL)
- [ ] code-architect: TDD-first engineer
- [ ] adminbot: Systems administrator
- [ ] creative-director: Creative director
- [ ] exec-assistant: Executive assistant
- [ ] patient-tutor: Patient tutor
- [ ] research-analyst: Research analyst

---

## Phase 10: Context Files Enhance & Verify

### 10.1 — Priority Order Verification
1. `.hermes.md` → highest priority
2. `AGENTS.md` → repo instructions
3. `~/.hermes/profiles/<name>/SOUL.md` → profile standards
4. `~/.hermes/SOUL.md` → global standards
5. `USER.md` → profile state
6. `MEMORY.md` → learned facts

### 10.2 — Cross-Reference Check
- [ ] .hermes.md references AGENTS.md
- [ ] AGENTS.md references SESSION_REPORT.md
- [ ] Profile SOUL.md files reference parent SOUL.md
- [ ] No circular references

---

## Phase 11: Validate Memories Enhance & Verify

### 11.1 — Global MEMORY.md
**File**: `C:\Users\Alexa\AppData\Local\hermes\memories\MEMORY.md`
**Current**: 4 entries, 589/2200 chars ✅
**Check**:
- [ ] All entries still relevant
- [ ] No stale facts
- [ ] Under 2200 char limit

### 11.2 — Per-Profile MEMORY.md
- [ ] Each profile has MEMORY.md
- [ ] No cross-profile duplication
- [ ] All under limits

### 11.3 — validate-memories Skill
- [ ] Skill exists and is current
- [ ] Script `scripts/validate_memories.py` exists and runs
- [ ] Schema checks pass for all USER.md and MEMORY.md files

---

## Phase 12: Profile Consolidation Enhance & Verify

### 12.1 — DRY Violation Check
- [ ] No duplicate content between USER.md and SOUL.md
- [ ] No duplicate content between profile SOUL.md and parent SOUL.md
- [ ] No duplicate content between AGENTS.md and .hermes.md
- [ ] Cross-references used instead of copies

### 12.2 — Profile SOUL.md Consolidation
- [ ] Each profile SOUL.md ≤25 lines
- [ ] Each references parent SOUL.md
- [ ] No duplicated standards from parent

### 12.3 — USER.md Consolidation
- [ ] Each profile has unique USER.md (not just copies)
- [ ] default profile USER.md created (currently missing)
- [ ] code-architect USER.md created (currently missing)

---

## Phase 13: DRY Violation Sweep

### 13.1 — Cross-File Duplication Scan
- Compare AGENTS.md vs .hermes.md for overlapping content
- Compare profile SOUL.md files vs parent SOUL.md
- Compare USER.md files across profiles
- Compare MEMORY.md files across profiles

### 13.2 — Fix Violations
- Replace duplicated content with cross-references
- Ensure one source of truth per fact/convention

---

## Phase 14: Session End Capture

### 14.1 — Update SESSION_REPORT.md
- Add current session entry
- Maintain rolling 5-session summary
- Document all changes made

### 14.2 — Update Plan Status
- Mark all phases complete
- Document final scores and metrics
- Record any remaining issues

### 14.3 — Git Commit
- Commit all changes with descriptive message
- Tag if appropriate

---

## Verification Gates (End of Each Phase)

- [ ] All tool outputs reviewed
- [ ] No errors in logs
- [ ] Files verified on disk (not via cache)
- [ ] Scores recorded and meet thresholds
- [ ] User notified of blockers

## Final Verification (End of All Phases)

- [ ] All skills score ≥80
- [ ] All profiles have SOUL.md + USER.md + MEMORY.md
- [ ] AGENTS.md and .hermes.md enhanced and verified
- [ ] Stale markdown files deleted
- [ ] Provider enumeration complete
- [ ] System maintenance healthy
- [ ] DRY violations resolved
- [ ] Session end captured

---

## Estimated Effort

| Phase | Estimated Time | Complexity |
|-------|---------------|------------|
| 1: Skill-judge all skills | 4-6 hours | High (352 skills) |
| 2: Clean markdown files | 1-2 hours | Medium |
| 3: AGENTS.md + .hermes.md | 30 min | Low |
| 4: Profiles | 1 hour | Medium |
| 5: Provider enumeration | 30 min | Low |
| 6: System maintenance | 30 min | Low |
| 7: Hermes tools | 15 min | Low |
| 8: Operator policy | 15 min | Low |
| 9: Personality | 30 min | Low |
| 10: Context files | 30 min | Low |
| 11: Validate memories | 30 min | Low |
| 12: Profile consolidation | 1 hour | Medium |
| 13: DRY sweep | 1 hour | Medium |
| 14: Session end capture | 15 min | Low |
| **Total** | **~12-16 hours** | |

## Files That Will Be Created/Modified

| File | Action |
|------|--------|
| `C:\Users\Alexa\AppData\Local\hermes\profiles\*\memories\USER.md` (6 profiles) | Enhance |
| `C:\Users\Alexa\AppData\Local\hermes\skills\planning\*\SKILL.md` | Enhance |
| `C:\Users\Alexa\AppData\Local\hermes\skills\*\SKILL.md` (below-threshold) | Enhance |
| `C:\Users\Alexa\Desktop\SandBox\AGENTS.md` | Enhance |
| `C:\Users\Alexa\Desktop\SandBox\.hermes.md` | Enhance |
| `C:\Users\Alexa\Desktop\SandBox\SESSION_REPORT.md` | Update |
| `C:\Users\Alexa\Desktop\SandBox\docs\*` (stale files) | Delete |
| `C:\Users\Alexa\Desktop\SandBox\*.md` (stale root files) | Delete |
| `judge_results\batch_*_results.md` | Create |
| `.hermes/plans/2026-06-16_eco-system-audit-plan.md` | Create (this file) |

---

**Plan created**: 2026-06-16
**Profile**: default
**Model**: gpt-5.4-mini (openai-codex)
**Status**: Awaiting user approval to execute
