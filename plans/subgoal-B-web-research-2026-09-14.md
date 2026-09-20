# Subgoal B — Web-Research (OpenRouter Free Models) + Agent-Browser

## Goal

- Use `/goal /using-superpowers /brainstorming /user-communication-preferences` + web-search/web-extract + agent-browser (`https://openrouter.ai/models?variant=free`).
- Convert HTML page to markdown; generate markdown report of free models.
- Execute `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (referenced by user) on each model in report.
- Deliver artifacts: report, converted prompt results, plan, spec, results file.

## Skills Referenced (14-skill stack — reference by name; use native equivalents if unavailable)

- /using-superpowers /brainstorming /user-communication-preferences /multi-file-change-protocol /mcp-sequential-thinking /mcp-filesystem /mcp-ast-grep /mcp-memory /writing-clearly-and-concisely /subagent-driven-development /plan /plan-mode /plans-and-specs /create-implementation-plan /update-implementation-plan /implementation-plan /execute-implementation-plan /executing-plans /create-implementation-spec /update-implementation-spec /implementation-spec /execute-implementation-spec /executing-specs /create-implementation-prompt /update-implementation-prompt /implementation-prompt /execute-implementation-prompt /executing-prompts /systematic-debugging /skill-creator /skill-judge /prompts-judge /specs-judge /scripts-judge

## Tools

- `agent-browser`: browser_exec with real profile (pre-configured; user confirmed `yes use the tool`).
- `web-research-pipeline`: web-search (tavily/backend), web-extract, fetch.
- `mcp-tavily`, `mcp-parallel-search`, `mcp-fetch`: MCP server integration.

## Verification Gates

- Gate B1: Agent-browser fetch of `https://openrouter.ai/models?variant=free` executed (verified by page info / screenshot / content hash).
- Gate B2: HTML converted to markdown (verified by `.md` artifact size/content).
- Gate B3: Markdown report of free models created with real URLs / descriptions (no synthetic model names / capabilities).
- Gate B4: `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` executed per model (verified by prompt output artifacts — real responses only).
- Gate B5: Results file (`results/web-research-subgoal-B-*.md`) contains verified model outputs with real file paths/sizes.

## Rules Enforced

- Best quality (full verification gates, subagent delegation, all approvals).
- No synthetic session IDs / capabilities / quality scores / rankings / artifacts.
- .env 3334 B protected; identity preserved; DRY enforced; sequential A→B order maintained.
- All crud batches approved (approval mechanism: clarification / kanban_request_review).
- Subagent delegated with full context (workspace, user identity, authorization FULL, security preservation, DRY rules, model/fallback info).
