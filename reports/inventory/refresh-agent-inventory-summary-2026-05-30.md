# Refresh Agent Inventory Summary (2026-05-30)

## Scope

- Read and scanned all files under reports/ (29 files).
- Mapped VS Code Copilot Chat global storage at:
  - c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat
- Consolidated inventory for:
  - Copilot CLI, VS Code Copilot Chat extension, OpenCode, Hermes, Qwen
  - skills, agents, hooks, plugins, prompts, instructions
  - MCP servers and ACPX targets

## Source Set Read

- reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- reports/cleanup-2026-05-30-manifest.md
- reports/manual-review-queue-2026-05-30.md
- reports/post-cleanup-summary-2026-05-30.md
- reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md
- reports/inventory/copilot-cli-vscode-copilot-chat-priority-categories-20260530.md
- reports/inventory/copilot-inventory-summary-2026-05-30.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_COMPLETION_CERTIFICATE.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_DELIVERABLES_MANIFEST.txt
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_FINAL_SUMMARY.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_IMPLEMENTATION_VERIFIED.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_INDEX.txt
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE3_CODE_REVIEW_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE4_EXECUTION_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE4_MIGRATION_LOG.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE4_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE5_EXECUTION_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE5_REAL_EXECUTION_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE5_TESTING_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE6_CLEANUP_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE6_EXECUTION_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASE6_REAL_CLEANUP_REPORT.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PHASES_3_6_READINESS.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_FIX_PROJECT_SUMMARY.md
- reports/migrations/bash-scripts-fix/BASH_SCRIPTS_MIGRATION_COMPLETION_CERT.md
- reports/migrations/skills-fix/SKILLS_FIX_COMPLETION_CERT.md
- reports/migrations/skills-fix/SKILLS_FIX_INDEX.txt
- reports/migrations/skills-fix/SKILLS_FIX_PHASE_1_3_REPORT.md
- reports/migrations/skills-fix/SKILLS_FIX_PHASE_3_EXECUTION_REPORT.md

## VS Code Copilot Chat Extension Map

Top-level map for
c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat:

- ask-agent/
  - Ask.agent.md
- explore-agent/
  - Explore.agent.md
- plan-agent/
  - Plan.agent.md
- copilotCli/
  - copilot
  - copilot.bat
  - copilot.ps1
- debugCommand/
  - copilot-debug.bat
  - copilot-debug.ps1
  - copilotDebugCommand.js
- copilot-cli-images/ (empty)
- commandEmbeddings.json
- settingEmbeddings.json
- toolEmbeddingsCache.bin

## Inventory Snapshot

### Canonical report snapshot (historical baseline)

From reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md:

- Instructions: 34
- Agents: 475
- Prompts: 340
- Skills: 346
- Hooks: 2
- Plugins: 21

### Live workspace scan snapshot (refresh run)

From current workspace glob scans during this run:

- Instructions: 34
- Agents: 159
- Prompts: 185
- Skills: 289
- Hooks: 2
- Plugins: 21

## Requested Category Listing

### Copilot CLI

- Report source:
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md
- Global storage wrappers:
  - c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/copilotCli/copilot
  - c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/copilotCli/copilot.bat
  - c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/copilotCli/copilot.ps1
- Repo identity references:
  - .github/prompts/plan-acpx-agent-stack-audit-copilot.prompt.md
  - AGENTS.md (ACPX Coding Agent Integration table)

### VS Code Copilot Chat Extension

- Report source:
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md
- Extension storage map:
  - c:/Users/Alexa/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/\*
- Published extension skill counts in report:
  - VS Code Copilot Chat Extension Skills: 142
  - VS Code Copilot Built-in Skills: 13

### OpenCode

- Hooks:
  - .opencode/hooks/hooks.json
  - .opencode/hooks/hooks-cursor.json
- Plugins (21):
  - .opencode/plugins/\*.yaml (full list in
    reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md)
- References in reports:
  - reports/inventory/copilot-inventory-summary-2026-05-30.md
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

### Hermes

- Root agent:
  - .github/agents/hermes.agent.md
- Hermes-related prompts:
  - .github/prompts/hermes-breakdown-\*.prompt.md
- Migration report family:
  - reports/migrations/skills-fix/\*
  - reports/manual-review-queue-2026-05-30.md (Hermes completion report family)

### Qwen

- Root agent:
  - .github/agents/qwen-code.agent.md
- ACPX target references:
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md
  - AGENTS.md (ACPX Coding Agent Integration table)

### Skills

- Canonical report baseline count: 346
- Live scan count: 289
- Authoritative list references:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

### Agents

- Canonical report baseline count: 475
- Live scan count: 159
- Authoritative list references:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

### Hooks

- Count: 2
- Files:
  - .opencode/hooks/hooks.json
  - .opencode/hooks/hooks-cursor.json

### Plugins

- Count: 21
- Directory:
  - .opencode/plugins/
- Full plugin list reference:
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

### Prompts

- Canonical report baseline count: 340
- Live scan count: 185
- Authoritative list references:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
  - reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

### Instructions

- Count: 34 (baseline and live scan agree)
- Authoritative list references:
  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md

### MCP Servers

From
reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md:

- repo:.opencode/opencode.json
  - MCP_DOCKER (type=local, enabled=true)
  - filesystem (type=local, enabled=true)
  - playwright (type=local, enabled=true)
  - sequential-thinking (type=local, enabled=true)
- machine:~/.qwen/mcp-servers.json (missing)
- machine:~/.acpx/config.json agents (ACPX targets, not MCP servers)
  - copilot => copilot --acp --stdio
  - hermes => hermes acp
  - opencode => opencode acp
  - qwen => qwen --acp

## Refresh-Agent-Inventory Findings

1. Counts in AGENTS.md and .github/copilot-instructions.md still match the
   historical canonical snapshot, but they drift from the current workspace scan
   for agents/prompts/skills.
2. .github/copilot-instructions.md currently does not include .github/skills/ in
   its skill reuse guidance.
3. Canonical report path should remain preserved; a refreshed operational
   snapshot should be linked as the latest run output.

## Recommended Refresh Actions

1. Update AGENTS.md inventory snapshot counts to current run values and point to
   this report as the latest refresh snapshot.
2. Update .github/copilot-instructions.md inventory snapshot counts to current
   run values and add .github/skills/ to skill reuse guidance.
3. Keep
   reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md as
   canonical historical anchor, and reference this refresh report as the latest
   operational refresh.
