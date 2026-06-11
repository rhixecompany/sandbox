---
name: profile-maintenance
title: Profile Maintenance — Audit & Update USER.md, MEMORY.md, SOUL.md
category: devops
description: "Systematic process for updating Hermes profile identity files (USER.md, MEMORY.md, SOUL.md) from accumulated session knowledge, environment state, and user corrections. Run at session start and end."
---

# Profile Maintenance

Audit and update the agent's self-knowledge files to match actual user preferences, environment state, and accumulated learning across sessions.

Trigger: "update/enhance/verify SOUL.md USER.md MEMORY.md" or run at session start/end.

## When to Use

- Session start: quick audit (Phase 1–2 only) to detect drift
- Session end: full apply (all phases) to capture what changed this session
- User asks "update USER.md/MEMORY.md/SOUL.md from what you know" or "enhance/verify profiles"
- User provides new personal info, preferences, or corrections
- Environment state changed (new model, provider, shell, profile config)
- After consolidating across multiple sessions
- Periodic health check: are the identity files still accurate?

## When NOT to Use

- Simple one-off facts — use `memory` tool directly (faster, no file overhead)
- Session-specific task progress — belongs in session_search, not persistent files
- Transient environment errors — do NOT persist "command not found" or "tool broken" state

## Workflow

### Phase 1: Gather Current State

1. Read all 4 files:
   - `~/AppData/Local/hermes/USER.md` — full identity/profile
   - `~/AppData/Local/hermes/SOUL.md` — operating principles
   - `~/AppData/Local/hermes/memories/MEMORY.md` — environment/project notes
   - `~/AppData/Local/hermes/memories/USER.md` — compact profile summary

2. Verify current environment with CLI tools:
   - `hermes profile list` — active profile, model, gateway status
   - `pwd` — current working directory
   - `echo $SHELL` — active shell
   - Check HERMES_HOME / config.yaml for paths

3. Search past sessions for user info, preferences, corrections:
   - `session_search(query="preference OR correction OR style OR convention")`
   - Look for explicit "remember this", "stop doing X", "don't format like this"

### Phase 2: Cross-Reference

Use the detailed checklist at `references/audit-checklist.md`. Summary:

4. Identify stale/missing/incorrect info by comparing:
   - Current environment ↔ file contents
   - Past session corrections ↔ current rules
   - User profile (memory) ↔ file contents

5. Check for DRY violations: is any info duplicated across files?

### Phase 3: Write with DRY

Each file owns exactly one concern — no overlap:

| File | Owns | Content |
|------|------|---------|
| `USER.md` | Identity + profile | Name, OS, editor, shell, model, provider, profiles list, exec prefs summary, refs SOUL.md for standards |
| `SOUL.md` | Operating principles | Tone, core rules, code quality, file ops protocol, security, skills protocol, response style, voice |
| `memories/MEMORY.md` | Environment notes | Hermes home/paths, GitHub orgs/repos, tool install paths, ACPX agent config, current session state |
| `memories/USER.md` | Compact profile | One-liner summary referencing root USER.md for full details |

6. Write each file with the correct scope.

### Phase 4: Verify

7. Confirm no fact, rule, or instruction is duplicated across files
8. Verify USER.md references SOUL.md for dev standards (doesn't inline them)
9. Verify SOUL.md doesn't repeat user identity/profile from USER.md
10. Verify MEMORY.md doesn't repeat user preferences or operating rules
11. Verify memories/USER.md references root USER.md (compact proxy)

## DRY Enforcement Rules

- **USER.md** → identity, profiles, model, exec prefs summary → references SOUL.md for standards
- **SOUL.md** → tone, rules, code quality, security, skills protocol → does NOT contain user identity
- **MEMORY.md** → env paths, GitHub orgs, tool configs, ACPX details → does NOT contain preferences or principles
- **memories/USER.md** → compressed user ref → links to root USER.md → does NOT duplicate content

## References

- `references/audit-checklist.md` — Detailed pass/fail audit checklist (structural, DRY, completeness, freshness, anti-patterns)
- `references/memory-tool-drift.md` — Memory-file drift reproduction and recovery notes after patch/write operations

## Pitfalls

- **Don't persist transient errors.** A "command not found" or "tool broke" in one session is not a durable fact. Only persist fixable config steps.
- **Don't save task progress.** Completed work, PR numbers, commit SHAs, "Phase N done" belong in session_search, not persistent files.
- **Don't skip environment verification.** Static context drifts — always run `hermes profile list` and `pwd` rather than answering from memory.
- **Don't miss the memories/ copies.** There are 4 files (2 root + 2 memories/) — all need updating to stay in sync.
- **Don't duplicate across files.** If you catch yourself writing the same rule in two files, stop and pick one owner file; cross-reference from the other.

### Pitfall: `memory(action='replace')` Matches Injected Context, Not File Content

**Problem:** The `memory` tool's `replace` action matches `old_text` against the **injected context** shown in the system prompt (a whitespace-collapsed, single-line render), NOT against the raw file content. If you read a file with `read_file` and use that text verbatim as `old_text`, the match will almost always fail because whitespace, line breaks, and formatting differ.

**Symptom:** `memory(action='replace')` returns "No entry matched" even though the text clearly exists in the file. Repeated attempts with slightly different substrings all fail. You end up calling `memory(action='add')` which then hits the char limit.

**Prevention:**
1. To update memory, use the **exact text as shown in the injected system prompt** at the top of the session — not text read from disk.
2. If the injected prompt text is too long or mashed together, use `memory(action='add')` to append the corrected entry, then optionally `memory(action='remove')` on the old one using a short unique substring from the injected version.
3. If memory store is near its char limit (check usage in the injected prompt, e.g. "72% — 998/1,375 chars"), remove stale entries before adding new ones. The store WILL reject additions silently with a size-exceeded error.

**Recovery:** If `replace` keeps failing and `add` hits the char limit, free space first by removing truly stale entries, then retry `add`. Do NOT keep retrying `replace` with permuted old_text — it will never match disk-format text against the injected prompt format.

### Pitfall: Hook Scripts Writing Multi-Line JSON to Log Files

**Problem:** Using `jq` without the `-c` flag produces multi-line JSON output. When appended to a JSON Lines log file (one JSON object per line), this corrupts the format and makes logs unparseable.

**Prevention:** Always use `jq -c` (compact) when writing JSON to log files. Test by running the script and verifying each line is valid JSON: `jq . < logfile`.

### Pitfall: Float Comparison in Bash Using `bc` + `(( ))`

**Problem:** `(( ))` only does integer arithmetic. `bc -l` returns 1 or 0, but `(( ))` can't handle the floating point comparison properly, causing silent failures (e.g., max_severity stays at 0.0).

**Prevention:** Use `awk "BEGIN {exit !($a > $b)}"` for float comparisons in bash. This returns exit code 0 (true) or 1 (false) correctly for any numeric values.

### Pitfall: Hook Scripts Using Wrong Log Directory

**Problem:** Hook templates from Copilot/GitHub use `logs/copilot/` as the log directory. Hermes hooks must use `logs/hermes/` (and `logs/hermes/governance/` for governance audit).

**Prevention:** Always use `$HOME/AppData/Local/hermes/logs/hermes/` as the base log path. Never hardcode `logs/copilot/` in Hermes hooks.

### Pitfall: Relative Paths in hooks.json

**Problem:** Hook templates use relative paths like `.github/hooks/session-logger/log-session-start.sh`. Hermes resolves paths from its own working directory, not the repo root, causing "file not found" errors.

**Prevention:** Always use absolute paths in `hooks.json`: `C:/Users/Alexa/AppData/Local/hermes/hooks/<hook-name>/<script>.sh`.

### Pitfall: Memory Tool Drift After `patch` Writes (Issue #26045)

**Problem:** When the `patch` tool modifies `MEMORY.md` or `USER.md` in `~/AppData/Local/hermes/memories/`, the memory tool's internal state can drift out of sync with the file on disk. Subsequent `memory(action='add')` or `memory(action='replace')` calls may fail with "Refusing to write MEMORY.md: file on disk has content that wouldn't round-trip."

**Symptom:** `memory()` returns a drift error and may create a `.bak.*` snapshot. Repeated retries in the same session usually keep failing even if the file reads back correctly.

**Prevention:**
1. After using `patch()` on any file under `~/AppData/Local/hermes/memories/`, assume `memory()` is temporarily unsafe until the store re-syncs.
2. If you need to update memory after patching, prefer `write_file` for a full clean rewrite rather than incremental patching of memory files.
3. Treat generated `.bak.*` files as artifacts and remove them after inspection.

**Recovery:** If blocked, do not loop `memory()` retries in the same session. Verify the on-disk file, remove any generated `.bak.*` artifacts, and defer the `memory()` update until the next session start when the store re-reads the file. If the content still needs to be captured immediately, rewrite the file cleanly first, then stop using the memory tool for that session.

### Pitfall: `terminal` `mv` Fails on Duplicates — Remove First

**Problem:** When moving many files/directories with `mv`, if a destination already exists, the entire `mv` command fails and stops. In a batch move script, this means all subsequent moves in the same command also fail.

**Symptom:** `mv: cannot move 'X' to 'Y': Directory not empty` — the script exits with error, leaving some files moved and others not.

**Prevention:** Before batch moves, remove duplicates first:
```bash
# Remove duplicates first
rm -rf <root-duplicate-1> <root-duplicate-2>
# Then batch move
mv skill-a category-a/ && mv skill-b category-b/ && ...
```

**Alternative:** Use `execute_code` with `shutil.move()` in Python — it handles duplicates more gracefully and can skip existing destinations.

### Pitfall: Profile-Level Sections Removed from SOUL.md Make It Too Thin

**Problem:** Aggressively de-duplicating SOUL.md by removing sections that "also appear in the system prompt" (like "Finishing the Job", "Memory & Persistence") can make SOUL.md feel thin or skeletal. Those sections are in the system prompt because they apply globally — but SOUL.md is also read by the user and referenced by profiles. Removing them entirely means a human reader of SOUL.md sees no mention of key behaviors.

**Prevention:** When de-duplicating SOUL.md, keep a **minimal forward-reference** to major behavioral sections rather than deleting them entirely. For example, a single "Finishing the Job" bullet under Core Rules is enough — the system prompt has the full text. Don't let purism make the file unreadable. 30 lines of principles that a human can read in 60 seconds is better than 15 lines that omits half the operating model.
