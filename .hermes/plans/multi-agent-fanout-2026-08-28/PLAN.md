---
title: Multi-Agent / Multi-Provider Fanout — Plan
generated: 2026-08-28
profile: adminbot
model: minimax/minimax-m3:free
status: ready → executing
---

# PLAN — Multi-Agent / Multi-Provider Fanout

## Sequencing (strict; "only then" is a hard constraint)

```
[1] Write SPEC.md, PLAN.md, implementation-plan.md
    ↓ only then
[2] Create scripts/auth_inventory.py (parse `hermes auth list`)
    ↓ only then
[3] Create scripts/package_inspector.py (read packages/**/*)
    ↓ only then
[4] Create scripts/fanout/ provider adapters (openrouter + openai_compat)
    ↓ only then
[5] Create scripts/fanout/ agent adapters (hermes, codex, opencode, copilot)
    ↓ only then
[6] Create scripts/fanout.py (orchestrator)
    ↓ only then
[7] Run V1 (auth_inventory), V2 (package_inspector) — verify JSON valid
    ↓ only then
[8] Run V3 (fanout --smoke) — verify at least 1 live cell returns ok
    ↓ only then
[9] Create skill multi-agent-fanout (SKILL.md + 3 refs + scripts + templates)
    ↓ only then
[10] Create prompt .github/prompts/multi-agent-fanout.prompt.md
    ↓ only then
[11] Full verification sweep
    ↓ only then
[12] Update SESSION_REPORT.md
```

## Task Breakdown

### T1 — Plans (done in this turn)

- `.hermes/plans/multi-agent-fanout-2026-08-28/SPEC.md` — design
- `.hermes/plans/multi-agent-fanout-2026-08-28/PLAN.md` — sequencing (this file)
- `.hermes/plans/multi-agent-fanout-2026-08-28/implementation-plan.md` — step-by-step

### T2 — auth_inventory.py

Parse `hermes auth list` text output, extract per-provider info.

**Inputs:** `hermes auth list` text
**Output:** `scripts/.runtime/provider_inventory.json`
**Schema:**
```json
{
  "generated": "...",
  "providers": [
    {
      "name": "openrouter",
      "credential_count": 1,
      "primary": {"env_var": "OPENROUTER_API_KEY", "auth_type": "api_key", "label": "OPENROUTER_API_KEY"},
      "credentials": [{"label": "OPENROUTER_API_KEY", "auth_type": "api_key", "source": "env", "is_active": true}],
      "capabilities_static": {
        "vision": false,
        "tools": true,
        "json_mode": true,
        "streaming": true,
        "system_prompt": true,
        "context_window_default": 32768
      }
    }
  ]
}
```

**Verify:** `python -c "import json; json.load(open('scripts/.runtime/provider_inventory.json'))"` exits 0; len(providers) == 11

### T3 — package_inspector.py

Walk `packages/*/`, parse `package.json` (TS) or `pyproject.toml` (Python), emit per-package summary.

**Inputs:** `packages/**/*`
**Output:** `scripts/.runtime/packages.json`
**Schema:**
```json
{
  "generated": "...",
  "packages": [
    {
      "name": "openrouter-client",
      "type": "typescript",
      "version": "1.0.0",
      "runtime": "bun@1.3.14",
      "entrypoints": ["src/client.ts", "src/chat.ts"],
      "exports": ["OpenRouterClient", "sendChat", "Message", "ChatCompletion"],
      "dependencies": ["@openrouter/sdk"],
      "dev_dependencies": ["@types/bun", "typescript"],
      "tests": ["test/chat.test.ts"],
      "spec": "SPEC.md",
      "plan": "PLAN.md"
    },
    {"name": "openrouter-client-py", "type": "python", "...": "..."}
  ]
}
```

**Verify:** `python -c "import json; json.load(open('scripts/.runtime/packages.json'))"` exits 0; len(packages) == 2

### T4 — Provider adapters

Two files in `scripts/fanout/providers/`:

- `openrouter.py` — uses in-tree `packages/openrouter-client-py` (subprocess `uv run`)
- `openai_compat.py` — generic OpenAI-compatible `/chat/completions` caller (deepseek, gemini, xai, nous, ollama-cloud, huggingface)

Both expose a uniform interface:
```python
async def call(prompt: str, model: str, api_key: str, base_url: str, **kwargs) -> dict:
    """Returns {output_text, output_tokens, latency_ms, error?, raw?}"""
```

### T5 — Agent adapters

Four files in `scripts/fanout/agents/`:

- `hermes.py` — `subprocess.run(['hermes', '-m', model, '-p', prompt, '--cli', '--no-tui'])`
- `codex.py` — `subprocess.run(['codex', 'exec', prompt, '--model', model])`
- `opencode.py` — `subprocess.run(['opencode', 'run', prompt, '-m', model])`
- `copilot.py` — `subprocess.run(['copilot', '-p', prompt, '--model', model])`

All return `{output_text, latency_ms, exit_code, error?}`.

### T6 — fanout.py orchestrator

```python
# scripts/fanout.py
import argparse, asyncio, json
from pathlib import Path

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run only 1-2 cells")
    parser.add_argument("--prompt", default="Reply with the word OK and your model name")
    parser.add_argument("--output", default=".hermes/plans/multi-agent-fanout-<date>/fanout-report.json")
    args = parser.parse_args()

    inv = json.load(open("scripts/.runtime/provider_inventory.json"))
    cells = build_cells(inv, smoke=args.smoke)
    results = await asyncio.gather(*[run_cell(c, args.prompt) for c in cells])
    write_report(args.output, results)

asyncio.run(main())
```

### T7 — Skill

```
~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/
├── SKILL.md                       (≤250 lines, workflow + verification checklist)
├── references/
│   ├── output-schema.md           (the JSON shape, examples)
│   ├── provider-matrix.md         (the 11×4 matrix, per-cell notes)
│   └── agent-adapters.md          (per-agent CLI flag cheatsheet)
├── scripts/
│   ├── auth_inventory.py          (copy from scripts/)
│   ├── package_inspector.py       (copy)
│   ├── fanout.py                  (copy)
│   └── fanout/                    (copy providers/ + agents/)
└── templates/
    ├── fanout-config.json         (per-task default model overrides)
    └── capability-table.json      (extend with new providers)
```

### T8 — Prompt

`.github/prompts/multi-agent-fanout.prompt.md` — single-shot agent prompt.

### T9 — Verification

```
python scripts/auth_inventory.py           # V1
python scripts/package_inspector.py        # V2
python scripts/fanout.py --smoke           # V3 (real live call)
hermes skills list | grep multi-agent      # V5
ls .github/prompts/multi-agent-fanout.prompt.md  # V6
```

### T10 — SESSION_REPORT.md

Append this session as a new section.

## Stop Conditions

- **Continue until** all V1-V8 pass
- **Stop & ask** if a provider 401s the live call AND the static fallback can't fill capabilities
- **Stop & document** if a CLI tool is missing
