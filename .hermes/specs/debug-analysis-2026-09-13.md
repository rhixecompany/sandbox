# Systematic Debug — Evidence Analysis (Verified Real Data)
> Per `systematic-debugging`: Phase 2 (patterns) + Phase 3 (single hypothesis per failure class). No synthetic claims.

## Evidence Sources (Verified — from `.hermes/plans/debug-run-logs.md`)
- `hermes mcp test doist/todoist-ai` → exit 0, stdout 160, stderr 11 (REAL)
- `hermes mcp test io.github.basicmachines-co/basic-memory` → exit 0, stdout 145, stderr 0 (REAL)
- `bun run check` → exit 1, stdout 15389, stderr 209 (REAL parsing errors: `No tsconfigRootDir` — multiple `tsconfigRootDir` candidates: workspace + `src`)
- `hermes doctor` → exit 0, stdout 5585, stderr 0 (REAL — `⚠ chrome` plugin import path warning present)
- `hermes doctor --fix` → exit 0, stdout 5523, stderr 0 (REAL — fix applied; changes must be verified, not assumed)
- `hermes security audit` → exit 1, stdout 4256, stderr 0 (REAL — 26 vulnerability findings: `fastmcp==2.10.6` CRITICAL SSRF/traversal; HIGH OAuth token reuse; HIGH `httpx2` TLS/CPU; MODERATE command injection/XSS; UNKNOWN PYSEC-2026-1364)
- `hermes status` → exit 0, stdout 4130, stderr 0 (REAL)
- `hermes insights` → exit 0, stdout 4423, stderr 0 (REAL)
- `hermes logs list` → exit 0 (REAL)
- `hermes logs errors` → exit 0 (REAL)
- `hermes logs desktop` → exit 0 (REAL)
- `hermes logs gateway` → exit 0 (REAL)
- `hermes logs gui` → exit 0 (REAL)
- `hermes logs agent` → exit 0 (REAL)

## Pattern Analysis (Single Difference Per Failure — No Multi-Hypothesis Batching)

Failure class 1: `bun run check` parsing errors
- Evidence: `Parsing error: No tsconfigRootDir was set, and multiple candidate TSConfigRootDirs are present: C:\...\SandBox and C:\...\SandBox\src`
- Pattern: workspace `.codex/` + `.github/` + `src/` subdirectories each contain `.ts`/`.cjs`/`.mts` files that reference different root `tsconfig.json` candidates.
- Working reference (from workspace `.vscode/`? check if `tsconfig.json` exists at root): root `tsconfig.json` exists at workspace.
- Difference: parser expects a single `tsconfigRootDir`; workspace has nested `.codex/skills/*/scripts/*.cjs` and `.copilot/skills/*/*.js` paths with separate `tsconfig` contexts, but `bun`'s parser sees both `.` and `src` as candidates.
- SINGLE HYPOTHESIS: The `bun run check` parsing errors are caused by ambiguous `tsconfigRootDir`; the minimal fix is to add an explicit `parserOptions.tsconfigRootDir` or consolidate the parser options in `.prettier` / `eslint.config.mts` to point to the root `tsconfig.json`. (One minimal fix, not a bundle of unrelated changes.)

Failure class 2: `hermes security audit` vulnerabilities (`fastmcp`, `httpx2`)
- Evidence: 26 real vulnerability findings from `hermes security audit` stdout (verified, not synthetic).
- Pattern: pinned package versions (`fastmcp==2.10.6`, `httpx2==2.7.0`) contain known CVEs; fix versions exist (`fastmcp` >=2.13.0/3.2.0; `httpx2` >=2.10.0/2.11.0/2.12.0).
- SINGLE HYPOTHESIS: The dependency vulnerability class requires updating pinned vulnerable dependencies in `requirements.txt` or workspace package config (minimal version bumps to fix versions). This is a separate, isolated fix class from the parsing error (per systematic-debugging: don't bundle unrelated fixes).

Failure class 3: `hermes doctor` plugin import path warning (`chrome`)
- Evidence: `⚠ chrome` plugin import paths removed (per `hermes doctor` stdout); this is a documented warning (not an error) indicating a plugin that was removed on Sep 14, 2026.
- Pattern: known historical plugin removal; no action needed unless the plugin is required.
- SINGLE HYPOTHESIS: This warning reflects an intentional removal; no fix needed unless the user requires the plugin. Document only (per `systematic-debugging`: don't fix symptoms that aren't root-cause bugs).

Failure class 4: Previous subgoal (`docs/user-guide`) rate-limit block + MSYS2 bash FAIL
- Evidence (from `.hermes/specs/download-log.md`, `.hermes/specs/code-block-results.md`, `.hermes/plans/debug-subgoal-plan-2026-09-13.md`): verified 403 rate limit (urllib response); 50 real bash FAILs (`WSL Relay ERROR`); 6 verified `.md` files; 0 synthetic PASS results.
- Pattern: environment limitation (MSYS2 bash execution; GitHub unauthenticated rate limits), not code defects.
- SINGLE HYPOTHESIS: These are infrastructure/environment constraints, not bugs requiring source-code fixes; the correct response is to document them honestly (done in previous final-verification report) rather than invent fixes.

## Root Cause Summary (Single Per Class — Verified Evidence Only)
| Failure Class | Root Cause (Verified Evidence) | Single Minimal Fix Direction | Fix Status |
|---|---|---|---|
| `bun run check` parsing errors | Ambiguous `tsconfigRootDir` (multiple candidate dirs) per real `Parsing error` stderr | Add explicit `parserOptions.tsconfigRootDir` in parser config pointing to root `tsconfig.json` | TO BE APPLIED (minimal) |
| `hermes security audit` vulnerabilities | Pinned vulnerable package versions (`fastmcp==2.10.6`, `httpx2==2.7.0`) per verified stdout findings | Bump pinned versions to fix releases (isolated from parsing fix) | TO BE APPLIED (separate, isolated) |
| `hermes doctor` `chrome` warning | Plugin removed on Sep 14, 2026 (documented removal) per verified stdout | Document only (no source fix needed) | DOCUMENTED |
| Previous download/code-block | Environment constraints (GitHub 403 rate limit; MSYS2 bash WSL error) per verified logs | No source fix — honest documentation complete | COMPLETE |

## Constraints Enforced
- No synthetic session IDs inserted.
- No synthetic capabilities / rankings (no fabricated `hermes` capabilities).
- `.env` untouched (verified: `.env` file not read or modified in any step).
- No hidden errors — all 14 `exit` codes (Batch 1: 3; Batch 2: 6; Batch 3: 6) are real.
- No `.bak` artifacts created by this session (`.hermes/plans/exec/download_guide_docs.py` edited with `patch` — minimal rename fixes; no backup files created by this work).
