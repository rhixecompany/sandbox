# `sample.prompt.txt` Execution Index

**Updated:** 2026-06-11

This catalog maps the default target groups in [`sample.prompt.txt`](../sample.prompt.txt) to the documentation already present in the SandBox workspace.

Most of the linked page files already exist in the repo. This index is the cross-reference layer that ties them back to the prompt's workflow and highlights the few requested pages that are still missing.

---

## Target Group 1: Skills Discovery and Audit

| Artifact | Purpose |
|---|---|
| [docs/skills-audit/index.md](skills-audit/index.md) | Skills audit master index and score table |
| [docs/skills-debug-context.md](skills-debug-context.md) | Audit context and summary findings |
| [docs/SKILLS_FIX_EXECUTION_SUMMARY.md](SKILLS_FIX_EXECUTION_SUMMARY.md) | Phase 1-3 execution summary |
| [missing_skills.txt](../missing_skills.txt) | Skills identified as missing |
| [deficient_skills.txt](../deficient_skills.txt) | Skills flagged as weak or incomplete |
| [skills_missing_goal.txt](../skills_missing_goal.txt) | Goal-related gaps |
| [skills_missing_workflow.txt](../skills_missing_workflow.txt) | Workflow-related gaps |

## Target Group 2: MCP Server and Tool Research

| Artifact | Purpose |
|---|---|
| [docs/context7.md](context7.md) | Context7 MCP research summary |
| [docs/github-official.md](github-official.md) | Official GitHub MCP documentation summary |
| [docs/playwright.md](playwright.md) | Playwright MCP research summary |
| [docs/vitest.md](vitest.md) | Vitest MCP research summary |
| [docs/django-mcp-server.md](django-mcp-server.md) | Django MCP server summary |
| [docs/gitmcp.md](gitmcp.md) | GitMCP summary |
| [docs/mcp-server-fetch-typescript.md](mcp-server-fetch-typescript.md) | Fetch MCP research summary |
| [docs/scrapegraph.md](scrapegraph.md) | ScrapeGraph MCP summary |
| [docs/markitdown-mcp-server.md](markitdown-mcp-server.md) | MarkItDown MCP summary |
| [docs/markdownify-mcp.md](markdownify-mcp.md) | Markdownify MCP summary |
| [docs/mcp-google-map.md](mcp-google-map.md) | Google Maps MCP summary |
| [docs/sentry.md](sentry.md) | Sentry MCP summary |
| [docs/apify.md](apify.md) | Apify MCP summary |
| [docs/chroma.md](chroma.md) | Chroma MCP summary |
| [docs/linear.md](linear.md) | Linear MCP summary |
| [docs/neo4j-memory.md](neo4j-memory.md) | Neo4j memory summary |
| [docs/neon.md](neon.md) | Neon MCP summary |
| [docs/nextjs-devtools.md](nextjs-devtools.md) | Next.js DevTools summary |
| [docs/python-interpreter.md](python-interpreter.md) | Python Interpreter MCP summary |
| [docs/node-js-sandbox.md](node-js-sandbox.md) | Node.js sandbox MCP summary |
| [docs/shadcn.md](shadcn.md) | shadcn MCP summary |
| [docs/youtube-transcripts.md](youtube-transcripts.md) | YouTube transcripts MCP summary |
| [docs/desktop-commander.md](desktop-commander.md) | Desktop Commander summary |

### Known gaps

`docs/INDEX.md` still flags several requested tools as missing or incomplete, including `redis`, `sqlite`, `hacker-news`, `postman`, `time`, `memory`, `ast-grep`, `stripe`, `cloud run`, `google flights`, `hostinger api`, and a few others from the original prompt.

## Target Group 3: Hermes Docs and Ecosystem

| Artifact | Purpose |
|---|---|
| [docs/awesome-hermes-agent/README.md](awesome-hermes-agent/README.md) | Hermes ecosystem reference list |
| [docs/getting-started/quickstart/README.md](getting-started/quickstart/README.md) | Quickstart guide |
| [docs/getting-started/learning-path/README.md](getting-started/learning-path/README.md) | Learning path guide |
| [docs/guides/tips/README.md](guides/tips/README.md) | Tips and workflow guidance |
| [docs/guides/use-mcp-with-hermes/README.md](guides/use-mcp-with-hermes/README.md) | Hermes + MCP integration guide |
| [docs/user-guide/features/skills/README.md](user-guide/features/skills/README.md) | Skills feature documentation |
| [docs/user-guide/features/mcp/README.md](user-guide/features/mcp/README.md) | MCP feature documentation |
| [docs/user-guide/features/personality/README.md](user-guide/features/personality/README.md) | Personality feature documentation |
| [docs/user-guide/features/context-files/README.md](user-guide/features/context-files/README.md) | Context files feature documentation |
| [docs/user-guide/features/hooks/README.md](user-guide/features/hooks/README.md) | Hooks feature documentation |
| [docs/user-guide/features/plugins/README.md](user-guide/features/plugins/README.md) | Plugins feature documentation |
| [docs/user-guide/features/tools/README.md](user-guide/features/tools/README.md) | Tools feature documentation |

## Target Groups 4-6: Profiles, Backup Inventory, Configuration Audit

| Artifact | Purpose |
|---|---|
| [docs/HERMES_PROFILE_SETUP_COMPLETE.md](HERMES_PROFILE_SETUP_COMPLETE.md) | Profile setup completion report |
| [docs/HERMES_PROFILES_GUIDE.md](HERMES_PROFILES_GUIDE.md) | Profile guidance |
| [docs/HERMES_CONFIGURATION_STATUS.md](HERMES_CONFIGURATION_STATUS.md) | Current configuration status |
| [docs/HERMES_CONFIGURATION_INVENTORY.md](HERMES_CONFIGURATION_INVENTORY.md) | Inventory of configuration artifacts |
| [docs/HERMES_COMPLETE_VERIFICATION.md](HERMES_COMPLETE_VERIFICATION.md) | Verification report |
| [docs/HERMES_MCP_CONFIGURATION_GUIDE.md](HERMES_MCP_CONFIGURATION_GUIDE.md) | MCP configuration guide |
| [docs/HERMES_MIGRATION_COMPLETION_REPORT.md](HERMES_MIGRATION_COMPLETION_REPORT.md) | Hermes migration completion report |
| [docs/HERMES_DOCUMENTATION_INDEX.md](HERMES_DOCUMENTATION_INDEX.md) | Compatibility landing page for older Hermes links |
| [docs/INDEX.md](INDEX.md) | Canonical docs hub for the broader MCP/tool catalog |

## Working Notes

- The prompt's page-level extraction work is already represented in the repository.
- This file is intentionally narrow: it indexes the artifacts already on disk rather than duplicating their contents.
- If you want the remaining missing MCP/tool pages filled in, the next step is to extend the docs set and then refresh `docs/INDEX.md`.
