# SPEC: Five-Goal Platform Remediation

> Date: 2026-08-28
> Workspace: C:\Users\Alexa\Desktop\SandBox
> Hermes home: C:\Users\Alexa\AppData\Local\hermes
> Profile: default (miniMax via OpenRouter, current session)

## Context

User invoked a five-goal, sequential pipeline covering all major surface area of
the Hermes/SandBox ecosystem. Each goal depends on the previous ("and only then")
so the work is partitioned into 5 phases with hard inter-phase gates.

Prior sessions (2026-06..2026-08-28) produced a deep infrastructure:
- `scripts/profile_config_audit.py` — reports missing context files per profile
- `scripts/mcp_audit.py` + `scripts/mcp_sync.py` — MCP config drift detection
- `scripts/agent_provider_matrix.py` — noninteractive provider+profile runner
- `scripts/disk_cleanup.py` — safe cache cleanup with dry-run
- `.mcp/registry.json` — single source of truth (32 servers)
- `agent_provider_matrix.md` plan + `agent-provider-matrix-spec.md` (Goals 2/3 work is done)
- `mcp-audit-2026-08-28/` (Goal 3 work is done)

This spec covers the remaining surface area and tightens the existing assets.

## Goals (verbatim, numbered)

1. **Context-file unification.** Search, identify, list, triage, debug, fix,
   enhance, verify SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md,
   CLAUDE.md, .cursorrules in the repo, sub-repos, hermes root, and every
   hermes profile. Use best practices, DRY, and minimize token usage by
   preferring MCP server tools.

2. **Authorized-provider matrix.** Run `hermes auth list` to enumerate every
   authorized provider. Read `packages/**/*` and build noninteractive
   scripts, skills, and hooks that execute one request against every
   installed AI agent and every authorized provider, and report the result
   with provider, context, max-output, and capabilities.

3. **MCP server sync.** Configure, debug, fix, test, and enable every
   installed MCP server. Inspect `.github/mcp.json`, copilot, codex, hermes
   configs. Recommend, debug, fix, test additional MCP servers. Sync and
   verify hermes, copilot, codex, and opencode MCP server configurations.

4. **Disk cleanup + Ollama setup.** Free disk by uninstalling winget, choco,
   and Windows apps. Install, configure, and test Ollama locally with the
   best small model that supports vision and reasoning. Wire that model
   into hermes, copilot, codex, and opencode.

5. **Final verification.** Execute
   `hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent && bun run check`
   and systematically debug, fix, and verify every bug, issue, warning, or
   error that surfaces.

## Hard constraints

- "Only then" is a hard gate. Phase N does not start until Phase N-1 reports
  green.
- Disk is critically low (~1.4 GB free at session start). Destructive disk
  operations (cleanups, app uninstalls) require either a successful dry-run
  first or an explicit user confirmation.
- `config.yaml` edits go through `hermes config set`. Direct YAML edits are
  prohibited per user-communication-preferences.
- No backup files. Git is the rollback channel.
- DRY: no duplicated facts across profiles. Pointers + cross-references.
- MCP-first tool precedence per `user-communication-preferences`.

## Scope decisions

- **Provider scope (Goal 2):** 9 unique providers authorized (copilot,
  deepseek, gemini, huggingface, nous, ollama-cloud, openai-codex,
  opencode-zen, openrouter, xai, xai-oauth — 11 entries, 9 unique). Use
  `hermes auth list` as the source of truth.
- **Ollama model (Goal 4):** Choose a single ~3-5 GB vision+reasoning model
  that fits in remaining disk after cleanup. Candidates: `gemma3:4b`
  (~3.3 GB, multimodal), `llama3.2-vision:11b` (~7.9 GB, may exceed budget),
  `qwen2.5vl:3b` (~3.2 GB, vision). Decision recorded at execution time.
- **App uninstalls (Goal 4):** Limited to applications the user has not
  used in 30+ days. Requires explicit confirmation.
- **MCP sync (Goal 3):** Apply changes only to disk configs. Live hermes
  config (`config.yaml`) stays source of truth; disk configs (opencode,
  codex, copilot, vscode) are synced from `.mcp/registry.json`.

## Deliverables (per goal)

| Goal | Spec | Plan | Script/Skill | Artifact |
|------|------|------|--------------|----------|
| 1 | this file | PLAN.md §1 | `scripts/profile_config_fix.py` + `skills/devops/profile-context-unification` | `profile-config-fix-report.json` + populated missing context files |
| 2 | this file | PLAN.md §2 | existing `agent_provider_matrix.py` + `agent-provider-matrix-runner` skill | `agent-provider-matrix-results.json` |
| 3 | this file | PLAN.md §3 | existing `mcp_audit.py` + `mcp_sync.py` | synced disk configs + new `mcp-validation-report.md` |
| 4 | this file | PLAN.md §4 | new `scripts/ollama_setup.py` | Ollama model running + cross-agent wiring verified |
| 5 | this file | PLAN.md §5 | n/a (verification commands only) | `final-verification-report.md` |

## Acceptance criteria

- **G1 (Goal 1):** `python scripts/profile_config_audit.py` reports 0
  `file_missing` issues for any of the 7 context files in any of the 14
  profiles. Each missing file is either (a) populated with a valid skeleton
  pointing to the canonical source, or (b) explicitly waived with rationale
  recorded in the audit report.
- **G2 (Goal 2):** `python scripts/agent_provider_matrix.py --dry-run` exits 0
  and shows the full provider × profile matrix. At least one cell is run
  live and produces a result row with provider, profile, model, request
  echo, response preview, context, max-output, and capability tags.
- **G3 (Goal 3):** All four disk MCP configs (opencode, codex, copilot,
  vscode) pass `python scripts/mcp_audit.py` with 0 FAIL. Disabled hermes
  servers (atlassian, docs, postgres) are documented in the audit report.
- **G4 (Goal 4):** `ollama list` shows at least one vision-capable model.
  `curl http://localhost:11434/api/tags` returns it. At least one of
  hermes/copilot/codex/opencode is configured to use it. Disk free after
  cleanup is reported.
- **G5 (Goal 5):** All 12 verification commands execute. Failures are
  cataloged, root-caused, and either fixed or documented. The final report
  shows pass/warn/fail counts.

## Risks

- **R1 — Disk-full mid-execution.** Mitigation: dry-run every cleanup
  before mutation; report free space at each gate.
- **R2 — Ollama model too large for free disk.** Mitigation: pick smallest
  vision-capable model; record decision; skip cross-agent wiring if no
  model can be pulled.
- **R3 — Profile config edits break inheritance.** Mitigation: each
  generated context file is a thin pointer to the canonical source; never
  duplicates rules already in `~/AppData/Local/hermes/SOUL.md` or
  `MEMORY.md`.
- **R4 — MCP sync overwrites user customizations.** Mitigation: backup
  registry once; never overwrite; only add missing servers.
- **R5 — Provider matrix triggers quota limits.** Mitigation: live cells
  are limited (default `--limit-cells 1`); full matrix is dry-run only.
- **R6 — `bun run check` cspell false-positives.** Mitigation: known
  non-issue; the script must be re-run after cspell dictionary updates.
