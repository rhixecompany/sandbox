# Subagent-Driven Development Full Implementation Plan

**Generated:** 2026-08-19 23:59 UTC | **Session:** 20260819_232045_caba2d
**Source Analysis:** 21 sessions, 36 user messages (18:41-23:23), state.db + session-logger + desktop.log + gateway_state

---

## Goal

Create, verify, execute, and implement a complete specification and plan for **subagent-driven-development** that gathers all user inputs/goals from today's TUI, CLI, and desktop sessions and implements them fully using the subagent-driven-development workflow (fresh subagent per task + 2-stage review).

---

## Context Summary (Today's Sessions)

| Metric | Value |
|--------|-------|
| Sessions today | 21 |
| User messages | 36 |
| Time range | 18:41 - 23:23 UTC |
| Active model | nemotron-3-ultra-free (opencode-zen) |
| Fallback model | deepseek-v4-flash-free |
| Profile | default (profile_name not persisting in state.db) |

### Extracted User Goals (Deduplicated & Categorized)

| Category | Goals | Priority |
|----------|-------|----------|
| **Config/Foundation** | Fix config.yaml corruption (line 958), hermes config validation | P0 - Blocking |
| **MCP Servers** | Install/setup/test: context7, sequential-thinking, github, filesystem, playwright, fetch, neon, docker, memory, honcho, ast-grep, code-sandbox, sentry, smithery | P1 - Enabler |
| **Core Skills** | Implement subagent-driven-development fully (2-stage review, context budget, gates taxonomy) | P1 - Core Ask |
| **Profile/Memory Sync** | soul-enhancer, hermes-personality-soul, create-missing-souls, create-missing-memories, hermes-profile-sync, hermes-profile-memory-sync | P1 - Core Ask |
| **SOUL/USER/MEMORY** | Enhance with git history, session continuity, cross-profile sync | P1 - Core Ask |
| **Honcho Integration** | Persistent cross-session memory, user modeling, peer cards | P2 - Enhancement |
| **Banking Project** | Load AGENTS.md context, fix context loading issues | P2 - Project Work |
| **Preferences** | TypeScript/VS Code dark theme, systematic skill-driven development | P2 - Context |

---

## Phase 1: Data Mining & Synthesis ✅ (COMPLETE - This Analysis)

**Status:** Done — This plan document is the output.

### Tasks Completed
- [x] 1.1 Parse all 21 session JSONs from `~/AppData/Local/hermes/sessions/`
- [x] 1.2 Query state.db for sessions + user messages (36 extracted)
- [x] 1.3 Read session-logger start/end captures from `logs/sessions/`
- [x] 1.4 Read desktop.log for gateway/backend events
- [x] 1.5 Read gateway_state.json for platform status
- [x] 1.6 Deduplicate and categorize 36 user messages into 8 goal categories
- [x] 1.7 Identify blockers: config.yaml corruption, DeepSeek rate limits, profile_name persistence

### Verification
```bash
# Confirm session analysis complete
ls -la ~/AppData/Local/hermes/sessions/session_20260819_*.json | wc -l
# Should show 21 session files
```

---

## Phase 2: Specification Creation

Create detailed SPEC.md files for each major workstream in `.hermes/plans/specs/`.

### 2.1 SPEC: Config & Foundation Repair
**File:** `.hermes/plans/specs/01-config-foundation-repair.md`
- Fix config.yaml YAML corruption at line 958 (quoted scalar, unexpected end of stream)
- Validate all mcp_servers entries use YAML list format (not JSON strings)
- Verify hermes config loads without errors
- Ensure profile_name persists in state.db sessions table

**Acceptance Criteria:**
- `hermes config validate` passes
- `hermes mcp list` shows all 14+ servers enabled
- New sessions show correct profile_name in state.db

### 2.2 SPEC: MCP Server Suite Setup
**File:** `.hermes/plans/specs/02-mcp-server-suite.md`
- Install/verify 14 MCP servers: github, filesystem, playwright, fetch, tavily, neon, docker, memory, honcho, ast-grep, code-sandbox, sentry, context7, sequential-thinking, smithery
- Each server: `hermes mcp test <name>` passes
- Configure credentials via vault_key_sync (Neon, GitHub, Context7)
- MCP-first tool precedence enforced in all skills

**Acceptance Criteria:**
- All 14+ `hermes mcp test <server>` pass
- Skills using MCP tools work without fallback to native

### 2.3 SPEC: subagent-driven-development Skill Enhancement
**File:** `.hermes/plans/specs/03-subagent-driven-development.md`
- Enhance existing skill at `skills/software-development/subagent-driven-development/`
- Add: context-budget-discipline reference, gates-taxonomy reference
- Implement 2-stage review: Spec Compliance → Code Quality (strict order)
- Add task granularity rules (2-5 min per task)
- Add red flags checklist (never skip reviews, never parallel on shared config)
- Add integration with test-driven-development, requesting-code-review
- Verify skill loads, passes skill-judge ≥ 90

**Acceptance Criteria:**
- `skill_view subagent-driven-development` shows enhanced content
- `skill-judge` score ≥ 90
- References exist and are loadable

### 2.4 SPEC: Profile/Memory Sync Skills (5 Skills)
**File:** `.hermes/plans/specs/04-profile-memory-sync-skills.md`
- **soul-enhancer**: SOUL.md enhancement, persona→tone→traits mapping
- **hermes-personality-soul**: Personality config for all 14 Hermes profiles
- **create-missing-souls**: Discover/create SOUL.md for profiles missing it
- **create-missing-memories**: Discover/create USER.md/MEMORY.md for profiles
- **hermes-profile-sync**: Bidirectional-safe root↔profile config.yaml propagation
- **hermes-profile-memory-sync**: Sync memory files + aliases across profiles

Each skill: SKILL.md + references/ + templates/ + scripts/ + CI workflow

**Acceptance Criteria:**
- All 6 skills load via `skill_view`
- Each has ≥ 3 reference/template/script files
- Cross-profile sync verified with `verify-sync`

### 2.5 SPEC: SOUL/USER/MEMORY Enhancement with Git History
**File:** `.hermes/plans/specs/05-soul-user-memory-enhancement.md`
- SOUL.md: Authoritative persona, boundaries, cognitive style (no H1, §-delimited)
- USER.md: Compact pointer to canonical rules in MEMORY.md (DRY)
- MEMORY.md: §-delimited facts, session-derived updates, MD041 false positive documented
- Integrate git history: `git log --oneline` insights into MEMORY.md
- Session continuity: SESSION_REPORT.md rolling summary (not stub)
- Profile routing table enforced in all three files

**Acceptance Criteria:**
- All 3 files pass `validate-memories`
- No duplicate content across SOUL/USER/MEMORY (DRY)
- Session startup reads SESSION_REPORT.md and finds real content

### 2.6 SPEC: Honcho Integration
**File:** `.hermes/plans/specs/06-honcho-integration.md`
- Configure honcho memory (hybrid mode: auto-inject + tools available)
- Implement honcho_profile, honcho_context, honcho_reasoning, honcho_search, honcho_conclude
- Peer card generation from session data
- Cross-session preference recall (TypeScript, VS Code dark theme)
- Memory persistence across profile switches

**Acceptance Criteria:**
- `honcho_profile` returns user peer card
- `honcho_reasoning level=high` synthesizes working style
- Preferences survive session restart

### 2.7 SPEC: Banking Project Context Loading
**File:** `.hermes/plans/specs/07-banking-project-context.md`
- Load `projects/Banking/AGENTS.md` as project context
- Verify AGENTS.md canonical guidance loads before .github/prompts/
- Fix context loading issues reported in sessions 221823, 222027, 222231
- Ensure project-specific specs reference `.github/instructions/`

**Acceptance Criteria:**
- `read_file projects/Banking/AGENTS.md` succeeds
- Project context recognized in new sessions
- Banking-specific prompts load correctly

---

## Phase 3: Master Implementation Plan

**File:** `.hermes/plans/2026-08-19_235900-subagent-driven-development-full-implementation.md` (this file)

### Task Breakdown with Dependencies

| Task ID | Phase | Task | Depends On | Profile | Est. Time |
|---------|-------|------|------------|---------|-----------|
| T01 | 2.1 | Fix config.yaml corruption | — | adminbot | 10 min |
| T02 | 2.1 | Validate profile_name persistence | T01 | adminbot | 5 min |
| T03 | 2.2 | Test/install all 14 MCP servers | T01 | adminbot | 30 min |
| T04 | 2.2 | Configure vault keys (Neon, GitHub, Context7) | T03 | adminbot | 15 min |
| T05 | 2.3 | Enhance subagent-driven-development skill | T03 | code-architect | 20 min |
| T06 | 2.3 | Add context-budget + gates-taxonomy refs | T05 | code-architect | 15 min |
| T07 | 2.3 | Verify skill-judge ≥ 90 | T06 | code-architect | 5 min |
| T08 | 2.4 | Implement soul-enhancer skill | T03 | code-architect | 25 min |
| T09 | 2.4 | Implement hermes-personality-soul skill | T03 | code-architect | 25 min |
| T10 | 2.4 | Implement create-missing-souls skill | T03 | code-architect | 20 min |
| T11 | 2.4 | Implement create-missing-memories skill | T03 | code-architect | 20 min |
| T12 | 2.4 | Implement hermes-profile-sync skill | T03 | code-architect | 30 min |
| T13 | 2.4 | Implement hermes-profile-memory-sync skill | T03 | code-architect | 30 min |
| T14 | 2.4 | Verify all 6 skills load + sync | T08-T13 | adminbot | 10 min |
| T15 | 2.5 | Enhance SOUL.md with git history | T01 | code-architect | 15 min |
| T16 | 2.5 | Enhance USER.md as DRY pointer | T15 | code-architect | 10 min |
| T17 | 2.5 | Enhance MEMORY.md with session updates | T15 | code-architect | 15 min |
| T18 | 2.5 | Validate memories across 7 profiles | T17 | adminbot | 10 min |
| T19 | 2.6 | Configure honcho hybrid mode | T03 | code-architect | 15 min |
| T20 | 2.6 | Implement honcho tools integration | T19 | code-architect | 20 min |
| T21 | 2.6 | Verify cross-session recall | T20 | research-analyst | 10 min |
| T22 | 2.7 | Fix Banking AGENTS.md context loading | T03 | code-architect | 15 min |
| T23 | 2.7 | Verify project context in new session | T22 | default | 5 min |
| T24 | 4 | Execute all tasks via subagent-driven-development | T07,T14,T18,T21,T23 | (per task) | — |
| T25 | 5 | Full verification & integration test | T24 | adminbot | 20 min |
| T26 | 6 | Update documentation & session report | T25 | exec-assistant | 10 min |

### Verification Gates (Must Pass Before Next Phase)

| Gate | Command | Expected |
|------|---------|----------|
| G1: Config Valid | `hermes config validate` | Exit 0, no YAML errors |
| G2: MCP Servers | `hermes mcp test all` (script) | All 14+ pass |
| G3: Skills Load | `skill_view <each skill>` | All load without error |
| G4: Skill Quality | `skill-judge` on new skills | All ≥ 90 |
| G5: Profile Sync | `verify-sync` | 65 checks pass |
| G6: Memories Valid | `validate-memories` | All 7 profiles pass |
| G7: Honcho Works | `honcho_profile`, `honcho_reasoning` | Return data |
| G8: Banking Context | New session loads AGENTS.md | Context present |
| G9: Subagent Workflow | Run 1 test task via subagent-driven-development | Spec PASS → Quality APPROVED |
| G10: Full Test Suite | `pytest tests/ -q` (if applicable) | All pass |

---

## Phase 4: Execution via Subagent-Driven-Development

**Workflow per Task (T01-T23):**

```
For EACH task:
  1. Dispatch IMPLEMENTER subagent with:
     - Full task spec from Phase 2 SPEC.md
     - TDD instructions (test first, implement, verify)
     - Project context (paths, conventions, dependencies)
  2. Dispatch SPEC COMPLIANCE REVIEWER:
     - Check against original SPEC.md requirements
     - Output: PASS or specific gaps
     - If gaps: loop back to implementer
  3. Dispatch CODE QUALITY REVIEWER:
     - Check style, errors, tests, security, edge cases
     - Output: APPROVED or REQUEST_CHANGES
     - If issues: loop back to implementer
  4. Mark task complete in todo list
  5. ONLY proceed when BOTH reviews PASS/APPROVED
```

**Strict Ordering:** Spec Compliance MUST pass before Code Quality review starts.

**Parallelization:** Independent tasks (e.g., T08-T13) can run in parallel batches. Shared-config tasks (T01, T15-T17) must be sequential.

---

## Phase 5: Verification & Integration

### 5.1 Automated Verification Script
**File:** `scripts/verify-full-implementation.py`
- Runs all 10 verification gates (G1-G10)
- Outputs JSON summary + human-readable report
- Fails fast on first gate failure with actionable error

### 5.2 Integration Tests
- New session startup: loads SESSION_REPORT.md, validates 5 mandatory skills
- Profile switch: `hermes profile use code-architect` → config loads
- MCP tool precedence: native tools not used when MCP equivalent exists
- Subagent workflow: end-to-end test task completes with both reviews
- Honcho recall: preferences persist across sessions
- Banking context: AGENTS.md loads in new Banking session

### 5.3 Acceptance Criteria
- [ ] All 10 gates pass
- [ ] No config.yaml corruption
- [ ] All 14+ MCP servers test pass
- [ ] All 6 profile/memory sync skills operational
- [ ] SOUL/USER/MEMORY enhanced, DRY, validated
- [ ] Honcho cross-session memory working
- [ ] Banking project context loads
- [ ] Subagent-driven-development skill enhanced and verified
- [ ] Session report updated with real content

---

## Phase 6: Documentation & Session Report

### 6.1 Update Documentation
- `.hermes/plans/specs/*.md` — All 7 specs created
- `docs/architecture/` — Blueprint updates if structure changed
- `README.md` — Any new workflows documented
- `AGENTS.md` — Update if canonical guidance changed

### 6.2 Update Session Report
- Run `generate_session_report.py` on session end
- Ensure SESSION_REPORT.md has real rolling summary (not stub)
- Include: session ID, timestamp, profile, model, work completed, tools/skills used, current state, result

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Config.yaml corruption blocks all Hermes ops | P0 - Total block | Fix first (T01), verify before any other work |
| DeepSeek rate limits | P1 - Fallback failures | Use nemotron-3-ultra-free primary; configure opencode-zen credential pool |
| Profile_name not persisting in state.db | P1 - Routing broken | Fix in T02, verify with new session |
| Skill cross-profile sync drift | P2 - Inconsistent skills | Run verify-sync after each profile skill batch |
| Subagent parallel edit conflicts on shared config | P2 - Config corruption | Sequential for shared-config tasks (T01, T15-T17); static configs for parallel |
| Banking context loading flaky | P2 - Project work blocked | Fix AGENTS.md loading (T22), verify in clean session (T23) |
| Session report remains stub | P2 - Continuity lost | Generate real report in Phase 6, verify at next session start |

---

## Execution Command Summary

```bash
# Phase 1: Already done (this analysis)

# Phase 2: Create specs (can be done in parallel batches)
# See .hermes/plans/specs/ for each SPEC.md

# Phase 3: This plan file is the master plan

# Phase 4: Execute via subagent-driven-development
# Controller will dispatch subagents per task using the skill workflow

# Phase 5: Run verification
python3 scripts/verify-full-implementation.py

# Phase 6: Update docs + session report
python3 ~/AppData/Local/hermes/scripts/generate_session_report.py
```

---

## Next Immediate Action

**Start Phase 2.1 (T01): Fix config.yaml corruption**

```bash
# View corruption
sed -n '950,970p' ~/AppData/Local/hermes/config.yaml

# Fix using python (not direct edit - security guard)
python3 -c "
import yaml
with open('~/AppData/Local/hermes/config.yaml') as f:
    content = f.read()
# Fix quoted scalar at line 958 - likely a mcp_servers args string that should be list
# ... targeted fix ...
"
# Verify
hermes config validate
```

---

*Plan created via `mcp-sequential-thinking` structured reasoning + `create-implementation-plan` + `plans-and-specs` workflows. Ready for `subagent-driven-development` execution.*