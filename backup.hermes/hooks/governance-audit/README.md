---
name: "Governance Audit"
description: "Scans Hermes agent prompts for threat signals and logs governance events"
tags: ["security", "governance", "audit", "safety", "hermes"]
---

# Governance Audit Hook

Real-time threat detection and audit logging for Hermes coding agent sessions. Scans user prompts for dangerous patterns before the agent processes them.

## Overview

This hook provides governance controls for Hermes agent sessions:

- **Threat detection**: Scans prompts for data exfiltration, privilege escalation, system destruction, prompt injection, and credential exposure
- **Governance levels**: `open`, `standard`, `strict`, `locked` — from audit-only to full blocking
- **Audit trail**: Append-only JSON Lines log of all governance events
- **Session summary**: Reports threat counts at session end

## Hook Events

| Event | Script | Log File |
|-------|--------|----------|
| `sessionStart` | `audit-session-start.sh` | `governance/audit.log` |
| `sessionEnd` | `audit-session-end.sh` | `governance/audit.log` |
| `userPromptSubmitted` | `audit-prompt.sh` | `governance/audit.log` |

## Threat Categories

| Category | Severity Range | Examples |
|----------|---------------|----------|
| `data_exfiltration` | 0.7 - 0.95 | Bulk data transfer, external export, credential upload |
| `privilege_escalation` | 0.8 - 0.95 | sudo, chmod 777, adding admin access |
| `system_destruction` | 0.9 - 0.95 | rm -rf /, drop database, mass deletion |
| `prompt_injection` | 0.6 - 0.9 | Instruction override, role reassignment |
| `credential_exposure` | 0.9 - 0.95 | Hardcoded API keys, AWS keys |

## Governance Levels

| Level | Behavior |
|-------|----------|
| `open` | Log threats only, never block |
| `standard` | Log threats, block only if `BLOCK_ON_THREAT=true` |
| `strict` | Log and block all detected threats |
| `locked` | Log and block all detected threats |

## Installation

1. Ensure scripts are executable:

   ```bash
   chmod +x C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/*.sh
   ```

2. Create the logs directory:

   ```bash
   mkdir -p C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance
   ```

3. Register the hook in `config.yaml` under `hooks:`.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `GOVERNANCE_LEVEL` | `standard` | Controls blocking behavior |
| `BLOCK_ON_THREAT` | `false` | Block prompts with threats (standard level) |
| `SKIP_GOVERNANCE_AUDIT` | unset | Disable governance audit entirely |

## Log Format

JSON Lines format — one compact JSON object per line:

```json
{"timestamp":"2026-01-15T10:30:00Z","event":"session_start","governance_level":"standard","cwd":"/workspace/project"}
{"timestamp":"2026-01-15T10:31:00Z","event":"prompt_scanned","governance_level":"standard","status":"clean"}
{"timestamp":"2026-01-15T10:32:00Z","event":"threat_detected","governance_level":"standard","threat_count":1,"max_severity":0.8,"threats":[{"category":"privilege_escalation","severity":0.8,"description":"Elevated privileges","evidence":"sudo"}]}
{"timestamp":"2026-01-15T10:45:00Z","event":"session_end","total_events":12,"threats_detected":1}
```

## Requirements

- `jq` for JSON processing (pre-installed on most systems)
- `grep` with `-E` (extended regex) support
- `awk` for float comparison (used instead of `bc` per hermes-hooks-manager rules)

## Privacy & Security

- Full prompts are **never** logged — only matched threat patterns (minimal evidence snippets) and metadata
- Add `logs/` to `.gitignore` to keep audit data local
- Set `SKIP_GOVERNANCE_AUDIT=true` to disable entirely
- All data stays local — no external network calls

## Source

Built-in Hermes hook.
