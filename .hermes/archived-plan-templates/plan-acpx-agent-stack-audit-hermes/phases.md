# Phases

> Extracted from `plan-acpx-agent-stack-audit-hermes.prompt.md`.

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
hermes doctor
hermes --version
opencode --version
opencode auth list
copilot --version
qwen --version
acpx --version
acpx qwen exec 'Reply with exactly: QWEN_ALIVE'
acpx opencode exec 'Reply with exactly: OPENCODE_ALIVE'
copilot -p 'Reply with exactly: COPILOT_ALIVE' --allow-all -s
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
