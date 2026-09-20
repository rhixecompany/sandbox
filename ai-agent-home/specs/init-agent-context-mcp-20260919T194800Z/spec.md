# Agent Context MCP and Workflow Specification

**Status:** COMPLETE  
**Run:** `init-agent-context-mcp-20260919T194800Z`

## Objective

Extend the completed cross-agent initialization with project command coverage, MCP guidance across Copilot/Hermes/Cursor/OpenCode surfaces, and concrete clarification-to-completion workflow examples.

## Confirmed Scope

- Update root agent adapters and canonical Copilot guidance.
- Treat `.github/mcp.json` as the repository MCP source and document `.vscode/mcp.json` as an editor mirror.
- Document high-value commands for Banking, comicwise, Bash, ecom, MCP servers, and Python projects, including targeted-test patterns.
- Add full workflow examples for clarification, artifact lifecycle, validation, blockers, and completion.
- Do not duplicate servers or hardcode credentials.

## MCP Coverage

- Playwright: browser/UI validation.
- tooling-lint: ESLint, Prettier, Markdown linting.
- python-quality: Ruff and Pyright.
- github: repository and pull-request operations.

## Acceptance Criteria

- Root adapters consistently reference MCP source and workflow.
- High-value command matrix reflects observed project manifests.
- New run artifacts are updated through validation and final completion.

## Completion Evidence

- Added MCP guidance for Playwright, tooling-lint, python-quality, and GitHub.
- Confirmed all four requested servers exist in both `.github/mcp.json` and `.vscode/mcp.json`.
- Added observed high-value command and targeted-test coverage for the major project stacks.
- Added the full clarification, artifact, audit, implementation, verification, and completion workflow.
- Markdownlint, JSON parsing, local-link validation, and `git diff --check` passed.
