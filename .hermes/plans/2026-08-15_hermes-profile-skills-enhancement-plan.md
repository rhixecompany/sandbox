---
name: profile-skills-enhancement-plan
title: Hermes Profile Skills Enhancement — Implementation Plan
description: Phased task breakdown for enhancing existing and creating missing Hermes profile management skills
date: 2026-08-15
status: draft
---

# Hermes Profile Skills Enhancement — Implementation Plan

**Spec:** [2026-08-15_hermes-profile-skills-enhancement-spec.md](2026-08-15_hermes-profile-skills-enhancement-spec.md)
**Goal:** Enhance 3 existing profile skills, create 3 missing ones, build tools/hooks/quick commands, and update all referencing blocks.

---

## Phase 1: Foundation Tools (no dependencies)

### Task 1.1 — Create `profile_discover.py`

- **Action:** Write the profile discovery script to `~/AppData/Local/hermes/scripts/profile_discover.py`
- **Details:** Discovers all 14 profiles via `hermes profile list` subprocess (fallback to dir listing). Checks SOUL.md existence/size/header/identity. Checks memories/ dir and USER.md/MEMORY.md presence and sizes.
- **Estimate:** 30 min
- **Depends on:** nothing

### Task 1.2 — Create `soul_propagate.py`

- **Action:** Write the SOUL header propagation script to `~/AppData/Local/hermes/scripts/soul_propagate.py`
- **Details:** Reads root SOUL.md, discovers profiles, fixes `**Profile:**` headers and adds `**Identity:**` lines. Supports `--dry-run` and `--profile <name>`.
- **Estimate:** 45 min
- **Depends on:** 1.1 (uses same discovery logic)

### Task 1.3 — Verify foundation tools

- **Action:** Run both scripts and confirm they work correctly
- **Details:** `python profile_discover.py` shows all 14 profiles. `python soul_propagate.py --dry-run` shows correct states.
- **Estimate:** 15 min
- **Depends on:** 1.1, 1.2

---

## Phase 2: Create Missing Skills (depends on Phase 1)

### Task 2.1 — Create `hermes-personality-soul` skill

- **Action:** Create SKILL.md at `~/AppData/Local/hermes/skills/profiles/hermes-personality-soul/SKILL.md`
- **Details:** Profile personality table (14 rows), persona mapping for soul-enhancer, SOUL.md personality template, cross-references to soul-enhancer/create-missing-souls/profile-soul-minimal-template. YAML frontmatter with tags: [hermes, profiles, personality, soul, identity].
- **Estimate:** 45 min
- **Depends on:** 1.3 (discovery data for accurate profile list)

### Task 2.2 — Create `create-missing-souls` skill

- **Action:** Create SKILL.md at `~/AppData/Local/hermes/skills/profiles/create-missing-souls/SKILL.md`
- **Details:** Discovery-based workflow, applies profile-soul-minimal-template, cross-references hermes-personality-soul for identity content, quick commands referencing soul_propagate.py, verification via validate_memories.py. YAML frontmatter.
- **Estimate:** 40 min
- **Depends on:** 2.1 (personality data), 1.2 (propagation script)

### Task 2.3 — Create `create-missing-memories` skill

- **Action:** Create SKILL.md at `~/AppData/Local/hermes/skills/profiles/create-missing-memories/SKILL.md`
- **Details:** Discovery-based workflow, creates USER.md (per-profile authored) and MEMORY.md (verbatim from root), validates size limits (USER ≤2000B, MEM ≤6000 chars), quick commands, cross-references profile-maintenance and validate-memories. YAML frontmatter.
- **Estimate:** 40 min
- **Depends on:** 1.3 (discovery data)

---

## Phase 3: Enhance Existing Skills (depends on Phase 2)

### Task 3.1 — Enhance `soul-enhancer` skill

- **Action:** Patch `~/AppData/Local/hermes/skills/devops/soul-enhancer/SKILL.md` and `enhance_soul.py`
- **Details:**
  - SKILL.md: Add Skills Required table (references hermes-personality-soul), add Quick Commands section, add post-enhancement hook reference
  - enhance_soul.py: Fix REQUIRED_SECTIONS to match actual SOUL.md format, add `--propagate` flag with `propagate_one()` function, add `--discover-profiles` flag
- **Estimate:** 60 min
- **Depends on:** 2.1 (personality skill exists for cross-reference)

### Task 3.2 — Enhance `hermes-profile-sync` skill

- **Action:** Patch `~/AppData/Local/hermes/skills/development/hermes-profile-sync/SKILL.md` and `sync_profile_configs.py`
- **Details:**
  - SKILL.md: Replace hardcoded PROFILES with discovery note, add `--dry-run` to all invocations, add memory sync delegation section, add Quick Commands section, add Skills Required table referencing hermes-profile-memory-sync
  - sync_profile_configs.py: Add `--discover` flag for dynamic profile discovery
- **Estimate:** 45 min
- **Depends on:** 2.3 (memory skill exists for delegation reference)

### Task 3.3 — Enhance `hermes-profile-memory-sync` skill

- **Action:** Patch `~/AppData/Local/hermes/skills/hermes-profile-memory-sync/SKILL.md`
- **Details:** Add `--dry-run` to workflow steps, add profile discovery note, add alias creation as explicit subcommand in Quick Commands, add Skills Required table referencing create-missing-souls and create-missing-memories, add post-sync verification hook reference.
- **Estimate:** 30 min
- **Depends on:** 2.2, 2.3

### Task 3.4 — Update `hermes-profiles` skill

- **Action:** Patch `~/AppData/Local/hermes/skills/devops/hermes-profiles/SKILL.md`
- **Details:** Update Quick Commands to reference new scripts (profile_discover.py, soul_propagate.py). Add cross-reference note that detailed workflows are in hermes-profile-memory-sync and hermes-profile-sync. Update Skills Required table.
- **Estimate:** 20 min
- **Depends on:** 3.1, 3.2, 3.3

---

## Phase 4: Hooks (depends on Phase 1)

### Task 4.1 — Create post-soul-enhancement hook

- **Action:** Create `~/AppData/Local/hermes/hooks/post-soul-enhancement/validate_soul.sh`
- **Details:** Validates all profile SOUL.md files have `## ` sections and `**Profile:**` header. Returns failure count.
- **Estimate:** 15 min
- **Depends on:** 1.1

### Task 4.2 — Create post-memory-creation hook

- **Action:** Create `~/AppData/Local/hermes/hooks/post-memory-creation/validate_memories.sh`
- **Details:** Runs validate_memories.py after memory creation operations.
- **Estimate:** 10 min
- **Depends on:** 1.1

---

## Phase 5: Block Updates (depends on Phase 3)

### Task 5.1 — Update `.hermes.md`

- **Action:** Patch `~/Desktop/SandBox/.hermes.md`
- **Details:** Update profile skills references. Add quick command references for profile discovery and soul propagation.
- **Estimate:** 20 min
- **Depends on:** 3.4

### Task 5.2 — Update `.github/prompts/` references

- **Action:** Search and update any prompt files referencing profile skills
- **Details:** Check `.github/prompts/` for references to soul-enhancer, hermes-profiles, profile-maintenance. Update to include new skills where relevant.
- **Estimate:** 30 min
- **Depends on:** 3.4

### Task 5.3 — Update `AGENTS.md`

- **Action:** Patch `~/Desktop/SandBox/AGENTS.md`
- **Details:** Add profile skill quick commands to the workspace reference section if present.
- **Estimate:** 15 min
- **Depends on:** 3.4

---

## Task Dependency Graph

```
1.1 ──→ 1.3 ──→ 2.1 ──→ 3.1 ──→ 5.1
  │       │       │       │       │
  └──→ 1.2 ─┘  │       │       │
                │       │       │
                └──→ 2.2 ──→ 3.4 ──→ 5.2
                  │       │
                  └──→ 2.3 ──→ 3.2 ──→ 5.3
                    │       │
                    └──────→ 3.3 ──→ 5.1

1.1 ──→ 4.1
1.2 ──→ 4.2

3.1 ──→ 5.1
3.4 ──→ 5.2, 5.3
```

## Parallelizable Work

| Wave       | Tasks              | Notes                                                      |
| ---------- | ------------------ | ---------------------------------------------------------- |
| **Wave 1** | 1.1, 1.2           | Independent — both are new scripts                         |
| **Wave 2** | 2.1, 2.2, 2.3      | Can run in parallel after 1.3 (all are new SKILL.md files) |
| **Wave 3** | 3.1, 3.2, 3.3      | Independent enhancements — different skill files           |
| **Wave 4** | 4.1, 4.2           | Independent hooks                                          |
| **Wave 5** | 3.4, 5.1, 5.2, 5.3 | Block updates — can batch after Wave 3                     |

## Total Estimates

| Phase                      | Tasks              | Estimated time |
| -------------------------- | ------------------ | -------------- |
| 1: Foundation tools        | 1.1, 1.2, 1.3      | 1.5 h          |
| 2: Create missing skills   | 2.1, 2.2, 2.3      | 2 h            |
| 3: Enhance existing skills | 3.1, 3.2, 3.3, 3.4 | 2.5 h          |
| 4: Hooks                   | 4.1, 4.2           | 0.5 h          |
| 5: Block updates           | 5.1, 5.2, 5.3      | 1 h            |
| **Total**                  |                    | **~7.5 hours** |

## Risks

| Risk                                                       | Likelihood | Impact | Mitigation                                                               |
| ---------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------ |
| `hermes profile list` output format changes                | Low        | Medium | Script has fallback to directory listing                                 |
| validate_memories.py schema changes                        | Low        | Medium | Reference the current schema from the skill; update if validator changes |
| Cross-profile write guard blocks skill file creation       | Medium     | Low    | Create files via terminal (cp) or use write_file with cross_profile=True |
| Existing skill files have content not captured in my reads | Low        | Medium | Read full files before patching; use targeted patches not rewrites       |
