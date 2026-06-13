# Hermes Agent Documentation Index — Phase 3 Extraction

**Generated:** 2026-06-13  
**Source:** [sample.prompt.md](file:///C:/Users/Alexa/Desktop/SandBox/sample.prompt.md) Phase 3 targets  
**Extraction Method:** `web_extract` (primary) + full content preservation  
**Total Pages:** 12/12 ✅

---

## Catalog

| # | File | Source URL | Status | Size (chars) |
|---|------|------------|--------|--------------|
| 1 | [github.com_0xNyk_awesome-hermes-agent.md](hermes-agent.nousresearch.com_docs_user-guide_features_skills.md) | https://github.com/0xNyk/awesome-hermes-agent | ✅ Extracted | ~3000+ |
| 2 | [hermes-agent.nousresearch.com_docs_user-guide_features_skills.md](hermes-agent.nousresearch.com_docs_user-guide_features_skills.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | ✅ Extracted | ~8000+ |
| 3 | [hermes-agent.nousresearch.com_docs_user-guide_features_mcp.md](hermes-agent.nousresearch.com_docs_user-guide_features_mcp.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | ✅ Extracted | ~10000+ |
| 4 | [hermes-agent.nousresearch.com_docs_guides_use-mcp-with-hermes.md](hermes-agent.nousresearch.com_docs_guides_use-mcp-with-hermes.md) | https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes | ✅ Extracted | ~9000+ |
| 5 | [hermes-agent.nousresearch.com_docs_user-guide_features_personality.md](hermes-agent.nousresearch.com_docs_user-guide_features_personality.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/personality | ✅ Extracted | ~7000+ |
| 6 | [hermes-agent.nousresearch.com_docs_user-guide_features_context-files.md](hermes-agent.nousresearch.com_docs_user-guide_features_context-files.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files | ✅ Extracted | ~5500 |
| 7 | [hermes-agent.nousresearch.com_docs_getting-started_quickstart.md](hermes-agent.nousresearch.com_docs_getting-started_quickstart.md) | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | ✅ Extracted | ~6500 |
| 8 | [hermes-agent.nousresearch.com_docs_guides_tips.md](hermes-agent.nousresearch.com_docs_guides_tips.md) | https://hermes-agent.nousresearch.com/docs/guides/tips | ✅ Extracted | ~5500 |
| 9 | [hermes-agent.nousresearch.com_docs_user-guide_features_tools.md](hermes-agent.nousresearch.com_docs_user-guide_features_tools.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/tools | ✅ Extracted | ~5600 |
| 10 | [hermes-agent.nousresearch.com_docs_getting-started_learning-path.md](hermes-agent.nousresearch.com_docs_getting-started_learning-path.md) | https://hermes-agent.nousresearch.com/docs/getting-started/learning-path | ✅ Extracted | ~4600 |
| 11 | [hermes-agent.nousresearch.com_docs_user-guide_features_hooks.md](hermes-agent.nousresearch.com_docs_user-guide_features_hooks.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks | ✅ Extracted | ~5800 |
| 12 | [hermes-agent.nousresearch.com_docs_user-guide_features_plugins.md](hermes-agent.nousresearch.com_docs_user-guide_features_plugins.md) | https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins | ✅ Extracted | ~7500 |

---

## Topic Clusters

### Core Features
- **Skills** — Progressive disclosure, SKILL.md format, CLI commands, bundles
- **MCP** — Model Context Protocol integration, server config, tool filtering, WSL2 bridging
- **Personality/SOUL.md** — Agent identity, built-in personalities, custom configs
- **Context Files** — AGENTS.md, CLAUDE.md, SOUL.md, .cursorrules loading priority
- **Tools/Toolsets** — Built-in tools, terminal backends (local/Docker/SSH/Modal/Daytona), configuration
- **Hooks** — Gateway hooks, plugin hooks, shell hooks, event types
- **Plugins** — Plugin structure, ctx APIs, discovery sources, security model

### Getting Started
- **Quickstart** — Install, provider selection (30+ providers), first chat, troubleshooting
- **Learning Path** — Beginner/Intermediate/Advanced tracks, use-case paths, feature directory
- **Tips & Best Practices** — Prompting, context files, memory vs skills, CLI shortcuts, performance, security

### Ecosystem
- **Awesome Hermes Agent** — Curated community resources (skills, plugins, tools, deployments, playbooks)

---

## Verification

```bash
# Count files
ls docs/hermes/*.md | wc -l
# → 12

# Verify each has source URL header
head -3 docs/hermes/*.md
# → All show "# Source: <URL>"
```

---

## Next Phase

**Phase 4:** Profiles and Workspace Markdown  
- Research all Markdown files in `docs/*`
- Identify available profiles
- Create profiles with `hermes profile create {name} --clone-all`
- Verify clones copy config, keys, SOUL.md, memories, skills, sessions

**Phase 5:** Docs Inventory  
- Inspect `docs/*` for hooks, skills, plugins
- Install plugins first
- Verify/test/debug plugins → hooks → skills

**Phase 6:** Configuration Hierarchy Audit  
- List all: hooks, tools, skills, plugins, MCP servers
- Validate config hierarchy: `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`