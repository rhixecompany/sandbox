# Agent / Provider Matrix Runner

## Overview

Runs a single user request across every installed Hermes profile and every authorized provider, feeding each cell a prompt that includes package-derived capability context. Designed for noninteractive execution from a terminal or CI.

## When to Use

- Cross-provider comparison of agent behavior
- Generating a capability + output matrix for `packages/**/*`
- Smoke testing provider/profile wiring without interactivity

## Prerequisites

- `hermes auth list` and `hermes profile list` are configured
- The workspace has a `packages/` tree with at least one manifest
- A renderable prompt template at `prompts/agent-provider-matrix.prompt.md`

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/agent_provider_matrix.py` | The runner: parses inventory, scans packages, renders the prompt, executes cells |
| `scripts/agent-provider-matrix-smokecheck.sh` | One-cell live validation |

## Usage

```bash
# Dry run (plan only, no live provider calls)
python scripts/agent_provider_matrix.py --dry-run --limit-cells 2 --quiet

# Live run for a single profile/provider pair
python scripts/agent_provider_matrix.py --profile default --provider openai-codex --max-turns 2 --run-budget 120

# Full matrix (be budget-aware: profiles x providers = many cells)
python scripts/agent_provider_matrix.py --limit-cells 5
```

### Flags

| Flag | Default | Notes |
|------|---------|-------|
| `--request` | built-in default | Free-text request rendered into the prompt template |
| `--request-file` | — | Read request from a file |
| `--prompt-template` | `prompts/agent-provider-matrix.prompt.md` | `{{ }}` placeholders: `REQUEST`, `PROFILE`, `PROVIDER`, `MAX_OUTPUT`, `PACKAGE_CONTEXT`, `PACKAGE_CAPABILITIES`, `MODEL_HINT` |
| `--packages-root` | `packages/` | Root containing package manifests |
| `--results-root` | `.hermes/plans/results/agent-provider-matrix` | Output directory (timestamped sub-run) |
| `--provider` | all | Repeatable or CSV |
| `--profile` | all | Repeatable or CSV |
| `--max-output` | 1200 | Response excerpt budget (chars) |
| `--max-turns` | 20 | Per-cell Hermes max-turns |
| `--run-budget` | 300 | Per-cell Hermes run-budget (seconds) |
| `--model` | profile default | Override model for every cell |
| `--limit-cells` | all | Cap the number of cells (smoke-test helper) |
| `--dry-run` | off | Render commands/context only; do not call `hermes chat` |
| `--quiet` | verbose | Compact progress output |

## Output Artifacts

Each run writes a timestamped directory under `.hermes/plans/results/agent-provider-matrix/<UTC>/`:

```
inventory.json                       # profiles, providers, packages (snapshot at run time)
summary.md                           # human-readable matrix table
summary.json                         # machine-readable roll-up
<profile>/<provider>/
  request.md                         # rendered prompt per cell
  stdout.txt                         # raw Hermes stdout
  stderr.txt                         # raw Hermes stderr
  result.json                        # normalized result + excerpt
```

## Result Schema (per cell)

```jsonc
{
  "profile": "default",
  "provider": "openai-codex",
  "package_context": "…",
  "max_output": 1200,
  "capabilities": ["chat completions", "streaming"],
  "model": "gpt-5.4-mini",
  "command": ["hermes", "-p", "default", "chat", …],
  "exit_code": 0,
  "duration_ms": 3421,
  "status": "ok",
  "response_excerpt": "…",
  "result_path": ".hermes/…/result.json",
  "assumptions": ["…"]
}
```

## Verification Checklist

- [ ] `python scripts/agent_provider_matrix.py --dry-run --limit-cells 1 --quiet` exits 0
- [ ] `inventory.json` lists all providers and profiles from live `hermes` output
- [ ] Package capability summaries are produced for every package under `packages/`
- [ ] `--prompt-template` renders without leftover `{{ }}` placeholders
- [ ] One live cell completes and `result.json` contains the normalized fields
- [ ] No secrets appear in any printed or saved output

## References

- `provider-model-audit` / `test-providers-models` — provider inventory concepts
- `prompts/agent-provider-matrix.prompt.md` — prompt template
- `packages/openrouter-client/` and `packages/openrouter-client-py/` — package context source
