---
user: Alexa
---

# USER.md — Alexa

**Identity:** Win 11 | Git Bash | VS Code | Workspace ~/Desktop/SandBox

**Active Model:** stepfun/step-3.7-flash:free (nous)
**Chain:** opencode-zen → nous → openrouter

## Execution Preferences
Read→patch→verify. Strict sequential on "only then". MCP-first. No backup files — git. DRY: single source per fact. Paths from $HOME/$USERPROFILE.

**Tools:** Python 3.13/3.11 | uv | Bun 1.3.14+

**Security:** MCP least-privilege + OAuth 2.1+PKCE + SSRF blocks. No secrets in output. Never commit .env.

**Memory:** MCP knowledge graph for structured facts; native `memory` tool (batch ops) for compact entries.

See SOUL.md for quality/commits/response style. See SOUL.md profile routing table.

See ~/AppData/Local/hermes/USER.md for full profile. Compact: Alexa | Windows 11 | bash (git-bash/MSYS) | default | qwen/qwen3-coder:free (OpenRouter) | read-first verify-first | no inline scripts | MCP-first tooling
# USER.md — Alexa (default)

## Identity
- **Name:** Alexa | **OS:** Windows 11 | **Shell:** Git Bash/MSYS
- **Editor:** VS Code | **Hermes:** ~/AppData/Local/hermes | **Workspace:** ~/Desktop/SandBox

## Active Model & Providers
- **Model:** deepseek-v4-flash-free (opencode-zen) | **Active Profile:** alexa
- **Chain:** opencode-zen → nous (stepfun/step-3.7-flash:free) → openrouter (qwen/qwen3-coder:free)
- **7 configured:** alexa, default, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst
- **17 unconfigured:** arch, architect, debugger, devops-expert, github-actions-expert, hermes, implementation-plan, mentor, planner, power-bi, prd, prompt-engineer, qa-subagent, reviewer, specification, tanstack, terraform

## Execution Preferences
- Read first, patch edits; verify before claim | Concise, action-first
- No backup files (use git) | Explain risks before destructive ops
- Strict sequential on "only then" | No inline scripts
- Session startup: load 5 skills, use MCP first, profile per task

## Environment
- **Python:** 3.13.14 / 3.11.15 | **uv:** installed | **Bun:** 1.3.14+
- **14 MCP servers** | **15 plugins** | **3 hooks** | **373 skills**

## Standards
- See ~/AppData/Local/hermes/USER.md + SOUL.md + MASTER_RULES.md + PROJECT_RULES.md
Profile maintenance authorized: resync all Hermes profile files (default + non-default) when updating identity/model/provider. Use cross_profile=True for profile memory edits.
Profile sync rules for USER.md/SOUL.md: root files are system behavior + active session identity; non-default profiles keep only role-specific personality/rules. Compact profile memory files must remain smaller than root USER.md.
Canonical model query order: current session/context > skill docs > config.yaml. Do not edit ~/.hermes/config.yaml directly; use hermes config set. hermes/config.yaml is authoritative for provider chain.
Alexa persona/preferences distilled: concise, action-first, DRY, strict sequential gating with “only then”, explicit completion criteria before advancing, prefers best-practice depth with full operational detail. Windows host, Git Bash, workspace C:\Users\Alexa\Desktop\SandBox, sole git repo. Canonical model stepfun/step-3.7-flash:free (nous). Active session provider chain opencode-zen -> nous -> openrouter. Approves destructive/normalization ops per full pass + commit/push. Strongly prefers durable fixes verified before claiming done.
Alexa: name, OS Windows 11, shell Git Bash (MSYS), editor VS Code. Hermes profile default; workspace SandBox. Model stepfun/step-3.7-flash:free (nous). Values: DRY, strict sequential, plan normalization, memory validation, full-pass audits. Context drift detected earlier: root SOUL.md had stale stepfun label; now canonical. Non-default profiles cross-reference root identity.
User prefers systematic debugging workflow: Phase 1 (root cause) before any fixes. They value clean SESSION_REPORT.md updates alongside code fixes in commits. They want full git add/commit/push with push to all subrepos.
User prefers skill-library updates after sessions when a reusable technique, correction, or workflow lesson emerges, and prefers class-level umbrella skills with session-specific detail kept in references/ files.