---
title: Goal 1 — Refactor context files + extract multi-file-change-protocol skill
status: "in_progress"
created: 2026-09-11
applies_to: SandBox root + ~/AppData/Local/hermes (SOUL/USER/MEMORY + skills/)
trigger_threshold: >6 file changes → load 14-skill stack
---

# Goal 1 — Refactor Context Files (Strict DRY, Token Preservation)

## Decision Lock (from clarifications)

| Decision               | Value                                                        | Source               |
| ---------------------- | ------------------------------------------------------------ | -------------------- |
| Auto-trigger threshold | **>6 file changes**                                          | user literal request |
| Protocol location      | extract into dedicated skill `multi-file-change-protocol`    | user pick #2         |
| Slimming style         | **Strict DRY** — pure cross-references, no inline duplicates | user pick #1         |
| Dedupe workflow skill  | single `dedupe-skills` skill                                 | user pick #1         |

## Scope (10 files affected)

| #   | Path                                                                                         | Action                                                    | New line target |
| --- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------- |
| 1   | `SandBox/$HERMES_HOME.md`                                                                    | rewrite as pointer + add >6 trigger + reference new skill | ~50             |
| 2   | `SandBox/AGENTS.md`                                                                          | rewrite as pointer + add >6 trigger + reference new skill | ~40             |
| 3   | `SandBox/CLAUDE.md`                                                                          | rewrite as pointer                                        | ~15             |
| 4   | `SandBox/.cursorrules`                                                                       | rewrite as pointer                                        | ~15             |
| 5   | `~/AppData/Local/hermes/SOUL.md`                                                             | strip to persona + invariants, reference new skill        | ~120            |
| 6   | `~/AppData/Local/hermes/memories/USER.md`                                                    | already pointer — verify no duplication                   | ~50             |
| 7   | `~/AppData/Local/hermes/memories/MEMORY.md`                                                  | already §-delimited — verify no H1, trim duplicates       | ~50             |
| 8   | NEW: `~/AppData/Local/hermes/skills/multi-file-change-protocol/SKILL.md`                     | create                                                    | ~80             |
| 9   | NEW: `~/AppData/Local/hermes/skills/multi-file-change-protocol/references/14-skill-stack.md` | create                                                    | ~60             |
| 10  | NEW: `~/AppData/Local/hermes/skills/dedupe-skills/SKILL.md`                                  | create                                                    | ~60             |

(Skill_manage creates new skills at `~/AppData/Local/hermes/skills/<name>/SKILL.md` — auto-creates folder.)

## Phase 1 — Extract protocol skill (before slimming, so SOUL/AGENTS have a target to reference)

1. Create `multi-file-change-protocol` skill via `skill_manage`:
   - Description first 57 chars: `Use when a request will modify >6 files. Load 14-skill stack`
   - YAML frontmatter: name, version, author
   - Body: trigger rule, the 14-skill list, 5-step protocol, verification checklist
   - Reference file: `references/14-skill-stack.md` — full table of skills → purpose

**Gate 1.1:** `skill_view(name='multi-file-change-protocol')` returns the new skill body.
**Gate 1.2:** file exists at `~/AppData/Local/hermes/skills/multi-file-change-protocol/SKILL.md` with ≥10 line body.

## Phase 2 — Slim SOUL.md (most duplication source)

1. Strip lines 280-323 (Multi-File Change Protocol block in current SOUL.md) — replaced by reference.
2. Replace with: `>6 file change trigger → see skill: multi-file-change-protocol`
3. Keep all persona, invariants, memory hierarchy, 4 mandatory rules (these are SOUL-only).
4. Verify SOUL.md < 130 lines.

**Gate 2.1:** `grep -q "Multi-File Change Protocol" SOUL.md` returns non-empty (table of contents marker) but the inlined block is gone.
**Gate 2.2:** line count ≤130.

## Phase 3 — Slim `$HERMES_HOME.md` + `AGENTS.md` (workspace-specific overrides)

1. Remove duplicate Profile table from both files (already in SOUL/USER).
2. Replace inlined "Multi-File Change Protocol (≥5 files)" with: trigger + skill reference.
3. `$HERMES_HOME.md` keeps Hermes-specific paths (e.g. `~/myvenv`, MCP server list — workspace-only).
4. `AGENTS.md` keeps workspace layout, .github/prompts library map (workspace-only).
5. Add `>6 file threshold` reminder to both (was `≥5`).

**Gate 3.1:** both files reference `multi-file-change-protocol` skill instead of inlining the 14-skill list.
**Gate 3.2:** `$HERMES_HOME.md` ≤60 lines, `AGENTS.md` ≤60 lines.

## Phase 4 — Slim `CLAUDE.md` + `.cursorrules` (already thin stubs)

1. Verify they are pointers only — no functional content to strip.
2. Update multi-file threshold text from `≥5` → `>6`.
3. Replace inline "see SOUL.md canonical block" → "see skill: multi-file-change-protocol".

**Gate 4.1:** both files ≤20 lines, both contain trigger reference.

## Phase 5 — Verify USER.md / MEMORY.md (already pointer/§-delimited)

1. `~/AppData/Local/hermes/memories/USER.md` — already pointer. Verify no inlined profile table.
2. `~/AppData/Local/hermes/memories/MEMORY.md` — §-delimited per Rule 4. Verify no H1 header.
3. No edits expected unless duplicates creep in.

**Gate 5.1:** USER.md ≤55 lines, MEMORY.md ≤55 lines, no H1 in MEMORY.md.

## Phase 6 — Create `dedupe-skills` skill (for Goal 3)

1. `skill_manage` create with description `Use when hermes skills list shows duplicates. Dedupe by category, preserve newest version`.
2. Body: workflow (log → dedupe by category → delete old duplicates → log updated).

**Gate 6.1:** skill exists, body ≥10 lines.

## Phase 7 — Verification

1. `hermes profile list` (verify still works).
2. `grep -L "multi-file-change-protocol" $HERMES_HOME.md AGENTS.md CLAUDE.md .cursorrules SOUL.md` returns nothing (all reference the skill).
3. Total token count of 9 refactored files ≤ 3,500 lines (down from ~870 currently → save ~60%).
4. `hermes skills list | grep -E "(multi-file-change-protocol|dedupe-skills)"` shows both.

## Risks & Mitigations

| Risk                                                    | Mitigation                                                                             |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Strict DRY breaks TUI rendering if links fail           | keep `>6 trigger` text + skill name verbatim in every file (no fragile markdown links) |
| Profile copy (Goal 5) wipes profile-only customizations | backup first per user clarification                                                    |
| New skill folder structure wrong                        | `skill_manage` `create` action auto-creates folder per docs                            |

## Out of Scope (Goals 2-5)

- Tech-stack reports → Goal 2
- Skills dedupe execution → Goal 3
- Free-model benchmark → Goal 4
- Profile cleanup + sync → Goal 5

## Completion Signal

"All 9 refactored files ≤ targets, both new skills registered, grep gates green."
