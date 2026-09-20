---
goal: "Unified Multi-File CRUD Protocol (≥4 files)"
version: 1.0.0
date_created: 2026-09-17
last_updated: 2026-09-17
owner: Alexander E Iseghohi
status: "In progress"
tags: [protocol, multi-file, crud, workflow, orchestration]
---

# Unified Multi-File CRUD Protocol — Implementation Plan

## Goal

Merge the existing `/multi-file-change-protocol` (>5 file trigger) with the new extended workflow (≥4 file trigger, full CRUD skill stack, subagent delegation, clarify rounds) into a single unified protocol stored as `/multi-file-crud-protocol`, with a brief reference in MEMORY.md.

## Subgoals

1. Create unified skill at `~/AppData/Local/hermes/skills/multi-file-crud-protocol/SKILL.md`
2. Update MEMORY.md with brief reference to the new protocol
3. Mark old `/multi-file-change-protocol` as superseded by the unified skill
4. Verify all artifacts via skill-judge + manual checklist

## Steps

### Phase 1: Create Unified Skill

- Create `~/AppData/Local/hermes/skills/multi-file-crud-protocol/` directory
- Write `SKILL.md` with full unified protocol content
- Include: trigger rule, reordered skill stack, extended workflow, 5-step protocol, decision tree, profile routing, rules enforcement

### Phase 2: Update MEMORY.md

- Read current MEMORY.md
- Add brief §-delimited entry referencing the new skill
- Preserve all existing entries

### Phase 3: Supersede Old Skill

- Read existing `multi-file-change-protocol/SKILL.md`
- Add frontmatter `superseded_by: multi-file-crud-protocol` marker
- Keep original content intact for reference

### Phase 4: Verify

- Run skill-judge on new skill
- Verify file sizes via os.path.getsize
- Verify MEMORY.md size increased correctly
- Confirm no .env exposure, no synthetic artifacts

## Todos

- [ ] Create unified skill directory + SKILL.md
- [ ] Update MEMORY.md with reference
- [ ] Mark old skill as superseded
- [ ] Run verification gates

## Phases

1. **CREATE** — Write all artifacts
2. **VERIFY** — Run checks + skill-judge
3. **COMPLETE** — Final report

## Tasks

| ID  | Owner   | Description                   | Dependencies |
| --- | ------- | ----------------------------- | ------------ |
| T1  | default | Create unified skill SKILL.md | None         |
| T2  | default | Update MEMORY.md              | T1           |
| T3  | default | Mark old skill superseded     | T1           |
| T4  | default | Verify all artifacts          | T1, T2, T3   |

## Gates

- [ ] G1: SKILL.md exists and is valid YAML markdown
- [ ] G2: MEMORY.md updated with new entry
- [ ] G3: Old skill marked superseded
- [ ] G4: skill-judge passes (or unavailability recorded)
- [ ] G5: No .env exposure, no synthetic artifacts

## Needed Specs

- `~/AppData/Local/hermes/skills/multi-file-change-protocol/SKILL.md` (read for merge)
- `$HERMES_HOME/profiles/default/MEMORY.md` (read for update)

## Dependencies and Risks

- Risk: Old skill may have references that need updating → Mitigation: keep old skill intact, just add superseded marker
- Risk: MEMORY.md may be near char limit → Mitigation: keep entry concise (§-delimited, <200 chars)

## Verification Evidence

- File sizes via os.path.getsize
- skill-judge result
- MEMORY.md diff

## Rollback and Completion

- Rollback: remove new skill, revert MEMORY.md via git
- Completion: all gates pass, report to user
