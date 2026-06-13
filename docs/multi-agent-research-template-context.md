# multi-agent-research-template — Context Catalog

Generated: 2026-06-13 Source file: C:\Users\Alexa\Desktop\SandBox\sample.prompt.md

## Summary

This file is the master reusable prompt template for executing a 6-phase research and implementation workflow across Codex, Copilot, and Hermes agents. It defines template variables, agent mappings, shared rules, core workflow, and detailed research targets for Phases 1-6 covering skills audit, MCP server research, Hermes docs extraction, profile creation, docs inventory, and configuration hierarchy audit.

## Forward References (this file → others)

| Type | Reference | Path | Exists? |
|------|-----------|------|---------|
| Markdown link | sample.prompt.md (self) | C:\Users\Alexa\Desktop\SandBox\sample.prompt.md | ✅ |
| Directory reference | `docs/` | C:\Users\Alexa\Desktop\SandBox\docs\ | ✅ |
| Command trigger | `/plan` | Hermes built-in | ✅ |
| Command trigger | `/skills browse` | Hermes built-in | ✅ |
| Command trigger | `/skills search` | Hermes built-in | ✅ |
| Command trigger | `/skills audit` | Hermes built-in | ✅ |
| Command trigger | `/systematic-debugging` | Hermes skill | ✅ |
| Command trigger | `hermes profile create` | Hermes CLI | ✅ |
| Command trigger | `--clone-all` | Hermes CLI flag | ✅ |
| URL | https://github.com/0xNyk/awesome-hermes-agent | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/personality | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/guides/tips | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/tools | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/getting-started/learning-path | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks | External | ✅ |
| URL | https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins | External | ✅ |
| MCP Server | vitest | External | ❓ |
| MCP Server | playwright | External | ❓ |
| MCP Server | django | External | ❓ |
| MCP Server | sequential-thinking | External | ❓ |
| MCP Server | context7 | External | ❓ |
| MCP Server | sentry | External | ❓ |
| MCP Server | github official | External | ❓ |
| MCP Server | gitmcp | External | ❓ |
| MCP Server | fetch | External | ❓ |
| MCP Server | scrapegraph | External | ❓ |
| MCP Server | time | External | ❓ |
| MCP Server | memory | External | ❓ |
| MCP Server | youtube transcripts | External | ❓ |
| MCP Server | Desktop Commander | External | ❓ |
| MCP Server | filesystem | External | ✅ (configured) |
| MCP Server | node.js sandbox | External | ❓ |
| MCP Server | redis | External | ❓ |
| MCP Server | markitdown | External | ❓ |
| MCP Server | google maps | External | ❓ |
| MCP Server | ast-grep | External | ✅ (configured) |
| MCP Server | npm sentinel | External | ❓ |
| MCP Server | sqlite | External | ❓ |
| MCP Server | hacker news | External | ❓ |
| MCP Server | markdownify | External | ❓ |
| MCP Server | postman | External | ❓ |
| MCP Server | cloud run | External | ❓ |
| MCP Server | stripe | External | ❓ |
| MCP Server | apify | External | ❓ |
| MCP Server | chroma | External | ❓ |
| MCP Server | python refactoring assistant | External | ❓ |
| MCP Server | neo4j memory | External | ❓ |
| MCP Server | api gateway | External | ❓ |
| MCP Server | next.js devtools | External | ❓ |
| MCP Server | python interpreter | External | ❓ |
| MCP Server | gemini api docs | External | ❓ |
| MCP Server | hostinger api | External | ❓ |
| MCP Server | google flights | External | ❓ |
| MCP Server | neon | External | ❓ |
| MCP Server | shadcn | External | ❓ |
| MCP Server | uv | External | ❓ |
| MCP Server | linear | External | ✅ (configured) |
| MCP Server | mcp-docker | External | ✅ (configured) |

## Reverse References (others → this file)

| Type | Source File | Reference | Context snippet |
|------|-------------|-----------|-----------------|
| Markdown link | docs/hermes/index.md | `[sample.prompt.md](file:///C:/Users/Alexa/Desktop/SandBox/sample.prompt.md)` | Phase 3 targets |
| Text reference | docs/phase4-profiles-log.md | `sample.prompt.md` | Verified profile list and target profile names |
| Text reference | docs/phase3-hermes-docs-extraction-log.md | `sample.prompt.md` | Verified target URL list from Phase 3 |
| Text reference | docs/phase2-mcp-research-log.md | `sample.prompt.md` | Phase 2 target list inputs |
| Text reference | docs/phase1-skills-audit-log.md | `sample.prompt.md` | Began execution against sample.prompt.md |
| Markdown link | docs/sample-prompt-execution-index.md | `[sample.prompt.txt](../sample.prompt.txt)` | Execution index mapping targets to docs |

## Plans & Specs (plugin system)

| Namespace | Type | Status | Linked to source? |
|-----------|------|--------|-------------------|
| multi-agent-research-template-debug | plan | Not created | No |
| sample-prompt-execution | spec | Exists (execution index) | Yes |