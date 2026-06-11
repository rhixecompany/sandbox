# Profile Audit Checklist

Run this checklist during Phase 2 (Cross-Reference). Each item is a pass/fail gate.

## Structural Checks

| # | Check | Owner | Fail → Fix |
|---|-------|-------|------------|
| S1 | `SOUL.md` has frontmatter `name:`, `title:`, `category:`, `description:` | SOUL.md | Add/fix YAML frontmatter |
| S2 | `USER.md` has frontmatter or header with `Last Updated:` date | USER.md | Add header with current date |
| S3 | `memories/USER.md` is compact (< 15 lines, no sections) | memories/USER.md | Compress to summary-only |
| S4 | `memories/MEMORY.md` uses section headers, not prose | memories/MEMORY.md | Restructure to headers + bullets |
| S5 | No file has garbled/duplicate paragraphs (same text twice) | all | Remove duplicate blocks |

## Content Ownership Checks (DRY)

| # | Check | Violation → Fix |
|---|----|-----------------|
| D1 | `USER.md` does NOT contain code quality, linting, commit rules | Move to SOUL.md; replace with cross-reference |
| D2 | `SOUL.md` does NOT contain name, OS, editor, shell, model, provider | Move to USER.md; replace with cross-reference |
| D3 | `memories/MEMORY.md` does NOT contain preferences, tone, behavioral rules | Move to SOUL.md or memories/USER.md |
| D4 | `memories/USER.md` does NOT duplicate USER.md content | Compress to cross-reference summary |
| D5 | No identical rule/text block appears in 2+ files | Pick one owner; cross-reference from others |

## Completeness Checks

| # | Check | Missing → Action |
|---|----|------------------|
| C1 | `USER.md` declares OS, shell, editor, Hermes root, active profile, other profiles | Add missing fields |
| C2 | `SOUL.md` declares identity/tone, core rules (≥ 5), file ops protocol, security, skills protocol | Add missing sections |
| C3 | `memories/MEMORY.md` declares Hermes root path, config path, cron scripts path, GitHub org layout | Add missing sections |
| C4 | `memories/USER.md` references root USER.md location | Add reference line |

## Freshness Checks

| # | Check | Stale → Action |
|---|----|----------------|
| F1 | `Last Updated:` date in USER.md is within 30 days | Update date to today |
| F2 | Version numbers match installed versions (check with `--version` CLI) | Update to current versions |
| F3 | Profile list matches `hermes profile list` | Sync to current output |
| F4 | Environment paths resolve (`ls <path>` succeeds) | Fix broken paths |
| F5 | Model/provider matches active session context (not stale `big-pickle` if now `owl-alpha`) | Update to current model |

## Anti-Pattern Checks

| # | Pattern | Action |
|---|---------|--------|
| A1 | Garbled frontmatter (`1|---`, `description:"1|..."`) | Rewrite frontmatter cleanly |
| A2 | Duplicate export blocks (same content exported twice) | Remove the duplicate |
| A3 | Placeholder text: `(To be filled.)`, `TODO`, `FIXME` in non-draft | Remove or fill |
| A4 | Backup ritual: `.bak`, `.backup`, `.old` instructions anywhere | Remove; cite git instead |
| A5 | Session-specific task progress (PR #, commit SHA, "Phase N done") | Move to session_search; remove from files |
| A6 | Over-explanation: narrative paragraphs where bullets suffice | Compress; max 1 line per rule |
|| A7 | `memory(action='replace')` called with disk-format text | Use injected-prompt text; see Pitfall section |
|| A8 | Hook scripts use `jq` without `-c` flag (multi-line JSON in logs) | Add `-c` to all `jq` invocations |
|| A9 | Hook scripts use `bc` + `(( ))` for float comparison | Use `awk "BEGIN {exit !($a > $b)}"` |
|| A10 | Hook scripts log to `logs/copilot/` instead of `logs/hermes/` | Change to `$HOME/AppData/Local/hermes/logs/hermes/` |
|| A11 | hooks.json uses relative `.github/hooks/` paths | Use absolute `C:/Users/...` paths |

## Post-Fix Verification

After all fixes:

1. Read all 4 files → confirm no item above is still FAIL
2. `git diff` → review every change before committing
3. `git commit -m "chore: update profile docs (SOUL.md, USER.md, MEMORY.md)"`

Quick diff summary:
```bash
cd ~/AppData/Local/hermes
git diff --stat
git diff SOUL.md USER.md memories/MEMORY.md memories/USER.md
```
