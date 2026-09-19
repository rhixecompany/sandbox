---
name: agentic-workflow
title: Agentic Engineering Workflow
version: 1.0.0
author: Alexa
trigger: "Agentic engineering workflow / AGENTS.md merge / profile identity updates / repo workflow initialization"
---

Always-on rules (this user's specs):
- Never invent synthetic session IDs, capabilities, ranking, quality metrics, or verification results.
- Verification-first: verify real behavior (`/check verify` drives the actual app; `/check review` uses a fresh model), not just green tests or code reads.
- Design decisions must be written to files (`docs/specs/`, `AGENTS.md`, profile identity docs), never buried in chat or code comments only.
- Build from approved specs; `/develop` stops and routes back to `/architect` when a load-bearing decision is unmade.
- Fix root cause (`/debug` loop: reproduce → localize → one hypothesis → minimal fix → regression test), not symptoms.
- Document actual changes (`/document`) from real commits/diffs, not AI memory or guesses.
- Reconcile durable state after merge (`/sync` updates `AGENTS.md` with surgical edits; flags stale specs; never overwrites curated prose).
- AGENTS.md updates follow merge discipline: preserve user's existing content (wording, sections, rules); surgical edits only; verify exact commands from repo (`package.json`, `.husky/pre-commit`, `.editorconfig`, `.ruff.toml`, CI); observe conventions (tab indent / lf line endings, conventional commits, branch naming); never expand beyond 100 lines without justification.
- Profile identity updates (`SOUL.md`, `.cursorrules`) include workflow rules honestly (blockers preserved: adminbot/default MISSING, MSYS2 FAIL, rate-limit 403; `.env` protected: 5274 B CWD / 30269 B hermes).
- Marketing/course references from source files are excluded from workflow documentation unless explicitly requested.
- When ambiguous: use `clarify` with explicit multi-select choices before implementing changes.

Procedure (the 9 skills, in order):
1. Scope (`/scope`): Plan before any code. Write to `docs/scope/`. Define what's in v1, what's out, dependencies.
2. Architect (`/architect`): Design against existing constraints. Write spec to `docs/specs/`. Recommend approach + honest alternative with reason it lost. Never bury decisions in code.
3. Develop (`/develop`): Build from approved spec + `AGENTS.md`. If load-bearing decision unmade → stops, routes to `/architect`.
4. Audit (`/audit`): Read actual repo (structure, stack, existing docs, `AGENTS.md`). Write/update `AGENTS.md`; never overwrite curated content; flag conflicts.
5. Check (`/check verify` + `/check review`): Verify real app behavior against spec criteria (`verify`). Code review with fresh model (`review`). Writes to `docs/reviews/`.
6. Test (`/test`): Write test suite for uncommitted changes. Read framework preferences (asks/saves `test/preferences.json`). Strategy: happy path + edge + error + accessibility.
7. Document (`/document`): Human-facing prose from actual diff (`pr` | `changelog` | `release-note` | `postmortem`). No code edits.
8. Debug (`/debug`): Investigate root cause. Reproduce reliably. Narrow smallest failing spot. One theory → test → fix → verify. Include regression test (`/test`). No extra refactors.
9. Sync (`/sync`): Reconcile durable knowledge after change complete. Update `AGENTS.md` (surgical), reconcile scope (`docs/scope/`), flag stale specs. No whole-section rewrites.

Pitfalls (generalizable rules + mechanism, imperative):
- `spellcheck` script in `package.json` is DISABLED (`# cspell disabled - cspell.json removed`). Do not assume `.cspell.json` is active; check script before relying on spellcheck.
- `.editorconfig` says `lf` / `tab` indent; README incorrectly claims CRLF. Trust `.editorconfig` for line endings; don't rely on README claims without verification.
- `.markdownlint-cli2.jsonc` and `.markdownlint.jsonc` must stay in sync. Check both before markdown edits; don't assume one reflects the other.
- Runtime is Bun (`packageManager: bun@1.3.14`), not npm/Node. Use `bun install`, `bun run ...`. Lockfile is `bun.lock`.
- Subprojects (`projects/*`) are autonomous (`AGENTS.md`, own `package.json`/`pyproject.toml`, own CI). Don't apply root scripts to subprojects without checking local `AGENTS.md`.
- `test` at root = vitest; Python = `pytest` with `testpaths = ["projects"]`. Different toolchains; don't assume same command.
- Pre-commit hook (`.husky/pre-commit`): `lint` → `typecheck` → `format:check` → `markdownlint` → `spellcheck`. All must pass before PR.
- `pre-commit` `.pre-commit-config.yaml` checks YAML, JSON, TOML, trailing whitespace, EOF. Install with `pre-commit install`.
- `projects/Bash/` uses multi-wrapper parity (`.sh` + `.ps1` + `.bat`) with `--dry-run`. Never run destructive scripts without `--dry-run` first.
- Full recursive scan for env refs timed out (300s) — honest blocker preserved in session evidence; don't invent results.
- OpenRouter model fetch timed out — real blocker, not resolved; don't claim model list is verified when fetch failed.

References:
- See `references/agentic-skills.md` for the 9 installed skills and their commands.
- See `references/merge-discipline.md` for AGENTS.md merge rules and verification checklist.
