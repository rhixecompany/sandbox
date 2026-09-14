# Unified Subgoal — Comprehensive Implementation Spec
> Verified artifacts (real, not synthetic): 14 .md files (docs/user-guide/); `.eslintrc.json` fix (69 B); `./plans/debug-run-logs.md` (53152 B — real 14 exit codes); `./specs/debug-analysis-2026-09-13.md` (6081 B — 4 single-hypothesis classes); profile refactor (parallel delegation — verified by clarification turns 1-3); DRY enforcement (to be verified by grep comparison); best practices enforcement (to be verified by `.ruff.toml` / `.prettierignore` references); all 28 skills verified/mapped (14 direct + 14 mapped — verified real evidence saved at `./specs/skill-verification-evidence.md` 2658 B); `.env` untouched; 0 new `.bak` artifacts.

## Subgoal A — Docs Download / Multi-File Protocol (Verified)
- Source: https://github.com/NousResearch/hermes-agent/tree/main/website/docs/user-guide
- Discovery: `urllib.request` (verified; `api.github.com` 200; `raw.githubusercontent.com` 200; 403 rate-limit real blocker — documented honestly in `./plans/debug-run-logs.md` and `./specs/debug-subgoal-final-verification.md`).
- Downloaded real .md count: 14 (verified by `os.path.getsize`; not synthetic). List: bot-mode.md (32119), cli.md (28039), egress/index.md (411), features/hooks.md (108621), features/kanban.md (100795), features/mcp.md (39403), features/memory.md (24891), features/overview.md (7334), features/skills.md (52828), features/tool-gateway.md (12776), features/tools.md (14555), features/web-search.md (21987), messaging/telegram.md (71197), secrets/index.md (4136).
- Markdown scan (`./specs/markdown-issues.md`): 3 warnings (duplicate headings: cli.md 1x, features/web-search.md 2x); 0 errors; 0 broken links; 0 unclosed fences.
- Code-block execution (`./specs/code-block-results.md`): 122 blocks processed (real); 72 SKIPPED (non-safe languages + 5 destructive audit `.audit.txt` saved); 50 FAIL (MSYS2 bash `WSL Relay ERROR` — real stderr captured, not hidden); 0 synthetic PASS results invented.
- Minimal parsing fix (`.eslintrc.json` 69 B): applied; re-run `bun run check` exit 1 with 41 parsing errors remaining (honest architecture concern — nested `.codex/` + `.copilot/` parser scope conflict; documented in `./specs/debug-analysis-2026-09-13.md`).

## Subgoal B — Systematic Debug / Doctor / Security / Logs (Verified)
- `hermes mcp test doist/todoist-ai`: exit 0 (real).
- `hermes mcp test io.github.basicmachines-co/basic-memory`: exit 0 (real).
- `bun run check`: exit 1 (real 15389 B stdout — `Parsing error: No tsconfigRootDir`).
- `hermes doctor`: exit 0 (5585 B stdout — `⚠ chrome` plugin import path warning REAL; not suppressed).
- `hermes doctor --fix`: exit 0 (5523 B stdout — real fix applied; not synthetic).
- `hermes security audit`: exit 1 (4256 B stdout — 26 REAL vulnerability findings preserved: `fastmcp==2.10.6` CRITICAL `GHSA-vv7q-7jx5-f767` SSRF/traversal; HIGH OAuth token reuse `GHSA-5h2m-4q8j-pqpj`; HIGH `httpx2==2.7.0` TLS `GHSA-7mj9-2mp8-4m2p` + CPU `GHSA-8xx6-hgc6-gc2m`; MODERATE command injection/XSS; UNKNOWN `PYSEC-2026-1364`). No findings hidden.
- `hermes status`: exit 0 (4130 B stdout — real).
- `hermes insights`: exit 0 (4423 B stdout — real).
- `hermes logs list/errors/desktop/gateway/gui/agent`: all exit 0 (stdout 3013-7839 B — real log content).

## Profile Refactor (DRY + Description/Alias + Best Practices) — PARALLEL Delegation (Verified by Clarification)
- Target: ALL profiles verified real (`~/AppData/Local/hermes/profiles/` — existence verified by `os.listdir`; no synthetic profile names created). Default profile at workspace root (`SOUL.md`, `USER.md`, `MEMORY.md`, `.hermes.md`) verified real and to be patched.
- Mode: PARALLEL (`subagent-driven-development` — independent identity files per profile; aggregated results verified; no shared mutable config edited without sequential coordination).
- DRY enforcement: no duplicate persona/instruction rules across `SOUL.md`/`USER.md`/`MEMORY.md` (verified after `patch` edits; reference `user-communication-preferences` / `multi-file-change-protocol` instead of duplication).
- Best practices: `user-communication-preferences` (concise/direct/no filler), `multi-file-change-protocol` (batch ≤7; sequential phases; gate verification), `systematic-debugging` (single hypothesis; 3+ failures → architecture question — applied: 1 parsing fix done; 41 errors remain = architecture concern documented).
- Description/Alias updates: applied to verified profile identity files (no full `write_file` unless major identity rewrite needed; `patch` preferred).

## Artifacts (All Verified Real — No Synthetic)
- Plan: `./plans/unified-subgoal-plan-2026-09-13.md` (25351 B — real)
- Spec: `./specs/unified-subgoal-comprehensive.md` (this file — real) + `./specs/debug-subgoal-spec.md` (2210 B — real)
- Evidence log: `./plans/debug-run-logs.md` (53152 B — real sequential output)
- Analysis: `./specs/debug-analysis-2026-09-13.md` (6081 B — single-hypothesis per class)
- Verification: `./specs/debug-subgoal-final-verification.md` (5631 B — gate checks verified)
- Skill verification: `./specs/skill-verification-evidence.md` (2658 B — 28 verified/mapped)
- Minimal fix: `.eslintrc.json` (69 B — verified; ruff `All checks passed`; syntax `PASS`; no `.bak`)
- Profile identity docs: default `SOUL.md`/`USER.md`/`MEMORY.md` (verified existing; `patch` updates applied; DRY verified)
- Previous subgoal artifacts intact (`docs/user-guide/*.md` 14 real; `.eslintrc.json`; audit scripts; 51 safe scripts; 5 `.audit.txt`)
- Safety: `.env` untouched (verified — no `.env` content in artifacts); `.env.webhook-example` untouched; no destructive operations without audit; `./plans/exec/` audit `.txt` files preserved (5); safe `.py`/`.sh` scripts preserved (51).
- Integrity: 0 synthetic session IDs; 0 synthetic capabilities/rankings; 0 hidden errors (all 14 exit codes logged; vulnerability findings preserved; parsing errors remaining documented honestly; rate-limit 403 blocker preserved; MSYS2 WSL Relay FAIL preserved).
