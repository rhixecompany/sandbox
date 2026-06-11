# Repo Prompt Refactor — Implementation Plan

> **Goal:** Refactor `Prompts/repo.prompts.md` into a valid AI prompt following
> prompt-engineering best practices, and create the supporting skill, template,
> and management prompt that complete the pipeline.

**Architecture:** Split one overloaded prompt into two focused prompts backed by
a reusable skill and a shared report template.

**Tech Stack:** Markdown, YAML frontmatter, Hermes skills, Copilot prompt format

---

## Phase 1: Analysis (COMPLETE)

Read `Prompts/repo.prompts.md` in full. Read all 14 `RESEARCH_REPORT.md` files.
Identify structural problems and produce a remediation list.

**Findings:**

| # | Issue | Severity |
|---|-------|----------|
| 1 | Critical anti-fabrication rules buried at line 531 | Critical |
| 2 | Inventory table shows 13 missing — all 14 exist on disk | High |
| 3 | No `mode:`, `system:`, or Hermes-compatible frontmatter fields | High |
| 4 | No `## Constraints` or `## Acceptance Criteria` sections | High |
| 5 | Instruction ratio ~20% (context dominates over directives) | High |
| 6 | Bottom `## Steps` / `## Tasks` duplicates all phase content | Medium |
| 7 | `### Migration Plan Phases` block appears twice (copy-paste) | Medium |
| 8 | Secondary goals reference stale `_archive/repo.prompts.txt` | Medium |
| 9 | Report template inline in body (30-line verbatim block) | Medium |
| 10 | Research pipeline and repo management mixed in one prompt | Medium |
| 11 | Skills list duplicated in frontmatter AND body | Low |
| 12 | Branch bash block cut off (incomplete code) | Low |

**Status:** ✅ Done

---

## Phase 2: Refactor repo.prompts.md (COMPLETE)

Apply all 12 fixes to `Prompts/repo.prompts.md` in a single write.

**Acceptance Criteria:**

- [ ] CRITICAL RULES section is first body section (within first 15% of file)
- [ ] `mode: agent` and `system:` block in frontmatter
- [ ] `## Constraints` and `## Acceptance Criteria` sections present
- [ ] Inventory shows all 14 as UPDATE (not missing)
- [ ] No duplicate `## Steps` / `## Tasks` section at bottom
- [ ] No duplicate `### Migration Plan Phases` block
- [ ] Secondary goals reference `Prompts/repo-management.prompts.md`
- [ ] Report template in `## Report Template` section (body, not archive)
- [ ] Skills table maps skill → phase → purpose (no duplicate in frontmatter)
- [ ] File size < 22KB (was 22.8KB original)
- [ ] `git diff --stat` shows net deletion (removed more than added)

**Result:** 18.5KB (was 22.8KB), net -103 lines, 407 deletions / 304 insertions.

**Status:** ✅ Done — committed at task 4

---

## Phase 3: Create Supporting Assets (COMPLETE)

### Task 3.1 — Create `repo-research-pipeline` skill

**Objective:** Reusable skill encoding the 6-phase research workflow so the
prompt can reference it instead of embedding logic inline.

**File:** `C:\Users\Alexa\AppData\Local\hermes\skills\research\repo-research-pipeline\SKILL.md`

**Acceptance Criteria:**

- [ ] Skill file exists at path above
- [ ] Contains 6 workflow phases (Inventory → Discovery → Research → Writing → Index → Verify)
- [ ] Pitfalls section includes fabricated-count warning from prior session
- [ ] Critical Rules section at top (no-fabrication, verify-before-claiming, scope-guard)
- [ ] Size gate rule (1KB-5KB) documented
- [ ] Symmetric cross-ref rule documented

**Status:** ✅ Done

---

### Task 3.2 — Create `Prompts/templates/RESEARCH_REPORT.template.md`

**Objective:** Extract the report template from the prompt body into a dedicated
file so both the prompt and any subagent can reference a single source of truth.

**File:** `Prompts/templates/RESEARCH_REPORT.template.md`

**Acceptance Criteria:**

- [ ] File exists with 10 required sections in correct order
- [ ] Inline comments explain each section's rules (size, sourcing, symmetry)
- [ ] Template header includes version and size gate comment

**Status:** ✅ Done

---

### Task 3.3 — Create `Prompts/repo-management.prompts.md`

**Objective:** Extract all secondary goals (branch norm, consolidation, dep audit,
Bun migration, CI) from repo.prompts.md into a dedicated, fully-specified prompt.

**File:** `Prompts/repo-management.prompts.md`

**Acceptance Criteria:**

- [ ] Trigger `/repo-management` in frontmatter
- [ ] `mode: agent` and `system:` block
- [ ] CRITICAL RULES as first body section — prerequisite gate + phase ordering
- [ ] 7 phases with tasks, steps, bash commands, and rollback plans
- [ ] Phase 3 (branch normalization) has complete bash script (was cut off in original)
- [ ] Acceptance criteria table with terminal verification commands
- [ ] References `/repo` as prerequisite in Related Prompts

**Status:** ✅ Done

---

## Phase 4: Verification

Run before commit.

**Tasks:**

- [ ] `Prompts/repo.prompts.md` — head shows YAML frontmatter, CRITICAL RULES first section
- [ ] `Prompts/repo-management.prompts.md` — exists, trigger `/repo-management`
- [ ] `Prompts/templates/RESEARCH_REPORT.template.md` — exists, 10 sections
- [ ] `skills/research/repo-research-pipeline/SKILL.md` — exists, 7.7KB
- [ ] `docs/plans/repo-prompt-refactor.md` — this file exists
- [ ] `git diff --stat` — all 5 new/modified files staged

**Verification commands:**

```bash
# File existence
ls Prompts/repo.prompts.md Prompts/repo-management.prompts.md \
   Prompts/templates/RESEARCH_REPORT.template.md \
   docs/plans/repo-prompt-refactor.md

# Skill
ls ~/AppData/Local/hermes/skills/research/repo-research-pipeline/SKILL.md

# Section counts
grep -c '^## ' Prompts/repo.prompts.md        # expect >= 10
grep -c '^## ' Prompts/repo-management.prompts.md  # expect >= 8

# Frontmatter check
head -5 Prompts/repo.prompts.md               # must start with ---
head -5 Prompts/repo-management.prompts.md    # must start with ---

# Sizes
wc -c Prompts/repo.prompts.md                 # expect ~18KB
wc -c Prompts/repo-management.prompts.md      # expect ~10KB+
```

---

## Phase 5: Commit and Push

Single atomic commit covering all 5 deliverables.

```bash
git add Prompts/repo.prompts.md \
        Prompts/repo-management.prompts.md \
        Prompts/templates/RESEARCH_REPORT.template.md \
        docs/plans/repo-prompt-refactor.md

git commit -m "refactor: repo.prompts.md — split, harden, add skill + template + management prompt"

git push origin master
```

---

## Deliverables Summary

| File | Action | Key Change |
|------|--------|------------|
| `Prompts/repo.prompts.md` | Refactored | Critical rules first, mode/system frontmatter, AC table, no duplication, correct inventory |
| `Prompts/repo-management.prompts.md` | Created | Full spec for all 6 secondary goals with rollback plans |
| `Prompts/templates/RESEARCH_REPORT.template.md` | Created | Single-source template for all 14 report files |
| `skills/research/repo-research-pipeline/SKILL.md` | Created | Reusable 6-phase research pipeline skill |
| `docs/plans/repo-prompt-refactor.md` | Created | This plan |
