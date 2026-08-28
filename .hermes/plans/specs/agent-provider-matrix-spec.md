# Agent / Provider Matrix Runner Specification

**Date:** 2026-08-28  
**Status:** draft  
**Scope:** Cross-provider, noninteractive execution across installed Hermes profiles and authorized providers, with package-derived capability context.

---

## Problem Statement

The current workspace has two OpenRouter wrapper packages under `packages/**/*` and a live Hermes installation with multiple profiles plus several authorized providers discovered via `hermes auth list`. We need a repeatable, noninteractive runner that can:

1. discover installed Hermes profiles,
2. discover authorized providers,
3. read and understand the package tree under `packages/**/*`,
4. run the same user request across every profile/provider pair,
5. return normalized results that include provider, context, max-output, and capabilities.

The workflow must be scriptable, deterministic, and safe to run from CI or a terminal session without prompts.

---

## Current Inventory

### Authorized providers from `hermes auth list`

Observed providers in the current environment:

- copilot
- deepseek
- gemini
- huggingface
- ollama-cloud
- openai-codex
- opencode-zen
- openrouter
- xai
- xai-oauth

### Installed Hermes profiles from `hermes profile list`

Observed profiles in the current environment:

- default
- alexa
- code-architect
- creative-director
- cto
- designer
- dev
- exec-assistant
- ops
- patient-tutor
- pm
- qa
- research-analyst
- security

### Package inventory under `packages/**/*`

Only two packages exist under `packages/`:

1. `packages/openrouter-client`
   - TypeScript
   - Bun package manager
   - Wrapper over `@openrouter/sdk`
   - Exposes `OpenRouterClient` and `sendChat`
   - Supports custom headers, streaming, `max_tokens`, and `temperature`

2. `packages/openrouter-client-py`
   - Python
   - `pyproject.toml` + setuptools
   - Wrapper over `openrouter`
   - Exposes `OpenRouterClient` and `send_chat`
   - Supports custom headers, streaming, `max_tokens`, and `temperature`

---

## Requirements

### Functional Requirements

- FR-1: Discover providers from `hermes auth list` at runtime; do not hard-code provider names.
- FR-2: Discover installed Hermes profiles from `hermes profile list` at runtime.
- FR-3: Read `packages/**/*` and derive a concise capability summary for each package.
- FR-4: Run a noninteractive request against every profile/provider pair by default.
- FR-5: Support filtering by profile and provider so the matrix can be reduced for debugging.
- FR-6: Use a prompt file/template so the same user request can be replayed consistently.
- FR-7: Capture normalized result fields: provider, profile, package context, max-output, capabilities, model used, status, exit code, and response excerpt.
- FR-8: Write machine-readable output plus a human-readable report.
- FR-9: Expose a dry-run mode that prints the exact commands and context without making live requests.
- FR-10: Use Hermes-managed credentials only; do not require subprocess environment keys.

### Non-Functional Requirements

- NFR-1: No interactive prompts.
- NFR-2: No secrets in stdout or report files.
- NFR-3: Windows-safe paths and subprocess calls.
- NFR-4: Deterministic inventory parsing and stable output ordering.
- NFR-5: Script must be runnable from the repository root.

---

## Output Contract

Each matrix result must contain:

- `profile`
- `provider`
- `package_context`
- `max_output`
- `capabilities`
- `model`
- `command`
- `exit_code`
- `duration_ms`
- `status`
- `response_excerpt`
- `result_path`
- `assumptions` (only if needed)

### Report formats

1. Markdown summary for humans
2. JSON artifact for automation
3. Per-cell text or JSON result files for reruns and diffing

---

## Acceptance Criteria

- AC-1: `hermes auth list` and `hermes profile list` are parsed successfully.
- AC-2: Package scanning produces capability summaries for both packages.
- AC-3: The prompt file exists and can be used noninteractively.
- AC-4: The runner supports `--dry-run` and produces no live provider calls.
- AC-5: The runner can execute a live request for at least one profile/provider pair.
- AC-6: The output includes provider, context, max-output, and capabilities for each result.
- AC-7: The runner writes summary artifacts under `.hermes/plans/results/`.
- AC-8: The workflow does not depend on secrets in subprocess env vars.

---

## Implementation Approach

- Use one Python runner in `scripts/` to avoid split-brain logic.
- Parse Hermes CLI output directly for profile/provider inventory.
- Scan `packages/**/*` with `pathlib` and a small set of heuristics:
  - package manager / build tool
  - exported entrypoints
  - tested features in README / SPEC / source
- Feed a prompt template into `hermes chat --query-file` for each matrix cell.
- Default to provider-only selection; allow future per-provider model mapping if needed.
- Record the effective model returned by Hermes in each result row.

---

## Risks and Tradeoffs

- Provider defaults may differ by profile, so the effective model must be recorded from the live response.
- The matrix can grow large quickly: 14 profiles × 10 providers = 140 requests. Dry-run and filtering are required.
- Some providers may be authenticated but rate-limited or quota-limited.
- Package capability detection is heuristic. The runner should be honest about what it inferred versus what it executed.

---

## References

- `provider-model-audit` — provider inventory and benchmarking concepts
- `test-providers-models` — inventory + model discovery workflow
- `provider-reliability-diagnostics` — provider failure handling and routing context
- `packages/openrouter-client/*` — TypeScript OpenRouter wrapper
- `packages/openrouter-client-py/*` — Python OpenRouter wrapper
