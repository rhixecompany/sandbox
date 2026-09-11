---
goal: Execute 4 sequential goals: research-artifact generation (G1), skills dedupe/judge/fix (G2), free-model benchmark (G3), profile asset sync (G4)
version: 1.0
date_created: 2026-09-11
last_updated: 2026-09-11
owner: Alexa
status: 'Planned'
tags: [process, skills, models, research, sync, dedupe]
---

# Four-Goal Execution Master Plan

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

Sequential execution of 4 goals, each gated by verification before the next starts. Goals run in order G1 → G2 → G3 → G4 (user-confirmed sequencing).

## 1. Requirements & Constraints

- **REQ-001**: Keep existing `node-dependency.md`, `python-packages.md`, `technology-stacks.md` (user chose incremental; reports ~1h old)
- **REQ-002**: G1 research artifacts = ONE skill + ONE script + ONE verified test per research TOPIC dir (11 topics), plus ONE hook for the research folder (user-clarified breadth)
- **REQ-003**: Update `requirements.txt` last in G1 — union of `pip freeze` installed packages and packages documented in `python-packages.md`
- **REQ-004**: G2 dedupe = near-exact duplicates; keep best/canonical category-placed copy, enhance it, delete the rest (user-clarified aggressiveness)
- **REQ-005**: G2 must prove `initial-skills.txt` count > `updated-skills.txt` count
- **REQ-006**: G2 skills judge score target ≥ 90 on remaining skills
- **REQ-007**: G3 = list free/non-premium models from ALL 3 providers (opencode-zen, openrouter, nous) first, then benchmark via `hermes chat`; report which queries complete successfully (user-clarified scope)
- **REQ-008**: G4 = delete then copy sync of skills/hooks/plugins/scripts + config.yaml + .env from `~/AppData/Local/hermes` into every subdir of `~/AppData/Local/hermes/profiles` (explicit user approval for destructive ops granted)
- **SEC-001**: Never print/commit secrets from `.env` or config.yaml contents — copy files, don't read contents into output
- **SEC-002**: Git safety — SandBox repo untouched by G4 (targets only `~/AppData/Local/hermes/profiles/`, outside repo)
- **CON-001**: Strict sequential: "only then" constraints are hard ordering gates
- **CON-002**: All 4 goals execute inside one session; artifacts land in `.hermes/plans/`, `.hermes/specs/`, `prompts/`, `scripts/`, `skills/`, `hooks/`
- **CON-003**: Windows host; hermes home = `C:\Users\Alexa\AppData\Local\hermes`; bash (MSYS2) syntax for terminal
- **GUD-001**: Verify before claim — every phase ends with tool-backed evidence (file counts, test pass, command exit 0)
- **GUD-002**: DRY — cross-reference artifacts, never duplicate instructions across plan/spec/prompt
- **PAT-001**: Implementation-plan identifier discipline (TASK/REQ/GOAL declared once, referenced freely)
- **PAT-002**: Subagent fan-out for independent per-topic artifact creation (G1) and per-skill fixes (G2)

## 2. Implementation Steps

### Implementation Phase 1 — G1: Research artifacts + requirements.txt

- GOAL-001: Create/test/debug/fix/verify skills, scripts, hooks derived from research/ markdown (11 topics), update requirements.txt

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | Inventory research/ topic dirs + md files; map topic → skill name → script name | ✅ | 2026-09-11 |
| TASK-002 | Create 11 SKILL.md (frontmatter-compliant, ≤250 lines, references/ for detail) | ✅ | 2026-09-11 |
| TASK-003 | Create 11 scripts (one per topic; scripts/ dir; no inline scripts) | ✅ | 2026-09-11 |
| TASK-004 | Create 11 tests (pytest or shell assert per script; scripts run, exit 0) | ✅ | 2026-09-11 |
| TASK-005 | Create 1 research-folder hook (e.g., new-md watch/format gate) | ✅ | 2026-09-11 |
| TASK-006 | Run all tests; debug + fix failures (trace before fix) | ✅ | 2026-09-11 |
| TASK-007 | Update requirements.txt = union(pip freeze, python-packages.md); verify importable | ✅ | 2026-09-11 |
| TASK-008 | Gate: all 11 scripts tested green; requirements.txt valid (pip check) | ✅ | 2026-09-11 |

### Implementation Phase 2 — G2: Skills dedupe + judge + fix

- GOAL-002: Shrink + harden skill library: dedupe, judge ≥90, fix debts, prove count decreased

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-010 | Run `hermes skills list` → `initial-skills.txt`; record count | ✅ | 2026-09-11 |
| TASK-011 | Read initial-skills.txt; detect duplicates (name collisions across categories, near-exact bodies) | ✅ | 2026-09-11 |
| TASK-012 | For each dup: keep canonical category version, enhance (merge unique content), delete others | ✅ | 2026-09-11 |
| TASK-013 | Run skill-judge on remaining skills; collect scores | ✅ | 2026-09-11 |
| TASK-014 | systematic-debugging: fix all debts/bugs/issues/warnings; raise scores ≥90 | ✅ | 2026-09-11 |
| TASK-015 | Run `hermes skills list` → `updated-skills.txt`; verify initial count > updated count | ✅ | 2026-09-11 |
| TASK-016 | Debug/fix/verify ALL skills in `updated-skills.txt`, ascending order of `hermes skills list-modified` | ✅ | 2026-09-11 |
| TASK-017 | Subgoal: `hermes skills audit && hermes skills check && hermes skills update`; fix findings | ✅ | 2026-09-11 |
| TASK-018 | Gate: counts proven (initial > updated), audit/check clean or documented residual | ✅ | 2026-09-11 |

### Implementation Phase 3 — G3: Free-model benchmark

- GOAL-003: Enumerate free models across opencode-zen/openrouter/nous; benchmark latency/accuracy/context/capabilities/tools/vision; report success set

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-020 | Load test-providers-models skill workflow; list free/non-premium models per provider (opencode-zen first) | ✅ | 2026-09-11 |
| TASK-021 | Capture baseline: `hermes auth list`, `hermes models` (or provider equivalents) → model inventory table | ✅ | 2026-09-11 |
| TASK-022 | Run `hermes chat` queries per model: latency, accuracy (factual probe), context (long-input probe), capabilities, tools (function-call probe), vision (image probe where supported) | 🔄 | 2026-09-11 |
| TASK-023 | Record per-query status (success/timeout/error) to results/ benchmark md | | |
| TASK-024 | Gate: report which queries completed successfully; no fabricated results — only observed | | |

### Implementation Phase 4 — G4: Profile asset sync

- GOAL-004: Reset + propagate root hermes assets into every profile subdir

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-030 | Inventory `~/AppData/Local/hermes/profiles/*` (15 subdirs incl. `skills` anomaly — verify what it is first) | | |
| TASK-031 | Delete skills/hooks/plugins/scripts dirs + config.yaml + .env in each profile subdir | | |
| TASK-032 | Copy root `~/AppData/Local/hermes/{skills,hooks,plugins,scripts,config.yaml,.env}` into every profile subdir | | |
| TASK-033 | Verify parity: dir trees + file counts match root per profile; config.yaml valid YAML parse | | |
| TASK-034 | Gate: per-profile tree diff vs root = empty; report anomaly handling for profiles/skills | | |

## 3. Alternatives

- **ALT-001**: Regenerate G1 reports from scratch — rejected (reports 1h old, user chose incremental)
- **ALT-002**: Per-file (30) research artifacts — rejected (user chose 11 topic-level artifacts)
- **ALT-003**: Exact-name-only dedupe — rejected (user chose near-exact, keep canonical)
- **ALT-004**: Benchmark only 4 verified models — rejected (user chose full free model list across 3 providers)
- **ALT-005**: Parallel non-sequential execution of goals — rejected (user chose strict sequence)

## 4. Dependencies

- **DEP-001**: Existing reports node-dependency.md / python-packages.md / technology-stacks.md (G1 input)
- **DEP-002**: research/ 30 md files across 11 topic dirs (G1 input)
- **DEP-003**: 629 skill dirs under `~/AppData/Local/hermes/skills/` (G2 input)
- **DEP-004**: hermes CLI (`skills list`, `auth list`, `chat`) (G2/G3)
- **DEP-005**: test-providers-models + skill-judge + systematic-debugging skills (G2/G3 workflows)
- **DEP-006**: Root hermes assets = source of truth for G4 copy
- **DEP-007**: bash (MSYS2) + Python 3.11/3.13 (uv) for scripts/tests

## 5. Files

- **FILE-001**: `node-dependency.md` (exists — keep)
- **FILE-002**: `python-packages.md` (exists — keep; G1 input)
- **FILE-003**: `research/*/` (exists — source)
- **FILE-004**: `skills/` + `scripts/` + `hooks/` in SandBox (G1 outputs, 11+11+1)
- **FILE-005**: `requirements.txt` (G1 update)
- **FILE-006**: `initial-skills.txt` + `updated-skills.txt` (G2 evidence)
- **FILE-007**: `results/models-benchmark-2026-09-11.md` (G3 output)
- **FILE-008**: `~/AppData/Local/hermes/profiles/*` (G4 target, outside repo)
- **FILE-009**: `.hermes/specs/2026-09-11-four-goal-execution-spec.md` (this plan's spec)
- **FILE-010**: `prompts/2026-09-11-four-goal-execution.prompt.md` (executable prompt)

## 6. Testing

- **TEST-001**: 11 research-topic scripts each exit 0 with fixture input (G1)
- **TEST-002**: `pip check` passes on updated requirements.txt; top packages import (G1)
- **TEST-003**: skill-judge score ≥90 on judged skills (G2)
- **TEST-004**: count(initial-skills.txt) > count(updated-skills.txt) (G2)
- **TEST-005**: `hermes skills audit && hermes skills check` exit clean or residual documented (G2)
- **TEST-006**: Per-profile diff vs root empty for skills/hooks/plugins/scripts/config.yaml/.env (G4)
- **TEST-007**: G3: every reported query has observed success/failure evidence; zero fabricated rows

## 7. Risks & Assumptions

- **RISK-001**: Dedupe deletes content user wants — mitigation: enhance-then-delete order, gitable evidence list kept in results/
- **RISK-002**: G3 queries may cost time/rate-limits across providers — mitigation: bounded timeouts, fallback providers, report failures as observed
- **RISK-003**: G4 copying root config.yaml into profiles may overwrite profile-specific config — mitigation: user explicitly requested this sync; `.bak` NOT created per standing rule (git/state.db is rollback); anomaly `profiles/skills` inspected first
- **RISK-004**: Windows path/CRLF issues in scripts — mitigation: LF writes, native path style for native tools
- **ASSUMPTION-001**: User approval for all destructive ops is standing (granted in request)
- **ASSUMPTION-002**: hermes skills CLI subcommands exist as stated (`list`, `list-modified`, `audit`, `check`, `update`)
- **ASSUMPTION-003**: Provider model lists retrievable via `hermes auth list` / test-providers-models workflow

## 8. Related Specifications / Further Reading

- [Execution spec](.hermes/specs/2026-09-11-four-goal-execution-spec.md)
- [Executable prompt](prompts/2026-09-11-four-goal-execution.prompt.md)
- [test-providers-models skill](skills/) — loaded at G3 start
- [skill-judge skill](skills/qa/skill-judge) — loaded at G2 start
- [systematic-debugging skill](skills/software-development/systematic-debugging) — loaded at G2/G3 start