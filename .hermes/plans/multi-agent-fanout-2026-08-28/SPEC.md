---
title: Multi-Agent / Multi-Provider Fanout — Specification
plan: .hermes/plans/multi-agent-fanout-2026-08-28/PLAN.md
generated: 2026-08-28
profile: adminbot
model: minimax/minimax-m3:free
status: ready
---

# SPEC — Multi-Agent / Multi-Provider Fanout

## 1. Problem Statement

The SandBox has 11 authorized LLM providers (`hermes auth list`) and 6 installed AI agents
(hermes, codex, opencode, copilot + npm-bundled omo, claude), plus 2 in-tree SDK packages
(`packages/openrouter-client` TS, `packages/openrouter-client-py` Python). There is no single
place that:

- Enumerates authorized providers with their capabilities
- Reads & documents the two SDK packages
- Runs a user prompt non-interactively across all (provider × agent) combinations
- Returns a structured result with `provider`, `model`, `context`, `max_output`, `capabilities`,
  `status`, `latency_ms`, `output_text`, `output_tokens`, `error`

## 2. Goals

| # | Goal | Priority |
|---|------|----------|
| G1 | One Python script that parses `hermes auth list` into a structured `provider_inventory.json` | MUST |
| G2 | One Python script that runs a prompt non-interactively against each (provider, agent) cell, captures structured results | MUST |
| G3 | One Python script that reads `packages/**/*` and emits a per-package documentation summary | MUST |
| G4 | Output schema includes provider, model, context, max_output, capabilities, status, latency, output, error | MUST |
| G5 | Reuse the two in-tree packages where possible (don't reimplement OpenRouter wrapper) | SHOULD |
| G6 | One umbrella skill `multi-agent-fanout` with SKILL.md, references, scripts, templates | MUST |
| G7 | One prompt `.github/prompts/multi-agent-fanout.prompt.md` for human invocation | MUST |
| G8 | Real fanout smoke test actually executes against live providers (no stubs, no fabricated data) | MUST |
| G9 | Document the output schema and provider capabilities as a Markdown report | SHOULD |

## 3. Non-Goals

- Build a full MOA (Mixture-of-Agents) ranking/arbitration layer (hermes already has `hermes moa`)
- Add new providers (out of scope; `hermes mcp catalog` and `hermes auth add` are the right tools)
- Replace either of the two in-tree SDK packages
- Add any package that needs an API key we don't already have

## 4. Design

### 4.1 Output Schema (the user's explicit ask)

```json
{
  "generated": "2026-08-28T17:55:00Z",
  "prompt": "Reply with the word OK and your model name",
  "results": [
    {
      "provider": "openrouter",
      "model": "minimax/minimax-m3:free",
      "agent": "openrouter-client",
      "context_window": 32768,
      "max_output_tokens": 4096,
      "capabilities": {
        "vision": false,
        "tools": true,
        "json_mode": true,
        "streaming": true,
        "system_prompt": true,
        "temperature": true,
        "top_p": true
      },
      "status": "ok" | "fail" | "skip" | "auth_failed",
      "latency_ms": 1234,
      "output_text": "...",
      "output_tokens": 12,
      "error": null | "..."
    }
  ]
}
```

### 4.2 Provider Inventory Source

Run `hermes auth list` once, parse text output, write `provider_inventory.json` containing
one entry per provider with: provider name, credential count, primary credential source
(env var or manual), and per-provider static-known capability defaults.

### 4.3 Provider × Agent Matrix

| Provider  | SDK / Agent                                  | Adapter |
|-----------|----------------------------------------------|---------|
| openrouter| packages/openrouter-client-py (async)        | scripts/fanout/providers/openrouter.py |
| openrouter| packages/openrouter-client (TS via bun)      | scripts/fanout/providers/openrouter_ts.py |
| deepseek  | OpenAI-compatible HTTP                       | scripts/fanout/providers/openai_compat.py (deepseek base URL) |
| gemini    | OpenAI-compatible HTTP (gemini base URL)     | scripts/fanout/providers/openai_compat.py |
| xai       | OpenAI-compatible HTTP                       | scripts/fanout/providers/openai_compat.py |
| opencode-zen| OpenAI-compatible HTTP                     | scripts/fanout/providers/openai_compat.py |
| nous      | OpenAI-compatible HTTP (inference-api.nousresearch.com) | scripts/fanout/providers/openai_compat.py |
| ollama-cloud| OpenAI-compatible HTTP                     | scripts/fanout/providers/openai_compat.py |
| huggingface| OpenAI-compatible HTTP                      | scripts/fanout/providers/openai_compat.py |
| copilot   | GitHub Copilot CLI (`copilot -p`)            | scripts/fanout/agents/copilot.py |
| openai-codex| OpenAI Codex CLI (`codex exec`)            | scripts/fanout/agents/codex.py |
| opencode  | opencode CLI (`opencode run`)                | scripts/fanout/agents/opencode.py |
| hermes    | hermes CLI (`hermes -z`)                     | scripts/fanout/agents/hermes.py |

Where providers overlap, the matrix generates multiple cells: e.g. `openrouter` × `openrouter-client-py`,
`openrouter` × `openrouter-client (TS)`, `openrouter` × `codex`, `openrouter` × `hermes`, etc.

### 4.4 Capability Source

| Source | When |
|--------|------|
| OpenRouter `/models` endpoint (live) | Always — gives context, modalities, pricing |
| Static provider-specific table | Fallback when API key missing or live call fails |
| Hermes profile config | For hermes-cell context (e.g. `nvidia/nemotron-3-ultra-550b-a55b:free` had 32k context) |

## 5. Verification Gates

| Gate | Pass condition |
|------|---------------|
| V1 | `python scripts/auth_inventory.py` writes valid JSON, 11 providers, 0 errors |
| V2 | `python scripts/package_inspector.py` writes valid JSON for both packages |
| V3 | `python scripts/fanout.py --smoke` exits 0 with at least 1 cell `status=ok` (real live result) |
| V4 | Output JSON has the schema fields: provider, model, agent, context_window, max_output_tokens, capabilities, status, latency_ms, output_text, output_tokens, error |
| V5 | Skill `multi-agent-fanout` is created and discoverable via `hermes skills list` |
| V6 | Prompt `.github/prompts/multi-agent-fanout.prompt.md` is created |
| V7 | All my created/modified files pass `bun run lint` (no syntax errors) |
| V8 | SESSION_REPORT.md updated |

## 6. Risks

| Risk | Mitigation |
|------|-----------|
| Some providers have no compatible SDK installed | Use raw `urllib.request` for OpenAI-compat providers; no new deps |
| Live calls to all 11 providers in one run is slow | `--smoke` mode runs only 1-2 cells; full fanout is opt-in |
| 401/403/429 rate limits on a provider | Mark `status: "auth_failed"` or `status: "fail"`; do not abort run |
| `hermes auth list` output format changes | Pin parser to current v0.20.6 format; document |
| Output tokens field missing in non-OpenAI providers | Fallback to `null` for `output_tokens`; never fabricate |

## 7. Files

| Path | Purpose |
|------|---------|
| `.hermes/plans/multi-agent-fanout-2026-08-28/SPEC.md` | This file |
| `.hermes/plans/multi-agent-fanout-2026-08-28/PLAN.md` | Sequencing + task breakdown |
| `.hermes/plans/multi-agent-fanout-2026-08-28/implementation-plan.md` | Step-by-step |
| `scripts/auth_inventory.py` | Provider inventory from `hermes auth list` |
| `scripts/package_inspector.py` | Reads packages/**/* → package docs |
| `scripts/fanout.py` | Run prompt non-interactively across cells |
| `scripts/fanout/providers/openrouter.py` | OpenRouter adapter (uses existing openrouter-client-py) |
| `scripts/fanout/providers/openai_compat.py` | OpenAI-compat adapter (deepseek/gemini/xai/nous/ollama/hf) |
| `scripts/fanout/agents/hermes.py` | hermes CLI subprocess |
| `scripts/fanout/agents/codex.py` | codex CLI subprocess |
| `scripts/fanout/agents/opencode.py` | opencode CLI subprocess |
| `scripts/fanout/agents/copilot.py` | copilot CLI subprocess |
| `~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/SKILL.md` | Umbrella skill |
| `~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/references/*` | 3 ref files |
| `~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/scripts/*` | Copies of inventory + fanout |
| `~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/templates/*` | Skeletons |
| `.github/prompts/multi-agent-fanout.prompt.md` | Human-invocation prompt |
