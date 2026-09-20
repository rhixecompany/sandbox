---
name: init-agent-context-mcp
version: 1.0.0
status: complete
run: init-agent-context-mcp-20260919T194800Z
---

# Extend Agent Context with MCP and Workflow Guidance

## Clarify First

Ask up to three focused questions per turn until all required, optional, recommended, blocker, and approval decisions are covered. Ask about the old/new request, scope, remaining tasks, blockers, MCP surfaces, command coverage, and approval gates.

## Inspect

Read `AGENTS.md`, `.github/copilot-instructions.md`, `.hermes.md`, `.cursorrules`, `.cursor/rules/`, `.github/mcp.json`, `.vscode/mcp.json`, and the manifests for major projects.

## Implement

- Keep `AGENTS.md` canonical and adapters thin.
- Use `.github/mcp.json` as the MCP source of truth.
- Document Playwright, tooling-lint, python-quality, and GitHub use without exposing credentials.
- Document only observed project commands and targeted-test patterns.
- Add the clarification → artifact → audit → implement → verify → close workflow.
- Update the current run's spec, plan, and prompt after each phase.

## Verify

Run Markdownlint, JSON parsing, local-link checks, and `git diff --check`. Record unrelated pre-existing failures separately.

## Complete

Set all current-run artifacts to `complete` only after the selected gates pass and evidence is written.

## Completion Evidence

MCP mappings parse successfully in `.github/mcp.json` and `.vscode/mcp.json`; requested servers are present, changed documentation passes markdownlint, local links resolve, and `git diff --check` passes.
