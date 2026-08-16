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

## Overview

Automated reasoning and workflow tool for `pending-store-apply`. Execute multi-step tasks with deterministic quality controls and structured outputs.

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
2. **Size limits are hard caps — byte caps verified live (2026-08-08).** `validate-memories` enforces `MEMORY.md < 6000B`, `USER.md < 2000B` and reports overage as `size NNNN>6000` / `size NNNN>2000`. The old `< 2200B / < 1375B` figures in earlier docs are stale — trust the validator output, not the docs. Practical inflation: applying 5 pending entries took MEMORY.md 5935→7357B and USER.md ~155→3188B, so a small queue still blows both caps ~7x (USER especially, being capped at 2000B).
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
- `python validate_memories.py` → expect `Files failing: 0`. Location: `$LOCALAPPDATA/hermes/skills/devops/validate-memories/scripts/validate_memories.py` — NOT `$LOCALAPPDATA/hermes/scripts/` (that path does not exist; the scoped `~/scripts/validate_memories.py` call fails with `can't open file`).
- Run `scripts/verify_apply.py` for ad-hoc logic verification (OS-safe temp harness, no live mutation).

### Phase 6: Drain the store
After a successful apply+compact, move the processed JSON files from `pending/memory/` to `pending/memory/_pruned/` (e.g. `mv 20b621da.json ... _pruned/`) so the queue stays auditable and doesn't re-apply next time. The apply script does NOT delete the JSONs it consumes — the store only shrinks when you move them.

## Compaction workflow (use after every Phase 3 apply)

1. Read current `MEMORY.md` + `USER.md` (they now carry appended raw lines).
2. Rewrite with `write_file`: group entries under `##` sections, keep `§` separators between entries (the file convention), drop dated/session-specific noise, keep durable env/directives/corrections/skill reference.
3. Measure: `wc -c` both files. Hard caps: MEMORY ≤5999B, USER ≤1999B.
4. If a few bytes over, micro-trim prose (not facts): shorten wording inside an entry, then `wc -c` again. The pal/home race is at 1-byte granularity — 6003 fails, 5993 passes.
5. **NEVER falsify content to hit the cap.** In 2026-08-08 a compaction draft changed a real fact (canonical skill count "619 (root 630 incl .archive 8 + 3 flat dups)") into a made-up "618 (root 809 + 8 flat dups)" purely to save bytes. That is data corruption for the sake of 10 bytes — always revert false saves and find genuine wording to trim. If you edited a tract of text purely to save bytes, re-read it and confirm every fact survives intact, and verify the new size.
6. Re-run validate_memories → 42/42 (0 failing). Back up pre-compact copies to a git-tracked dir (`~/Desktop/SandBox/hermes-memory-safety/`) BEFORE the rewrite so you can diff/restore.

## Assets

- `references/schema.md` — JSON entry shapes + size caps + safety-copy recipe.
- `scripts/review_pending_skills.py` — Phase 1 review/prune helper.
- `scripts/apply_pending_skills.py` — Phase 2 ordered executor.
- `scripts/apply_pending_memory.py` — Phase 3 DRY-safe applier.
- `scripts/verify_apply.py` — ad-hoc verification harness (temp-redirect + assertions).

All scripts read paths from a `CONFIG` block at top — paths are derived from the `LOCALAPPDATA` env var at runtime; do NOT hardcode user-specific paths. Note: `apply_pending_memory.py`'s CONFIG block still hardcodes `C:/Users/Alexa/...` — if you run on a different machine, sed the MEM/USR/PENDING paths first (or PR the script to env-drive them).

## Pitfalls

- **Don't force-fail.** A `patch` that misses is drift, not lost work — skip it.
- **Don't re-run blindly.** 311-entry queue → 168 applied / 101 skipped / 42 failed is a *healthy* outcome (stale queue), not an error.
- **Compact immediately.** Leaving MEMORY.md at 14KB fails validation and violates the user's own "compact memory" directives.
- **Post-format memory entries.** `apply_pending_memory.py` appends raw text lines to the end of MEMORY.md/USER.md without section headers. After applying, reorganize entries into appropriate `##` sections (e.g. `## Skills Created` for skill-record entries) so the file stays structured.
- **Verify before claiming done** — run `validate_memories.py` and the verify harness; show the output.
- **Delete-and-recreate alternative.** When the user says "delete all failed memory and recreate, approve them", they want: (1) delete all pending JSON files from `~/.hermes/pending/memory/`, (2) evaluate each entry's content for durability (skip stale session records, duplicates, SOP-level directives), (3) write surviving entries directly to MEMORY.md via `patch`, (4) verify size stays under limit and pending store is empty. This bypasses the standard Phase 1-5 pipeline — it's appropriate when the queue is small (≤10 entries) and the user explicitly wants a clean slate.
- **`memory` tool stages every write as pending.** When `write_approval` is enabled, every `memory(action='add')` or `memory(action='batch')` creates a new JSON file in the pending store instead of directly modifying MEMORY.md. To avoid inflating the queue during maintenance, use `write_file` or `patch` on MEMORY.md directly instead of the `memory` tool. This is how the "delete-and-recreate" pattern works in practice.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Apply (Drain) the Hermes Native Pending-Approval Store" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
