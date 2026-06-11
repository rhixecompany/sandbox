## Goal
Use when ## Description to accomplish the associated tasks and objectives.
## Description

Copilot executor variant. Run command-first audit and reconciliation for Hermes,
Copilot CLI and ACPX.

## Context

- Primary executor: Copilot CLI.
- Shell: PowerShell-first commands, runnable from bash.
- Objective: produce one verified support matrix.

### Machine-Local File Checklist

- [ ] `C:/Users/Alexa/AppData/Local/hermes/config.yaml`
- [ ] `C:/Users/Alexa/AppData/Local/hermes/.env`
- [ ] `C:/Users/Alexa/.acpx/config.json`

### Repo Control Points

- `c:/Users/Alexa/Desktop/SandBox/.opencode/hooks/hooks.json`
- `c:/Users/Alexa/Desktop/SandBox/.opencode/rules/acpx-integration.md`
- `c:/Users/Alexa/Desktop/SandBox/.opencode/skills/autonomous-ai-agents/acpx-agent-routing/SKILL.md`
- `c:/Users/Alexa/Desktop/SandBox/.github/agents/hermes.agent.md`
- `c:/Users/Alexa/Desktop/SandBox/.github/agents/qwen-code.agent.md`
- `c:/Users/Alexa/Desktop/SandBox/AGENTS.md`
- `c:/Users/Alexa/Desktop/SandBox/docs/agents-cross-reference.md`

## Skills Required

- CLI execution.
- Output triage.
- Routing contradiction analysis.
- Config and docs reconciliation.

## Subagents

- `debugger`.
- `technical-writer`.

## Personas

- Executor operator.
- Compatibility auditor.

## Rules

- Prefer runtime evidence over docs.
- Label each route: `working`, `broken`, `unverified`.
- Fix config before docs.
- Keep secrets redacted.

## Phases

### Phase 1: Runtime and Liveness

| Field | Details |
| --- | --- |
| Goal | Prove tool versions, auth state, and liveness. |
| Inputs | CLI tools and machine-local config. |
| Outputs | Version/liveness evidence. |
| Validation | All commands return output or explicit errors. |

**Commands**

```powershell
Set-Location 'C:/Users/Alexa/Desktop/SandBox'
copilot --version
copilot -p 'Reply with exactly: COPILOT_ALIVE' --allow-all -s
opencode --version
opencode auth list
acpx opencode exec 'Reply with exactly: OPENCODE_ALIVE'
qwen --version
acpx qwen exec 'Reply with exactly: QWEN_ALIVE'
hermes --version
acpx --version
```

### Phase 2: Routing and Drift Scan

| Field | Details |
| --- | --- |
| Goal | Resolve provider naming and route contradictions. |
| Inputs | Repo docs and scan output. |
| Outputs | Final routing decisions. |
| Validation | Contradictions have explicit decisions. |

**Commands**

```powershell
Set-Location 'C:/Users/Alexa/Desktop/SandBox'
rg -n 'opencode-acp|copilot-acp|qwen-code|qwen-acp|hermes-acp|hermes acp' .
rg -n 'not a valid Hermes ACP provider|acp://opencode|acp://copilot|acp://qwen' .opencode docs AGENTS.md
rg -n 'acpx-agent-routing' .opencode docs Prompts
rg -n '"plugin"|hooks|opencode-handoff|rate-limit|quota|cost-guard' .opencode
```

### Phase 3: Repo Validation

| Field | Details |
| --- | --- |
| Goal | Run repository format, type, and lint gates. |
| Inputs | `Bash/` toolchain scripts. |
| Outputs | Validation pass/fail evidence. |
| Validation | Commands complete with exit status captured. |

**Commands**

```powershell
Set-Location 'C:/Users/Alexa/Desktop/SandBox/Bash'
bun run format
bun run typecheck
bun run lint:strict
```

## Steps

1. Run liveness commands.
2. Run routing scans.
3. Run repo gates.
4. Publish output contract.

## Tasks

- Task 1.1 — Collect runtime and liveness evidence.
- Task 2.1 — Reconcile routing contradictions.
- Task 3.1 — Run repo validation commands.
- Task 4.1 — Publish final matrix and risks.

## Subtasks

- Subtask 1.1.1 — Capture versions and auth listings.
- Subtask 1.1.2 — Execute Copilot/OpenCode/Qwen liveness calls.
- Subtask 2.1.1 — Scan for provider name drift.
- Subtask 2.1.2 — Decide `opencode-acp` route status for Hermes.
- Subtask 3.1.1 — Run format/typecheck/lint strict.
- Subtask 4.1.1 — Emit contract sections in order.

## Actions Summary

1. `Support Matrix`.
2. `Routing Decisions`.
3. `Changes Made`.
4. `Open Risks`.
5. `Validation Run`.
