# ACPX Agents Verification Report

**Date:** 2026-05-30
**Method:** Runtime smoke matrix + control-point config audit

## Scope

- Hermes CLI and Hermes machine config
- ACPX registry and execution paths
- Qwen CLI and settings
- OpenCode CLI/auth/config and ACPX handoff behavior
- Copilot CLI one-shot liveness
- Repo routing docs and agent descriptors

## Runtime Evidence Matrix

| Check | Result | Evidence |
|---|---|---|
| `hermes doctor` | PASS | Doctor completed, config and tools detected |
| `hermes --version` | PASS | `Hermes Agent v0.15.1` |
| `opencode --version` | PASS | `1.15.12` |
| `opencode auth list` | PASS | Copilot, Google, OpenCode Zen credentials listed |
| `copilot --version` | PASS | `GitHub Copilot CLI 1.0.56` |
| `qwen --version` | PASS | `0.17.0` |
| `acpx --version` | PASS | `0.10.0` |
| `acpx qwen exec "...QWEN_ALIVE"` | PASS | Returned `QWEN_ALIVE` |
| `acpx opencode exec "...OPENCODE_ALIVE"` | PASS (DEGRADED) | Returned `OPENCODE_ALIVE` with NDJSON parse warnings |
| `copilot -p "...COPILOT_ALIVE"` | PASS | Returned `COPILOT_ALIVE` |

## Support Buckets

### Confirmed working

- Hermes CLI health and version commands
- ACPX orchestration binary and direct agent calls
- Qwen via ACPX exec path
- OpenCode via ACPX exec path (response path works)
- Copilot one-shot prompt path

### Confirmed broken or degraded

- OpenCode ACPX stream parsing is degraded on this stack when non-JSON plugin preamble lines are emitted before ACP JSON payloads.

### Documented but unverified

- Hermes-mediated OpenCode provider routing via `opencode-acp` in current live config.
- Any claim requiring `~/.qwen/mcp-servers.json` (file is not present in this environment).

## Architecture Decision

1. Keep Hermes ACP providers limited to paths verified in active machine config (`copilot-acp`, `qwen-code`).
2. Treat OpenCode as a direct ACPX target (`acpx opencode exec`) unless Hermes provider wiring is explicitly configured and re-verified.
3. Do not label OpenCode Hermes-provider support as confirmed until a dedicated Hermes-provider smoke test passes.

## Ownership Map

- Live machine authority:
  - `%LOCALAPPDATA%/hermes/config.yaml`
  - `%USERPROFILE%/.acpx/config.json`
  - `%USERPROFILE%/.qwen/settings.json`
  - `%USERPROFILE%/.config/opencode/opencode.json`
- Repo mirrors and guidance:
  - `.github/agents/*.agent.md`
  - `.opencode/rules/acpx-integration.md`
  - `.opencode/skills/**/SKILL.md`
  - `AGENTS.md`, `docs/agents-cross-reference.md`, `docs/specs/*.md`
- Historical, non-authoritative artifacts:
  - Older ACPX plan/spec/report documents unless re-validated against runtime

## Reconciled Provider Naming

- ACPX agent names: `qwen`, `opencode`, `hermes`, `copilot`
- Hermes ACP provider names in active config: `copilot-acp`, `qwen-code`
- OpenCode routing in this stack: direct ACPX target, not currently an active Hermes provider route
- Hermes ACP command form: `hermes acp` (not `hermes-acp`)

## Remaining Risks

1. OpenCode ACPX NDJSON warnings can confuse automation that assumes clean JSON-only transport.
2. Historical docs still exist in the repo and may conflict if consumed without runtime validation.
3. Machine-level config may change outside this repo; docs require periodic re-verification.
