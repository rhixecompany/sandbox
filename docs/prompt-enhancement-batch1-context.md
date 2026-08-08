# Prompt Enhancement Batch 1 - Context & Dependency Catalog

## Batch 1: 5 Most Recently Updated Prompts

| #   | Path                                             | Name                   | Title                                | Timestamp  |
| --- | ------------------------------------------------ | ---------------------- | ------------------------------------ | ---------- |
| 1   | .github/prompts/smithery-setup.prompt.md         | smithery-setup         | Smithery MCP Setup and Configuration | 1786135016 |
| 2   | .github/prompts/all-repo-docker-setup.prompt.md  | all-repo-docker-setup  | All Repository Docker Setup          | 1786133307 |
| 3   | .github/prompts/execute-all-prompts.prompt.md    | execute-all-prompts    | Execute All Prompts Orchestrator     | 1785893256 |
| 4   | .github/prompts/sync-hermes-opencode.prompt.md   | sync-hermes-opencode   | Sync Hermes OpenCode Codex           | 1785893123 |
| 5   | .github/prompts/tooling-implementation.prompt.md | tooling-implementation | Full Tooling Implementation          | 1785892726 |

## Prompt 1: smithery-setup.prompt.md

- **Tags**: mcp, smithery, configuration, tools, workflow, integration
- **Skills**: mcp, hermes-mcp, mcp-smithery, native-mcp, mcporter, mcp-fetch, mcp-filesystem, mcp-github, sequential-thinking, verification-before-completion, executing-plans, executing-prompt-workflows
- **Toolsets**: file, terminal, skills, mcp
- **Dependencies**: skill:using-superpowers, skill:session-audit-report, skill:hermes-profiles, skill:validate-memories
- **Forward Refs**: templates/sync-hermes-opencode/phases.md, templates/_shared/rules-core.md, templates/_shared/personas.md, templates/_shared/personality.md, templates/_shared/best-practices.md, templates/_shared/deps-core.md, templates/_shared/skills-table-core.md
- **Lines**: 854, Size: 27293 bytes

## Prompt 2: all-repo-docker-setup.prompt.md

- **Tags**: (none in frontmatter)
- **Skills**: using-superpowers, multi-stage-dockerfile, git-multi-repo-orchestration, docker-management, dependency-security-remediation, systematic-debugging, verification-before-completion, executing-plans, subagent-driven-development, workspace-audit, repo-management, technology-stack-blueprint-generator, architecture-blueprint-generator, folder-structure-blueprint-generator, context-map, enhance-markdown, writing-plans, plan
- **Toolsets**: terminal, file, code_execution, web, browser, mcp, delegation
- **Dependencies**: skill:using-superpowers, skill:multi-stage-dockerfile, skill:git-multi-repo-orchestration, skill:docker-management, skill:dependency-security-remediation, skill:systematic-debugging, skill:verification-before-completion, skill:executing-plans, skill:subagent-driven-development, skill:workspace-audit, skill:repo-management, skill:technology-stack-blueprint-generator, skill:architecture-blueprint-generator, skill:folder-structure-blueprint-generator, skill:context-map, skill:enhance-markdown, skill:writing-plans, skill:plan, tool:mcp-github, tool:mcp-docker, tool:mcp-filesystem, tool:mcp-playwright, tool:mcp-sequential-thinking, tool:mcp-fetch, tool:mcp-code-sandbox
- **Plan**: plans/all-repo-docker-setup.md
- **Trigger**: /all-repo-docker-setup
- **Lines**: 511, Size: 18050 bytes

## Prompt 3: execute-all-prompts.prompt.md

- **Tags**: ai-assistant, audit, data, execution, fix, ml, prompts, skills, typescript, workflow
- **Skills**: using-superpowers, user-communication-preferences, verification-before-completion, subagent-driven-development
- **Toolsets**: None
- **Dependencies**: skill:using-superpowers, skill:user-communication-preferences, skill:verification-before-completion, skill:subagent-driven-development
- **Forward Refs**: templates/execute-all-prompts/phases.md, templates/_shared/rules-core.md, templates/_shared/personas.md, templates/_shared/personality.md, templates/_shared/best-practices.md, templates/_shared/deps-core.md, templates/_shared/skills-table-core.md
- **Lines**: 185, Size: 6407 bytes

## Prompt 4: sync-hermes-opencode.prompt.md

- **Tags**: ai-assistant, data, prompts, skills, typescript, workflow
- **Skills**: multi-agent-sync, hermes-profiles, opencode
- **Toolsets**: file, terminal, skills
- **Dependencies**: skill:multi-agent-sync, skill:hermes-profiles, skill:opencode, skill:verification-before-completion
- **Plan**: None (references templates/sync-hermes-opencode/phases.md)
- **Forward Refs**: templates/sync-hermes-opencode/phases.md, templates/_shared/rules-core.md, templates/_shared/personas.md, templates/_shared/personality.md, templates/_shared/best-practices.md, templates/_shared/deps-core.md, templates/_shared/skills-table-core.md
- **Lines**: 161, Size: 5902 bytes

## Prompt 5: tooling-implementation.prompt.md

- **Tags**: configuration, linting, maintenance, tooling, workflow
- **Skills**: devops/tooling-implementation, software-development/executing-plans, software-development/executing-prompt-workflows, development/execute-workflow, software-development/python-quality, devops/tooling-lint, devops/tooling-config
- **Toolsets**: file, terminal, skills, todo
- **Scripts**: ~/AppData/Local/hermes/scripts/tooling_full_check.py
- **Dependencies**: skill:using-superpowers, skill:verification-before-completion
- **Forward Refs**: .hermes/plans/2026-08-01_tooling-implementation.md, templates/_shared/rules-core.md, templates/_shared/personas.md, templates/_shared/personality.md, templates/_shared/best-practices.md, templates/_shared/deps-core.md, templates/_shared/skills-table-core.md
- **Lines**: 167, Size: 8588 bytes

## Cross-Prompt Dependencies

- **smithery-setup** → references sync-hermes-opencode templates
- **all-repo-docker-setup** → references enhance-markdown skill, multiple blueprint generators
- **execute-all-prompts** → orchestrates audit-skills-judge-fix, agents-system-prompt-context-fix, sync-hermes-opencode, test-providers-models
- **sync-hermes-opencode** → uses multi-agent-sync skill
- **tooling-implementation** → references .hermes/plans/2026-08-01_tooling-implementation.md

## Common Template References

All prompts reference shared templates in `templates/_shared/`:

- rules-core.md
- personas.md
- personality.md
- best-practices.md
- deps-core.md
- skills-table-core.md
