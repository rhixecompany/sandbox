---
name: hermes-ecosystem-reliability
title: Hermes ecosystem startup, MCP, client, and rate-limit reliability
status: in_progress
created_at: 2026-09-05T08:45:56Z
owner: Alexa
profile: ops
---

# Hermes Ecosystem Reliability — Master Implementation Plan

## Goal

Debug, repair, enhance, and verify the Hermes session lifecycle, instruction/context layers, MCP/client projections, root Hermes script quick commands, and provider failure handling without resetting the existing dirty working tree or exposing secrets.

## Scope

1. **Session lifecycle** — startup/end hooks, session report generation, profile identity, memory validation, hook approvals, Windows path/locking behavior.
2. **Context/system prompts** — repository and Hermes instruction layers, stale profile/client references, duplicate/conflicting rules, structural validation.
3. **MCP/client synchronization** — `.mcp/registry.json` as the repository source, OpenCode/Codex/Copilot/VS Code projections, Hermes `config.yaml` reconciliation through Hermes CLI only, live MCP tool discovery and connectivity.
4. **Root scripts and quick commands** — every script in the canonical Hermes root scripts directory must have a valid, executable, tested `quick_commands` entry in live Hermes configuration and pass the scripts judge.
5. **Provider resilience** — bounded, policy-compliant retry/backoff/jitter, `Retry-After` handling, provider fallback, circuit breaking, and clear terminal failure; never evade quotas or abuse provider limits.
6. **Skills/plugins/hooks** — repair existing class-level skills and scripts where defects are proven; do not create duplicate one-off skills.

## Non-goals and safety constraints

- Do not reset, restore, delete, commit, push, or rewrite the pre-existing dirty tree.
- Do not read, print, copy, hash, or synchronize secret values from `.env`, credential files, or tokens. Inventory variable names and presence only.
- Do not claim Copilot/Codex/OpenCode/Hermes connectivity unless the real client/tool invocation verifies it.
- Do not bypass provider quotas. “Rate-limit bypass” means compliant retry/backoff/fallback, not quota evasion.
- Modify Hermes `config.yaml` only through supported Hermes CLI commands (`hermes config set`, `hermes mcp add/remove`, hook registration commands); never patch it directly.
- Keep changes bounded to files proven to own a defect. Use `patch` for existing files and `write_file` for new files.

## Baseline evidence (2026-09-05)

- Repository: `C:/Users/Alexa/Desktop/SandBox`, branch `clean-development`, 794 porcelain entries before this plan; extensive pre-existing prompt deletions and modifications are preserved.
- Active live profile: `ops`; live profile list contains 14 profiles, including `ops`, but not `adminbot`.
- Hermes MCP inventory: 27 listed servers; `postgres` is disabled; remaining listed servers are enabled in the live listing.
- Hooks: 14 configured entries. `post_tool_call`, `pre_tool_call`, and `subagent_stop` entries are not allowlisted. Several approved lifecycle scripts were modified after approval and require doctor/re-approval.
- `hermes config check`: passes (config version 40); optional provider variables are mostly absent, which is not itself a failure.
- Existing `scripts/mcp_sync.py` projects registry data to OpenCode, Codex, Copilot, and VS Code but intentionally omits applying Hermes configuration; its validator and sibling tools require review for schema drift and secret safety.
- Existing `scripts/validate-mcp-servers.py` loads `.env` values and emits previews; this is unsafe and can misclassify HTTP MCP endpoints because it relies on `HEAD`.
- Existing instruction/plugin audits contain heuristic parsing and stale profile/event assumptions; they require evidence-backed fixes rather than blind normalization.
- Existing plan/spec fragments overlap. Preserve them as historical inputs and use this file as the single execution order.

## Approach decision

Use one canonical registry plus generated projections and secret-safe validators. This is safer than broad hand-edits, testable across clients, and avoids upstream/vendor changes. Treat unavailable authentication or removed clients as explicit blockers.

## Phases and gates

### Phase 0 — Freeze evidence and inventory (read-only)

**Tasks**

- Capture baseline status, branch, profile/model, Hermes version/config status, MCP list, hooks list/doctor, plugins, and client executable availability.
- Inventory all `SESSION_REPORT.md`, `SOUL.md`, `USER.md`, `MEMORY.md`, `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, Copilot instructions, OpenCode/Codex/Copilot/VS Code configs, `.env*` names, and `config.yaml` paths under the repo and Hermes home without emitting values.
- Audit existing `.hermes/plans/` and `.hermes/specs/` and identify superseded/duplicate fragments without deleting them.
- Run the existing safe audits in report-only mode and save evidence under a new dated report directory; do not overwrite unrelated reports.
- Verify the live MCP server exposes the required filesystem, ast-grep, memory, sequential-thinking, and code-sandbox tools.

**Gate**

- Inventory is complete, secret-safe, and the actual live state is recorded. Any missing executable, authentication wall, or malformed config is classified as a blocker before fixes.

### Phase 1 — Author and validate the specification

**Tasks**

- Create `.hermes/specs/hermes-ecosystem-reliability-spec.md` with requirements, invariants, failure taxonomy, acceptance criteria, ownership per file, and explicit non-goals.
- Link this master plan to the spec and list all historical source plans.
- Define machine-checkable assertions for: lifecycle report fields, context consistency, client projection equality, Hermes/registry server-set reconciliation, quick-command coverage, rate-limit behavior, and no-secret output.

**Gate**

- Spec parses as Markdown/frontmatter, every requirement maps to a verification command or test, and no requirement requires destructive cleanup of the baseline.

### Phase 2 — Root-cause repair: lifecycle and context layers

**Tasks**

- Trace `session-logger` start/end capture and `generate_session_report.py`; reproduce start and end flows with temporary/test session data and verify `SESSION_REPORT.md` contains real continuity fields.
- Repair Windows-safe path handling, log rotation/lock handling, exit-code propagation, and idempotent report generation only where reproduced.
- Reconcile live profile names and model/provider identity in context files. Replace stale `adminbot` assumptions with the verified operations profile mapping while preserving canonical ownership and avoiding duplicate policy text.
- Repair the instruction audit’s false-positive stale/conflict rules and path classification; add regression fixtures for stale references, genuine conflicts, and duplicate layers.
- Run memory validation across all profiles; reduce or structurally repair over-limit memory only through the approved memory workflow, never by dropping facts silently.
- Run `hermes hooks doctor`; re-register or re-approve only modified/not-allowlisted hooks after their commands and hashes are verified. Do not weaken the allowlist.

**Gate**

- Simulated startup/end lifecycle passes twice, report is regenerated with verified fields, all active context layers pass structural and consistency checks, and hooks doctor reports no unexplained unsafe entries.

### Phase 3 — Root-cause repair: MCP registry and client projections

**Tasks**

- Validate `.mcp/registry.json` against each target schema and compare normalized enabled server sets, transports, commands, arguments, URLs, and env placeholder names (never values).
- Repair `scripts/mcp_sync.py` so projection is deterministic, preserves intentional non-MCP client settings, handles local/remote schema differences, and has a dry-run plus strict verification mode.
- Generate and verify `.vscode/mcp.json`, `.codex/mcp.json`, `.copilot/mcp.json`, and `opencode.json` from the registry only when the diff is attributable to the requested sync. Do not overwrite unrelated settings.
- Reconcile Hermes MCP through CLI-supported operations and record any registry entries that cannot be represented or authenticated in Hermes.
- Replace or quarantine the unsafe legacy MCP validator with a secret-safe validator that uses transport-appropriate probes and distinguishes disabled, configured, reachable, authenticated, tool-discoverable, and failed states.
- Exercise every enabled MCP server and required tool discovery path. Record remote authentication/authorization failures as blockers with exact evidence.

**Gate**

- All four disk projections normalize equal to the registry; Hermes reconciliation is explicit; every enabled server has a verified status; no validator/report emits secret material.

### Phase 4 — Root script quick-command contract

**Tasks**

- Inventory every executable script in `C:/Users/Alexa/AppData/Local/hermes/scripts` and inspect its `--help`/quick-command contract.
- Compare script inventory to live Hermes `quick_commands` using a parser, not hand-counted output. Detect missing, duplicate, invalid, unsupported, and non-executable entries.
- Repair the canonical quick-command generator/registry and its tests so all scripts have stable command names, valid arguments, safe timeouts, and deterministic output. Keep aliases explicit and avoid implicit provider/secret expansion.
- Update the installed `scripts-judge` skill/related prompt only after reading the current skill and references; encode the invariant that every root script must be represented and smoke-tested in live config.
- Run the judge, all script self-tests, and a full smoke pass. Persist machine-readable evidence and verify the count programmatically.

**Gate**

- `missing=0`, `duplicate=0`, `invalid=0`, every command smoke-tests successfully, and the declared total exactly matches the enumerated records.

### Phase 5 — Provider resilience and rate-limit handling

**Tasks**

- Audit the existing rate-limit layer and call sites before changing behavior. Identify where 429/usage-limit responses are parsed and where provider fallback is selected.
- Implement bounded exponential backoff with jitter, `Retry-After` support, per-provider attempt budgets, cooldown/circuit-breaker state, and fallback to an explicitly configured provider/model. Do not retry non-rate-limit permanent failures or loop indefinitely.
- Add deterministic tests for 429 with/without `Retry-After`, malformed headers, exhausted attempts, provider fallback, cancellation, and secret-safe error messages.
- Verify real provider/model health with the configured credentials without printing credentials or pretending an unconfigured client is healthy.

**Gate**

- Tests prove bounded behavior and correct fallback; live probes either pass or produce a precise external blocker; no quota-evasion behavior exists.

### Phase 6 — Cross-client and platform verification

**Tasks**

- Verify `hermes`, `opencode`, `code`/VS Code, `codex`, and `copilot` versions and their MCP configuration/diagnostic commands where installed.
- Run OpenCode, Codex, Copilot, and VS Code static config validation plus a minimal MCP tool invocation for each available client. Separate “not installed”, “not authenticated”, “configuration invalid”, “server unreachable”, and “tool invocation failed”.
- Verify the live Hermes profile and operations routing after all changes; switch to `code-architect` for repository code review/implementation passes and return to `ops` for platform verification.
- Verify all modified skill files with their judge/validator and all generated plans/specs with frontmatter and link checks.

**Gate**

- Every available client either passes its real MCP smoke test or has a documented, reproducible external blocker. No unavailable Copilot provider is represented as working.

### Phase 7 — Full regression and completion report

**Tasks**

- Run targeted Python tests and all applicable repository gates: `bun run lint`, `bun run typecheck`, `bun run check`, `bun run format`, `git diff --check`, JSON/YAML/frontmatter validation, scripts judge, lifecycle simulations, MCP sync verification, and client probes.
- Re-run session start/end capture and generate the final `SESSION_REPORT.md`; verify the exact file contents and report path.
- Update the master plan/spec with checked acceptance criteria, actual command outputs, remaining blockers, and lessons. Do not mark external systems complete without read-back evidence.
- Record only durable workflow lessons in the relevant skill; do not add transient task state to global memory.

**Gate**

- All acceptance criteria are checked or have a precise external blocker. Baseline changes remain distinguishable from this work. Final report contains no secrets.

## Expected change sets (subject to Phase 0 evidence)

**Repository**

- `.hermes/specs/hermes-ecosystem-reliability-spec.md` (new)
- This plan (new)
- `scripts/mcp_sync.py`
- `scripts/validate-mcp-servers.py` or a replacement with a safe name
- `scripts/hermes_config_audit.py`
- `scripts/instruction_audit.py`
- `scripts/plugins_hooks_audit.py`
- `scripts/hermes_quick_commands.py` and its tests/fixtures if present
- `.mcp/registry.json`, `.vscode/mcp.json`, `.codex/mcp.json`, `.copilot/mcp.json`, `opencode.json` only when Phase 0 proves the registry is the intended owner
- Context files only for proven stale/conflicting references

**Hermes-managed assets**

- `C:/Users/Alexa/AppData/Local/hermes/config.yaml` only through Hermes CLI
- `C:/Users/Alexa/AppData/Local/hermes/hooks/**` and approval records only through the hook lifecycle workflow
- Installed skills such as `scripts-judge` and `rate-limit-bypass` only through `skill_manage` after current content/references are audited

## Verification matrix

| Requirement | Evidence |
|---|---|
| Startup/end lifecycle | start/end capture artifacts, regenerated `SESSION_REPORT.md`, hook doctor, repeat run |
| Context consistency | instruction audit JSON, profile/config cross-reference check, frontmatter validation |
| MCP sync | normalized registry/projection diff, Hermes CLI reconciliation, per-server tool discovery |
| Quick commands | inventory JSON, live `quick_commands` parse, script smoke results, scripts judge |
| Rate limits | deterministic unit tests and bounded live provider probe |
| Client health | client version/config validation and minimal real MCP invocation |
| Secret safety | validator tests plus scan of generated reports for values/tokens |
| Repository integrity | baseline status comparison, targeted diff review, all build/lint/type/check gates |

## Rollback

- Repository edits: revert only files changed by this plan using targeted git restore/patch after user approval; never reset the full tree.
- Hermes config: reverse changes with the corresponding Hermes CLI command and verify read-back.
- Hooks/skills: use recorded approval and skill version/file diffs; do not delete historical artifacts.
- Client projections: regenerate from the last verified registry; preserve non-MCP settings.

## Progress log

- [x] Baseline captured and user authorized proceeding while preserving the dirty tree.
- [x] Live profile switched to `ops` and verified.
- [x] Mandatory and domain skills loaded/reloaded; sequential reasoning completed.
- [x] Initial live inventory captured.
- [ ] Phase 0 evidence artifacts complete.
- [ ] Phase 1 specification complete.
- [ ] Phase 2 lifecycle/context repairs complete.
- [ ] Phase 3 MCP/client repairs complete.
- [ ] Phase 4 quick-command contract complete.
- [ ] Phase 5 rate-limit resilience complete.
- [ ] Phase 6 cross-client verification complete.
- [ ] Phase 7 regression/completion report complete.
