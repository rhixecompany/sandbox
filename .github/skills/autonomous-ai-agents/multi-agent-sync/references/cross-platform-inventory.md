# Cross-Platform Agent Inventory Reference

> Captures the scale-aware inventory and grouping pattern from the 2026-06-21 multi-agent sync session.

## Situation

When syncing across 3 agent platforms with 170+ Copilot instructions and 174 Copilot agents, creating individual Hermes profiles/personalities for every item is impractical and counterproductive.

## Solution: Category Grouping + Priority Profiles

### Instructions → Personalities (Grouped)

Instead of creating 170 one-line personalities, group by tech stack:

| Group | Sample Instructions | Personality Entry |
|-------|-------------------|-------------------|
| Azure/DevOps | bicep, terraform, azure-functions, logic-apps | `azure-devops` |
| Web Frontend | reactjs, nextjs, astro, svelte, vuejs3, tailwind | `web-frontend` |
| Power Platform | power-bi-*, power-apps-*, dataverse-*, pcf-* | `power-platform` |
| .NET | csharp, blazor, maui, wpf, dotnet-* | `dotnet` |
| Database | postgresql, mongodb, ms-sql, cassandra | `database` |
| Security | owasp, secure-coding, secret-scanning, rbac | `security` |
| DevOps/SRE | docker, kubernetes, github-actions, ansible | `devops-sre` |
| Java/JVM | java, springboot, kotlin, scala, quarkus | `java-jvm` |
| Python/Data | python, langchain, dataverse-python, pandas | `python-data` |
| AI/AI-ML | mcp, semantic-kernel, copilot-sdk, llm | `ai-ml` |
| Mobile | maui, flutter, dart | `mobile` |
| Code Quality | code-review, testing, playwright, object-calisthenics | `code-quality` |

### Agents → Profiles (Priority-First)

Create full profile directories only for agents with high cross-platform value. Criteria:

1. **Generic utility** — agents useful across any codebase (arch, debugger, reviewer, planner)
2. **Workspace alignment** — agents matching existing workspace patterns (hermes, github-actions)
3. **Domain coverage** — top 1-2 agents per domain (terraform, power-bi, prd, mentor)

Priority list (17 profiles from ~174 agents):
- hermes, arch, architect, debugger, planner, reviewer, specification
- qa-subagent, implementation-plan, prd, mentor, prompt-engineer
- devops-expert, github-actions-expert
- power-bi-data-modeling-expert, terraform
- tanstack-start-shadcn-tailwind

### Minimum Profile Structure

```
profiles/<name>/
├── config.yaml     # Minimal: _config_version + agent section
└── SOUL.md          # References source .agent.md + role description
```

### Config template:
```yaml
_config_version: 30
agent:
  max_turns: 100
  disabled_toolsets: []
  personas:
    <name>: >-
      <description from agent file>
```

### SOUL.md template:
```markdown
# SOUL.md — <name> Profile

## Source
Created from `.github/agents/<name>.agent.md`.

## Role
<description>

## Inherits
Core rules from parent SOUL.md (response style, security, workspace conventions).
```

## Cross-Platform Feature Matrix

| Feature | Hermes | Copilot (.github/) | Codex (~/.codex/) |
|---------|--------|--------------------|-------------------|
| Skill format | SKILL.md (YAML+MD) | .instructions.md | skill.json/TOML |
| Agent/profile | profiles/<name>/ dir | .agent.md | agents/*.toml |
| Hooks | hooks/<name>/hook.sh | hooks/<name>/ (stubs) | — |
| Plugins | plugins/<name>/ | — | plugins/ (cache only) |
| Config | config.yaml | — | config.toml |

## Sync Compatibility

| Asset | Direct Copy? | Notes |
|-------|-------------|-------|
| Hook scripts | ✅ Yes | Both use bash/POSIX shell |
| Skills | ⚠️ Namespace copy | Different formats — copy to hermes-auto/ namespace dir |
| Plugins | ❌ No | Only Hermes has loadable plugins |
| Profiles | ⚠️ Template-based | Agent content translates via SOUL.md template |

## Verification Gates

When verifying across the 3 platforms, check these specific items:

1. **Hermes profiles directory** — count matches expected priority agents
2. **Personalities in config** — grouped categories present in `agent.personalities`
3. **.github/hooks/** — mirrors Hermes hooks' `hook.sh` scripts
4. **~/.codex/skills/hermes-auto/** — contains copied skill categories
5. **Cross-reference document** — lists asset counts per platform
