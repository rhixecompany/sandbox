---
name: pending-store-apply
title: "Apply (Drain) the Hermes Native Pending-Approval Store"
description: "Safely execute the staged memory/ + skills/ JSON entries in ~/.hermes/pending/ to live files. Covers review/prune, ordered non-destructive executor, and compact-to-limits. Use when the user says 'approve all /memory pending', 'apply pending', or you must drain the native write_approval staging store."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [memory, skills, pending, approval, hermes, maintenance]
---

# Pending-Store-Apply

## When to Use

- User says "approve all /memory pending", "apply pending", "a -c" (approve + review/prune).
- `memory.write_approval` is enabled and the native staging store has accumulated entries.
- You need to drain `~/.hermes/pending/{memory,skills}/*.json` to live `MEMORY.md`/`USER.md`/skill files.

## What the store is

Hermes native `memory` tool stages writes when `write_approval` is on. Entries land as JSON files:

- `~/.hermes/pending/memory/*.json` → target `memories/MEMORY.md` (target `memory`) or `memories/USER.md` (target `user`)
- `~/.hermes/pending/skills/*.json` → target skill dirs under `~/.hermes/skills/`

There is **no CLI bulk-apply** — "approving" means executing the file ops yourself.

## CRITICAL constraints (read first)

1. **No git rollback.** `~/.hermes` is usually NOT a git repo. Save safety copies of `MEMORY.md`/`USER.md` to a git-tracked workspace dir BEFORE compacting.
2. **Size limits are hard caps** (validated by `validate-memories`): `MEMORY.md < 2200B`, `USER.md < 1375B`. Bulk "add" ops will inflate them ~7x. Always compact to durable facts only after applying.
3. **Queue is frequently STALE.** `create` ops often find the target already on disk; `patch` ops often fail `old_string not found` because disk diverged. Treat both as non-destructive no-ops, never force.
4. **Batch corruption risk.** Targets with 2–14 cumulative ops (e.g. `prompt-management` 14x) must be replayed in timestamp order, not raw order. Blind replay triggers the exact "old_string not found" cascade.

## Path Resolution (MANDATORY)

All scripts here MUST derive `HERMES_HOME` from the `LOCALAPPDATA` env var — never hardcode `C:/Users/<user>/AppData/Local/hermes`.
- Python: `HERMES_HOME = os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"`
- Node: `process.env.LOCALAPPDATA || process.env.USERPROFILE || 'C:\\Users\\Alexa'`
- Bash: `${LOCALAPPDATA:-$HOME/AppData/Local}/hermes`

**Pitfall (session-learned):** `$env:LOCALAPPDATA` is **PowerShell-only** syntax. In `.py`/`.js`/`.cjs`/`.sh` it is *not* a variable — a literal `$env:LOCALAPPDATA\hermes` string is never resolved and breaks the path. Use the native per-shell forms above. `LOCALAPPDATA` is the correct var for `AppData\Local` (not `USERPROFILE`/`HOME`, which point elsewhere). See `env-path-portability` skill.

**Verification harness:** `scripts/verify_apply.py` uses `tempfile.mkdtemp(prefix="hermes-verify-")` and redirects `LOCALAPPDATA` to that temp dir, then runs each apply script as a subprocess with fixtures and asserts file ops. This proves paths resolve from the env var (not hardcoded) without touching live data.

## Workflow

### Phase 1: Review & Prune (always)
Run `scripts/review_pending_skills.py` over `pending/skills/`. Drop:
- `delete` entries whose target dir does NOT exist (no-op).
- `patch`/`batch` ops with empty `new_string`/`content` (no-op).
Move them to `pending/skills/_pruned/` (non-destructive) so the store stays auditable.

### Phase 2: Apply skills (ordered, non-destructive)
Run `scripts/apply_pending_skills.py`. Semantics:
- `create` → if dir exists, **skip** (stale); else write `SKILL.md`.
- `write_file` → write referenced file under skill dir.
- `patch`/`edit` → `old_string.replace(new,1)`; if not found, **fail non-destructively** (skip).
- `delete` → `rmtree` if exists, else skip.
Order: timestamp sort, then creates → write_files → patches → edits → deletes.

### Phase 3: Apply memory (DRY-safe)
Run `scripts/apply_pending_memory.py`. `add` skips if content already present (DRY). `replace`/`remove` skip if `old_text` absent. `batch` applies each op in order.

### Phase 4: Compact to limits
The applied memory files will be over limit. Rewrite to durable facts only (drop dated audit numbers, session IDs, script filenames). Keep: environment, mandatory directives, corrections, skill list. Preserve the user's complex-task mandate. Save pre-compact copies first.

### Phase 5: Verify
- `python validate_memories.py` → expect `Files failing: 0`.
- Run `scripts/verify_apply.py` for ad-hoc logic verification (OS-safe temp harness, no live mutation).

## Assets

- `references/schema.md` — JSON entry shapes + size caps + safety-copy recipe.
- `scripts/review_pending_skills.py` — Phase 1 review/prune helper.
- `scripts/apply_pending_skills.py` — Phase 2 ordered executor.
- `scripts/apply_pending_memory.py` — Phase 3 DRY-safe applier.
- `scripts/verify_apply.py` — ad-hoc verification harness (temp-redirect + assertions).

All scripts read paths from a `CONFIG` block at top — paths are derived from the `LOCALAPPDATA` env var at runtime; do NOT hardcode user-specific paths.

## Pitfalls

- **Don't force-fail.** A `patch` that misses is drift, not lost work — skip it.
- **Don't re-run blindly.** 311-entry queue → 168 applied / 101 skipped / 42 failed is a *healthy* outcome (stale queue), not an error.
- **Compact immediately.** Leaving MEMORY.md at 14KB fails validation and violates the user's own "compact memory" directives.
- **Post-format memory entries.** `apply_pending_memory.py` appends raw text lines to the end of MEMORY.md/USER.md without section headers. After applying, reorganize entries into appropriate `##` sections (e.g. `## Skills Created` for skill-record entries) so the file stays structured.
- **Verify before claiming done** — run `validate_memories.py` and the verify harness; show the output.
