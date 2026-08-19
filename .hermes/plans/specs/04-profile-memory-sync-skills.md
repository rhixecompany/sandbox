# SPEC: Profile/Memory Sync Skills (6 Skills)

**Workstream:** 04-profile-memory-sync-skills
**Priority:** P1 - Core Ask
**Dependencies:** 02-mcp-server-suite, 03-subagent-driven-development
**Profile:** code-architect

---

## Problem Statement

User requested implementation of 6 profile/memory sync skills:
1. **soul-enhancer** — SOUL.md enhancement, persona→tone→traits mapping for all 14 Hermes profiles
2. **hermes-personality-soul** — Personality config for all 14 Hermes profiles
3. **create-missing-souls** — Discover/create SOUL.md for profiles missing it
4. **create-missing-memories** — Discover/create USER.md/MEMORY.md for profiles
5. **hermes-profile-sync** — Bidirectional-safe root↔profile config.yaml propagation
6. **hermes-profile-memory-sync** — Sync memory files + aliases across profiles

Each skill must be class-level (not one-off), with SKILL.md + references/ + templates/ + scripts/ + CI workflow.

## Skill Requirements (Per Skill)

### Common Requirements
- [ ] SKILL.md with complete frontmatter
- [ ] Skills Required table
- [ ] Workflow with ≥ 3 phases
- [ ] Pitfalls section
- [ ] Verification checklist
- [ ] Line count < 250 (detail in references/)
- [ ] At least 3 supporting files (references/, templates/, scripts/)
- [ ] Passes `skill-judge` ≥ 90
- [ ] Loads via `skill_view` without error

---

### 1. soul-enhancer
**Location:** `skills/profiles/soul-enhancer/`
**Purpose:** Enhance SOUL.md files with persona→tone→traits mapping for all 14 Hermes profiles

**Workflow:**
1. **Analyze** — Read target SOUL.md, identify gaps in persona/tone/traits
2. **Map** — Apply 14-profile personality matrix (default, adminbot, code-architect, research-analyst, creative-director, exec-assistant, patient-tutor, cto, pm, security, etc.)
3. **Enhance** — Add missing sections: cognitive style, execution frameworks, architectural invariants, standing rules
4. **Validate** — Cross-reference with USER.md/MEMORY.md for DRY compliance

**References:** `references/profile-personality-matrix.md`, `references/soul-template.md`

---

### 2. hermes-personality-soul
**Location:** `skills/profiles/hermes-personality-soul/`
**Purpose:** Define personality config for all 14 Hermes profiles

**Workflow:**
1. **Inventory** — List all 14 profiles and their intended use cases
2. **Define** — Map each profile to: model, temperature, system prompt additions, tool preferences
3. **Document** — Create personality reference with examples
4. **Sync** — Propagate to profile configs via hermes-profile-sync

**References:** `references/14-profile-personalities.md`, `references/personality-template.yaml`

---

### 3. create-missing-souls
**Location:** `skills/profiles/create-missing-souls/`
**Purpose:** Discover profiles missing SOUL.md or with stub SOUL.md; create from template

**Workflow:**
1. **Discover** — Scan `~/AppData/Local/hermes/profiles/` for directories
2. **Check** — For each profile, verify SOUL.md exists and has content (> 100 lines)
3. **Create** — For missing/stub: generate from soul-template.md with profile-specific persona
4. **Verify** — Validate each created SOUL.md with `validate-memories`

**References:** `references/soul-template.md`, `references/profile-discovery-script.py`

---

### 4. create-missing-memories
**Location:** `skills/profiles/create-missing-memories/`
**Purpose:** Discover profiles missing USER.md/MEMORY.md; create from template

**Workflow:**
1. **Discover** — Scan all profiles for USER.md and MEMORY.md
2. **Check** — Verify files exist and meet minimum criteria
3. **Create** — Generate USER.md (pointer to MEMORY.md) and MEMORY.md (§-delimited)
4. **Sync** — Run hermes-profile-memory-sync to propagate aliases

**References:** `references/user-template.md`, `references/memory-template.md`, `references/profile-discovery-script.py`

---

### 5. hermes-profile-sync
**Location:** `skills/profiles/hermes-profile-sync/`
**Purpose:** Bidirectional-safe propagation of root Hermes config.yaml into profile configs

**Workflow:**
1. **Read** — Load root config.yaml and all profile config.yaml files
2. **Diff** — Compare root vs profile for each configurable section
3. **Plan** — Generate sync plan (what to propagate, direction, conflicts)
4. **Execute** — Apply changes with safety checks (backup, dry-run, verify)
5. **Verify** — Confirm all profiles have consistent critical settings

**References:** `references/sync-rules.md`, `references/config-diff-script.py`, `references/verify-sync-script.py`

---

### 6. hermes-profile-memory-sync
**Location:** `skills/profiles/hermes-profile-memory-sync/`
**Purpose:** Sync memory files (USER.md, MEMORY.md) and aliases safely across profiles

**Workflow:**
1. **Read** — Load memory files from all 7 profiles
2. **Normalize** — Ensure consistent format (§-delimited, no H1)
3. **Merge** — Intelligently merge facts (newest wins, preserve profile-specific)
4. **Alias Sync** — Sync command aliases, shortcuts, custom tools
5. **Write** — Update all profile memory files
6. **Verify** — Run `validate-memories` on all profiles

**References:** `references/memory-merge-rules.md`, `references/alias-sync-script.py`, `references/validate-memories-script.py`

---

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

## Implementation Approach

```bash
# For each skill:
# 1. Create skill directory
mkdir -p ~/AppData/Local/hermes/skills/profiles/<skill-name>/{references,templates,scripts}

# 2. Write SKILL.md with full workflow
# 3. Write reference files
# 4. Write template files
# 5. Write automation scripts (Python)
# 6. Write CI workflow (.github/workflows/)
# 7. Update SKILL.md Assets list
# 8. Verify: skill_view, skill-judge
```

## Verification Steps

```bash
# Test each skill loads
for skill in soul-enhancer hermes-personality-soul create-missing-souls create-missing-memories hermes-profile-sync hermes-profile-memory-sync; do
  skill_view $skill
  echo "---"
done

# Run verify-sync
python3 ~/AppData/Local/hermes/scripts/verify_sync.py

# Validate memories
# (validate-memories skill or script)
```

## Risks

- **Profile directory structure** — 7 profiles under `~/AppData/Local/hermes/profiles/`
- **USER-owned skills** — `create-missing-memories` and `create-missing-souls` are USER-owned (curator refuses autonomous patches); need `hermes curator adopt` before editing
- **Config.yaml edit guard** — hermes-profile-sync must use `hermes config set` CLI, not direct file edits
- **Cross-profile drift** — Sync must be bidirectional-safe with conflict resolution

## References

- MEMORY.md: "USER-OWNED skills (created_by=None, curator refuses autonomous patches; `hermes curator adopt` before editing): profile-directive-sync, convert-plaintext-to-md, enhance-markdown"
- MEMORY.md: "Hermes config updates — use CLI, not direct file edits"
- MEMORY.md: "hermes-profiles mirror WIPED 2026-08-05 per user approval (gitignored, 0 tracked); backups at /tmp/hermes-profiles-*.bak"
- `~/AppData/Local/hermes/scripts/verify_sync.py` — parity root↔Codex↔OpenCode↔mirror↔6 profiles (65 checks)