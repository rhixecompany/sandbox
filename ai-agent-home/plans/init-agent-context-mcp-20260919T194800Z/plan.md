# Agent Context MCP and Workflow Plan

**Status:** COMPLETE  
**Run:** `init-agent-context-mcp-20260919T194800Z`

## Phases

1. Inspect existing MCP mappings and major project manifests.
2. Add MCP source-of-truth guidance and safe usage boundaries.
3. Add high-value build, lint, type-check, and targeted-test commands.
4. Add concrete clarification/artifact/validation workflow examples.
5. Validate changed Markdown, links, JSON syntax, and diff integrity.
6. Record evidence and mark all run artifacts complete.

## Validation

- Markdownlint all changed Markdown/context files.
- Parse `.github/mcp.json` and `.vscode/mcp.json`.
- Validate local links and required artifact paths.
- Run `git diff --check`.
- Do not run project code suites because this follow-up changes only documentation/config guidance; use observed manifests to verify command accuracy.

## Final Status

- Root Copilot, Hermes, Cursor, and pointer guidance now documents the canonical MCP source and safe usage boundaries.
- Major-stack commands and single-test patterns were derived from current manifests.
- No MCP server definitions were duplicated or credentials added because the requested servers were already configured in both workspace mappings.
- All selected validation gates passed.
