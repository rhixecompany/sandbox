# Plan: Terminal & Agent Ecosystem Full Sync + Repair

- **Date:** 2026-08-12
- **Status:** not_started → in_progress → completed
- **Owner:** Alexa (OWL) | **Branch:** development

## Goal

Debug/fix/configure/test Windows terminal app configs (Git Bash, WezTerm,
PowerShell), bidirectionally sync + verify every installed AI agent's MCP
servers/skills/hooks/plugins (DRY), orchestrate git lifecycle across all
subrepos, consolidate Python scripts into Hermes root (dedupe), repair and
dual-mode (sync+async) every Hermes-root script, create skills for each
script, validate missing files, run `bun run check` (background, no timeout),
then systematic-debug all warnings/errors and fully implement
env-credential-hydration + hermes-diagnostic-repair.

## Current Context (recon 2026-08-12)

- SandBox root: branch `development`, dirty=3 (hook.py, hooks.json,
  SESSION_REPORT.md modified; session_start_capture.py untracked).
- 19 project dirs under `projects/`; **14 have `.git`** (clean, `development`),
  **5 lack `.git`**: `Bash/`, `docs/`, `mcp-servers/`, `mcp-server-typescript/`,
  `Resume_maker/`.
- Terminal configs:
  - `~/.bashrc` (2 lines: `alias python3='python'`, HERMES_GIT_BASH_PATH) —
    **verify alias intent** (memory says python3=3.13.14, python=3.11.15).
  - `~/.bash_profile` (Git-for-Windows generated, sources ~/.profile + ~/.bashrc).
  - `~/.wezterm.lua` (22-line pcall entry) vs `~/.config/wezterm/wezterm.lua`
    (26-line direct-require entry) — **DIVERGENT**, needs bidir sync + module
    loading parity.
  - WezTerm modules: `~/.config/wezterm/{settings,appearance,keys,events,launch}.lua`
    - stray `wezterm.lua` (796B) + `backup-20260731/` — verify module set.
  - pwsh profile exists at `Documents/PowerShell/Microsoft.PowerShell_profile.ps1`
    (structural env vars only, no secrets — good); PS 5.1 profile missing
    (default location WindowsPowerShell) — create if needed.
  - wezterm installed at `C:\Program Files\WezTerm\wezterm`.
- Hermes root scripts: **117 `.py`** in `$LOCALAPPDATA/hermes/scripts/` (plus
  .ts/.ps1/.sh helpers) — needs compile/lint audit, sync+async conversion
  where applicable, tests, and skills.

## Phases

### Phase 1 — Terminal App Config Repair + Bidir Sync

1.1 Audit WezTerm: compare `~/.wezterm.lua` vs `~/.config/wezterm/wezterm.lua`;
unify entry-point behavior (root = pcall fallback, XDG = authoritative).
1.2 Verify module load path works: `wezterm ls-fonts --list-system` or
`wezterm --config-file ... show-keys` smoke test; `wezterm config` check.
1.3 Git Bash: verify `.bashrc` alias correctness vs python3/python reality;
fix if it breaks tooling; keep HERMES_GIT_BASH_PATH.
1.4 PowerShell: verify pwsh profile loads (pwsh -NoProfile -Command ... then
with profile); create PS 5.1 profile symlink/alias if desired; ensure no
secrets embedded (DRY — secrets come from env vault only).
1.5 Write terminal-config skill/docs if missing; validate no duplication.

### Phase 2 — Agent MCP / Skills / Hooks / Plugins Sync (DRY)

2.1 Inventory agents: Hermes (root config.yaml, skills/, hooks/), OpenCode
(`~/.omo/omo.jsonc`), Codex (`~/.codex/`), mirror dirs
(`~/Desktop/SandBox/hermes-profiles/`), `.github/hooks/SandBox`.
2.2 Run `verify_sync.py` (65 checks) from hermes-profiles; capture drift.
2.3 Sync drift using multi-agent-sync workflow; re-verify until clean.
2.4 Verify MCP servers live: `hermes mcp health` / mcp-server-health skill;
confirm no duplicate configs (DRY).

### Phase 3 — Git Multi-Repo Orchestration

3.1 Auth gate: `gh auth status`; baseline dirty counts per repo.
3.2 Per-repo loop (14 with .git): fetch, add, commit (conventional), push to
`development`, pull; parent submodule pointer bump LAST.
3.3 Missing repos (5): `git init` + remote add + fetch (no destructive ops
without approval; no force-push).
3.4 PR lifecycle: open PRs review-then-merge only where branches exist.
3.5 Verify sweep: all repos clean, submodules clean, expected PRs only.

### Phase 4 — Python Script Consolidation → Hermes Root (DRY, dedupe)

4.1 Inventory Python files in: `./` (SandBox root), `%TEMP%` (windows temp),
`./scripts`, `./.github/prompts`, `./.github/scripts`, `./.hermes`,
`./.copilot`, plus each subrepo.
4.2 Copy unique (non-duplicate) Python files to
`$LOCALAPPDATA/hermes/scripts/` (skip existing identical content).
4.3 Delete duplicates NOT in Hermes root — only files whose content hash
matches a Hermes-root file; keep git-tracked originals safe; report
every deletion. **Destructive gate:** approval before mass delete.

### Phase 5 — Hermes Root Script Repair + Sync/Async Conversion

5.1 Batch `python -m py_compile` + `ruff check --fix` all 117 scripts;
fix class-level issues.
5.2 Audit each script for async-able IO (http/network/file loops) —
convert to sync+async dual-mode where sensible (CLI flag or `asyncio.run`
wrapper); do NOT rewrite working scripts gratuitously.
5.3 Add/adjust tests: `tests/` at hermes-agent repo or per-script harness;
run targeted tests, capture pass counts.

### Phase 6 — Skills for Each Hermes Script

6.1 For scripts lacking a backing skill, create SKILL.md (frontmatter +
body) or patch existing skill (check duplicates first — DRY).
6.2 `hermes skills check` + `hermes skills update` to validate install.

### Phase 7 — Create/Update/Validate Missing Files

7.1 Diff expected vs actual: configs, prompts, scripts, skills, hooks.
7.2 Create missing; update stale; validate with existing validators
(frontmatter, prompts, vscode, skills).

### Phase 8 — `bun run check` (background, no timeout)

8.1 Launch `bun run check` background=true notify_on_complete=true at
SandBox root; capture output on completion; fix reported issues.

### Phase 9 — Systematic Debugging Sweep

9.1 Collect warnings/errors from Phase 8 + logs; classify; root-cause each;
fix in order; re-verify.

### Phase 10 — env-credential-hydration (full implementation)

10.1 Vault inventory `~/Desktop/Github/*.txt`; validate-then-sync workflow:
`vault_key_validate.py --json` → `vault_key_sync.py --apply` (dry-run
first); masked verification; `.env` gitignored check.

### Phase 11 — hermes-diagnostic-repair (full implementation)

11.1 Diagnostic battery: doctor, doctor --fix, security audit, status,
insights, skills audit/check/update, logs list/errors/desktop/gateway/
gui/agent. Classify findings; fix real bugs; verify with tests.

## Files likely to change

- `~/.wezterm.lua`, `~/.config/wezterm/wezterm.lua` (+ modules)
- `~/.bashrc`, pwsh profiles
- `$LOCALAPPDATA/hermes/scripts/*.py` (repairs, conversions)
- `$LOCALAPPDATA/hermes/skills/**` (new SKILL.md per script)
- `~/Desktop/SandBox/projects/**` (git commits)
- `~/Desktop/SandBox/.env` + hermes root `.env` (hydrated keys, masked)

## Validation

- `wezterm` smoke test, `pwsh` profile load test
- `verify_sync.py` clean, `hermes skills check` → 0 updates
- `python -m py_compile` all scripts; ruff clean; tests pass
- `bun run check` exit 0 (or documented fixes)
- `gh pr list` expected only; repos clean
- `git check-ignore .env` exits 0; masked key verification

## Risks / Tradeoffs

- **Destructive:** duplicate deletion (Phase 4.3) and git ops (Phase 3)
  require approval gates; no force-push; no commit unless asked per repo
  batch (user invoked orchestration explicitly — treat as approval).
- **Scale:** 117 scripts + 19 subrepos — batch processing, one class of fix
  at a time; don't touch working code gratuitously (sync/async conversion
  only where IO-bound and safe).
- **Windows quirks:** CRLF vs LF, MSYS_NO_PATHCONV for native Python,
  read-only .git pack files block rmtree (MSYS rm -rf first).

## Open Questions

- Alias `python3='python'` in .bashrc: intentional (3.11) or broken? Verify
  against tooling expectations before changing.
- 5 repos without .git: initialize + remote, or report only? (No remote URLs
  known for Bash/, docs/, mcp-servers/, mcp-server-typescript/,
  Resume_maker/ — will report unless remotes found.)
