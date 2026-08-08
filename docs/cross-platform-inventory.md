# Cross-Platform Asset Inventory

Generated: 2026-08-05

## Summary

| Asset    | Hermes                                                    | Codex       | OpenCode      |
| -------- | --------------------------------------------------------- | ----------- | ------------- |
| Skills   | 621                                                       | 621         | 621           |
| Profiles | 13                                                        | 144 agents  | N/A           |
| Plugins  | 15 enabled                                                | 10 enabled  | N/A           |
| Hooks    | 3 (session-logger, session-auto-commit, governance-audit) | 3 stubs     | N/A           |
| Config   | config.yaml                                               | config.toml | opencode.json |

## Detailed Inventory

### Skills

**Hermes** (`~/AppData/Local/hermes/skills/`)

- Total: 621 skills across 33 categories + 30 flat
- Categories: architecture, autonomous-ai-agents, blockchain, communication, creative, data-science, development, devops, email, finance, gaming, github, health, mcp, media, migration, mlops, note-taking, oh-my-hermes, payments, planning, product, productivity, qa, reference, research, security, smart-home, social-media, software-development, tooling, web-development

**Codex** (`~/.codex/skills/hermes-auto/`)

- Total: 621 skills (synced from Hermes)
- 27 flat skills, 594 categorized
- Flat skills (to be deduplicated): 27 skills that also exist in categorized form

**OpenCode** (`~/.opencode/skills/hermes-auto/`)

- Total: 621 skills (synced from Hermes)
- 27 flat skills, 594 categorized

### Profiles / Agents

**Hermes Profiles** (13):

- alexa, code-architect, creative-director, cto, designer, dev, exec-assistant, ops, patient-tutor, pm, qa, research-analyst, security

**Codex Agents** (144 agents):

- All agents in `~/.codex/agents/*.toml`
- Key agents mapped to Hermes profiles: architect-reviewer, code-reviewer, debugger, devops-engineer, documentation-engineer, prompt-engineer, project-manager, technical-writer, refactoring-specialist, security-auditor, test-automator, tooling-engineer, workflow-orchestrator, codebase-orchestrator, multi-agent-coordinator, task-distributor, ai-engineer, ml-engineer, mlops-engineer, data-engineer, data-scientist, research-analyst, knowledge-synthesizer, api-designer, api-documenter, graphql-architect, frontend-developer, react-specialist, nextjs-developer, typescript-pro, python-pro, golang-pro, rust-engineer, java-architect, cpp-pro, csharp-developer, kotlin-specialist, swift-expert, php-pro, docker-expert, kubernetes-specialist, terraform-engineer, cloud-architect, azure-infra-engineer

### Hooks

**Hermes** (3 hooks in `~/AppData/Local/hermes/hooks/`):

1. **session-logger** - Logs prompts, session start/end
2. **session-auto-commit** - Auto-commits session state
3. **governance-audit** - Audits sessions for governance

**Codex** - Hook support via plugins (3 stubs found)

**OpenCode** - No native hook system

### Plugins

**Hermes** (15 enabled plugins):

- basic, custom-provider, disk-cleanup, huggingface-provider, langfuse, nous, nous-provider, ollama-cloud-provider, openai-codex, openai-codex-provider, opencode-zen-provider, openrouter-provider, security-guidance, web-tavily

**Codex** (10 enabled plugins in config.toml):

- documents@openai-primary-runtime, presentations@openai-primary-runtime, spreadsheets@openai-primary-runtime, github@openai-curated, superpowers@openai-curated, pdf@openai-primary-runtime, template-creator@openai-primary-runtime, visualize@openai-bundled, chrome@openai-bundled, computer-use@openai-bundled, browser@openai-bundled

**OpenCode** - No plugin system (uses npm packages)

### Configuration

| Setting          | Hermes                             | Codex        | OpenCode                        |
| ---------------- | ---------------------------------- | ------------ | ------------------------------- |
| Primary Model    | gpt-5.4-mini                       | gpt-5.4-mini | opencode/deepseek-v4-flash-free |
| Provider         | openai-codex                       | OpenAI       | OpenCode Zen                    |
| Fallback         | opencode-zen/nemotron-3-ultra-free | N/A          | N/A                             |
| Reasoning Effort | N/A                                | xhigh        | N/A                             |
| Personality      | 213 entries                        | pragmatic    | N/A                             |

## Sync Status

✅ Skills: All 621 Hermes skills synced to Codex and OpenCode (3 missing skills added)
✅ Hooks: Hermes hooks copied to workspace `.github/hooks/`
⚠️ Profiles ↔ Agents: Mapping documented; Hermes has 13 profiles, Codex has 144 agents
⚠️ Config: Models differ by platform (expected - platform-specific optimization)
⚠️ Plugins: Platform-specific; no cross-platform sync possible
⚠️ Personalities: Hermes has 213 personalities; Codex uses single 'pragmatic' personality

## Conflicts Documented

1. **Model differences**: Each platform uses its optimized model/provider
2. **Profile vs Agent**: Hermes profiles (13) ≠ Codex agents (144) - different granularity
3. **Personalities**: Hermes has extensive personality library; Codex uses single personality
4. **Plugins**: Platform-specific implementations
5. **Hooks**: Only Hermes has full hook system

## Recommendations

1. **Keep platform-optimized models** - Don't force same model across platforms
2. **Map priority Codex agents → Hermes profiles** - Create Hermes profiles for key agents
3. **Deduplicate flat skills** - Remove 27 flat skill duplicates in Codex/OpenCode that have categorized counterparts
4. **Sync hooks to workspace** - Already done for CI/CD compatibility
