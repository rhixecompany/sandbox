---
name: 04-profile-memory-sync-skills
title: Profile/Memory Sync Skills (6 Skills)
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Implement 6 profile/memory sync skills (soul-enhancer, hermes-personality-soul, create-missing-souls, create-missing-memories, hermes-profile-sync, hermes-profile-memory-sync) as class-level skills with SKILL.md + references/ + templates/ + scripts/ + CI workflow for all 14 Hermes profiles.

## Requirements

### Common Requirements (Per Skill)
- [ ] SKILL.md with complete frontmatter
- [ ] Skills Required table
- [ ] Workflow with ≥ 3 phases
- [ ] Pitfalls section
- [ ] Verification checklist
- [ ] Line count < 250 (detail in references/)
- [ ] At least 3 supporting files (references/, templates/, scripts/)
- [ ] Passes `skill-judge` ≥ 90
- [ ] Loads via `skill_view` without error

### 1. soul-enhancer
**Location:** `skills/profiles/soul-enhancer/`
**Purpose:** Enhance SOUL.md files with persona→tone→traits mapping for all 14 Hermes profiles
- [ ] Analyze — Read target SOUL.md, identify gaps in persona/tone/traits
- [ ] Map — Apply 14-profile personality matrix
- [ ] Enhance — Add missing sections: cognitive style, execution frameworks, architectural invariants, standing rules
- [ ] Validate — Cross-reference with USER.md/MEMORY.md for DRY compliance

### 2. hermes-personality-soul
**Location:** `skills/profiles/hermes-personality-soul/`
**Purpose:** Define personality config for all 14 Hermes profiles
- [ ] Inventory — List all 14 profiles and their intended use cases
- [ ] Define — Map each profile to: model, temperature, system prompt additions, tool preferences
- [ ] Document — Create personality reference with examples
- [ ] Sync — Propagate to profile configs via hermes-profile-sync

### 3. create-missing-souls
**Location:** `skills/profiles/create-missing-souls/`
**Purpose:** Discover profiles missing SOUL.md or with stub SOUL.md; create from template
- [ ] Discover — Scan `~/AppData/Local/hermes/profiles/` for directories
- [ ] Check — For each profile, verify SOUL.md exists and has content (> 100 lines)
- [ ] Create — For missing/stub: generate from soul-template.md with profile-specific persona
- [ ] Verify — Validate each created SOUL.md with `validate-memories`

### 4. create-missing-memories
**Location:** `skills/profiles/create-missing-memories/`
**Purpose:** Discover profiles missing USER.md/MEMORY.md; create from template
- [ ] Discover — Scan all profiles for USER.md and MEMORY.md
- [ ] Check — Verify files exist and meet minimum criteria
- [ ] Create — Generate USER.md (pointer to MEMORY.md) and MEMORY.md (§-delimited)
- [ ] Sync — Run hermes-profile-memory-sync to propagate aliases

### 5. hermes-profile-sync
**Location:** `skills/profiles/hermes-profile-sync/`
**Purpose:** Bidirectional-safe propagation of root Hermes config.yaml into profile configs
- [ ] Read — Load root config.yaml and all profile config.yaml files
- [ ] Diff — Compare root vs profile for each configurable section
- [ ] Plan — Generate sync plan with direction and conflict resolution
- [ ] Execute — Apply changes with safety checks (backup, dry-run, verify)
- [ ] Verify — Confirm all profiles have consistent critical settings

### 6. hermes-profile-memory-sync
**Location:** `skills/profiles/hermes-profile-memory-sync/`
**Purpose:** Sync memory files (USER.md, MEMORY.md) and aliases safely across profiles
- [ ] Read — Load memory files from all 7 profiles
- [ ] Normalize — Ensure consistent format (§-delimited, no H1)
- [ ] Merge — Intelligently merge facts (newest wins, preserve profile-specific)
- [ ] Alias Sync — Sync command aliases, shortcuts, custom tools
- [ ] Write — Update all profile memory files
- [ ] Verify — Run `validate-memories` on all profiles

## Acceptance Criteria (All 6 Skills)

| Check | Command | Expected |
|-------|---------|----------|
| soul-enhancer loads | `skill_view soul-enhancer` | Success |
| hermes-personality-soul loads | `skill_view hermes-personality-soul` | Success |
| create-missing-souls loads | `skill_view create-missing-souls` | Success |
| create-missing-memories loads | `skill_view create-missing-memories` | Success |
| hermes-profile-sync loads | `skill_view hermes-profile-sync` | Success |
| hermes-profile-memory-sync loads | `skill_view hermes-profile-memory-sync` | Success |
| All skill-judge ≥ 90 | `skill-judge <each>` | Score ≥ 90 |
| Each has ≥ 3 support files | `ls skills/profiles/<skill>/{references,templates,scripts}/` | ≥ 3 files |
| Cross-profile sync works | `verify-sync` | 65 checks pass |

## Non-Functional Requirements

Each skill must be class-level (not one-off) with full SKILL.md + references/ + templates/ + scripts/ + CI workflow. Each skill must have ≥ 3 supporting files. Line count under 250 per SKILL.md with detail in references. USER-owned skills (create-missing-memories, create-missing-souls) require `hermes curator adopt` before editing. hermes-profile-sync must use `hermes config set` CLI, not direct file edits.

## Verification

```bash
# Test each skill loads
for skill in soul-enhancer hermes-personality-soul create-missing-souls create-missing-memories hermes-profile-sync hermes-profile-memory-sync; do
  skill_view $skill
  echo "---"
done

# Run verify-sync
python3 ~/AppData/Local/hermes/scripts/verify_sync.py
# Expected: 65 checks pass

# Validate memories
# (validate-memories skill or script)
```

## Linked Specs
- 04-profile-memory-sync-skills.md

## Linked Plan
- ../2026-08-15_hermes-profile-skills-enhancement-plan.md
