# multi-agent-research-template — Dependency Context Catalog

**Generated:** 2026-06-14
**Source File:** `./sample.prompt.txt`
**Purpose:** multi-agent-research-template

---

## Forward Dependencies (Extracted from Source)

### Markdown Links (URLs Referenced)
| Link Text | Target URL | Phase |
|-----------|------------|-------|
| `https://github.com/0xNyk/awesome-hermes-agent` | https://github.com/0xNyk/awesome-hermes-agent | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills` | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp` | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes` | https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/personality` | https://hermes-agent.nousresearch.com/docs/user-guide/features/personality | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files` | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/getting-started/quickstart` | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/guides/tips` | https://hermes-agent.nousresearch.com/docs/guides/tips | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/tools` | https://hermes-agent.nousresearch.com/docs/user-guide/features/tools | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/getting-started/learning-path` | https://hermes-agent.nousresearch.com/docs/getting-started/learning-path | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks` | https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks | Phase 3 |
| `https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins` | https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins | Phase 3 |

### @mentions
| Mention | Context |
|---------|---------|
| (none found) | — |

### /commands Referenced
| Command | Location | Context |
|---------|----------|---------|
| `/plan` | Phase 1, Step 1; Core Workflow Step 1 | Update existing plan |
| `hermes profile create {name} --clone-all` | Phase 4, Step 3 | Create profiles |
| `hermes skills audit` | Phase 6 implications | Skills audit |
| `hermes mcp install` | Phase 2/6 implications | MCP server installation |

### Plan Namespaces Referenced
| Namespace | Location |
|-----------|----------|
| `multi-agent-research-template` | Implicit (file identity) |
| Phase 1-6 workflow namespaces | Each phase section |

### Skills Referenced (Frontmatter Tags)
| Skill/Tag | Location |
|-----------|----------|
| `codex` | Frontmatter tags |
| `copilot` | Frontmatter tags |
| `hermes` | Frontmatter tags |
| `research` | Frontmatter tags |
| `planning` | Frontmatter tags |
| `automation` | Frontmatter tags |

### Template Variables
| Variable | Value |
|----------|-------|
| `{{workspace_root}}` | `C:\Users\Alexa\Desktop\SandBox` |
| `{{docs_root}}` | `docs/` |
| `{{agent_name}}` | `Codex` \| `Copilot` \| `Hermes` |
| `{{native_plan}}` | Active agent's planning command |
| `{{native_search}}` | Active agent's search command |
| `{{native_extract}}` | Active agent's extraction command |
| `{{native_files}}` | Active agent's file read/write command |

### MCP Servers/Tools Listed for Research (Phase 2)
vitest, playwright, django, sequential-thinking, context7, sentry, github official, gitmcp, fetch, scrapegraph, time, memory, youtube transcripts, Desktop Commander, filesystem, node.js sandbox, redis, sqlite, hacker news, markdownify, google maps, ast-grep, npm sentinel, postman, cloud run, stripe, apify, chroma, python refactoring assistant, neo4j memory, api gateway, next.js devtools, python interpreter, gemini api docs, hostinger api, google flights, neon, shadcn, uv, linear, mcp-docker

---

## Reverse Dependencies (Files Referencing This File)

| Referencing File | Reference Type | Context |
|------------------|----------------|---------|
| `docs/sample-prompt-execution-index.md` | Markdown link + Title | Execution index mapping targets to docs |
| `docs/multi-agent-research-template-context.md` | Context catalog | Previous enhance-markdown Phase 1 context |
| `docs/multi-agent-research-template-issues-context.md` | Issues context | Previous enhance-markdown Phase 1 issues |
| `docs/multi-agent-research-template-fix-issues-context.md` | Fix issues context | Previous enhance-markdown Phase 2 fix context |
| `docs/multi-agent-research-template-verify-context.md` | Verify context | Previous enhance-markdown Phase 4 verify |
| `thoughts/plans/multi-agent-research-template-debug.md` | Debug plan | Previous enhance-markdown Phase 2 fix plan |

---

## Related Artifacts (Existing — from prior enhance-markdown run)

| Artifact | Type | Description |
|----------|------|-------------|
| `docs/sample-prompt-execution-index.md` | Execution index | Maps prompt targets to workspace docs (12 Phase 3 URLs extracted) |
| `docs/multi-agent-research-template-context.md` | Phase 1 context | Dependency catalog from prior run |
| `docs/multi-agent-research-template-issues-context.md` | Phase 1 issues | Audit findings from prior run |
| `docs/multi-agent-research-template-fix-issues-context.md` | Phase 2 fix context | Fix plan + progress log from prior run |
| `docs/multi-agent-research-template-verify-context.md` | Phase 4 verify | Verification report from prior run |
| `thoughts/plans/multi-agent-research-template-debug.md` | Phase 2 plan | Dual-channel fix plan (Batch 1 ready, Batch 2 pending) |

---

## Notes

- This file (`sample.prompt.txt`) is a **cross-system prompt template** for Codex, Copilot, and Hermes
- Contains a 6-phase workflow with template variables for agent-agnostic execution
- Phase 2 lists 50+ MCP servers/tools for research
- Phase 3 lists 12 Hermes documentation URLs for extraction
- Phase 4-6 cover profiles, docs inventory, and config hierarchy audit
- Prior enhance-markdown run completed Phases 1-2 (fix plan created), Phase 3-4 not completed
- File has YAML frontmatter but missing `name` field (has `title`, `description`, `tags`, `mode`)
- Frontmatter uses `mode: agent` which is non-standard for Hermes prompts