# Plan: Sync MCP configs + lightweight update (verified 2026-09-20)

## Discovery (complete)

- opencode --help / mcp --help: PASS
- copilot --help / mcp --help: PASS (config files: ~/.copilot/mcp-config.json, .mcp.json)
- hermes --help / mcp --help: PASS (config.yaml)
- cursor-agent binary: NOT FOUND; docs = .cursor/rules/sandbox.mdc + workspace docs
- agent binary: NOT FOUND; agent config = agent-config-inventory.json + .codex/config.toml
- opencode.json duplicates: 0 duplicates (only /c/Users/Alexa/.config/opencode/opencode.json)

## Clarification (verified)

- Skip duplicate deletion (none exist)
- Apply opencode's _lightweight_mapping globally to hermes + copilot
- 'agent' = agent-config-inventory.json / .codex/config.toml; 'cursor-agent' = .cursor docs

## Changes (destructive/config — confirm once, then execute)

1. hermes config.yaml: disable heavy servers (playwright, code-sandbox, smithery, mcp-docker, mindstudio, parallel-search, parallel-task, neon, sentry, honcho, tavily, atlassian, twilio-docs, coderabbit-cli-mcp, docs plugins) — keep filesystem, github, ast-grep, memory, sequential-thinking, context7, fetch, tooling
2. copilot .mcp.json: disable same heavy servers; keep same core set
3. agent-config-inventory.json: add lightweight note referencing applied mapping
4. Document in plan verification file

## Risk note

Config edits disable MCP servers; native equivalents (execute_code, terminal, tool_search, subagent/delegate) must work independently. If native equivalents fail, restore from git/config backup.

=== VERIFICATION (2026-09-20) ===
opencode.json duplicates: 0 (only /c/Users/Alexa/.config/opencode/opencode.json, size=1907 B)
hermes config.yaml: enabled=7, disabled=22 (core kept, heavy disabled)
copilot .mcp.json: enabled=7, disabled=14 (core kept, heavy disabled)
agent-config-inventory.json: updated with lightweight note
cursor-agent (.cursor/rules/sandbox.mdc): no binary config edited; docs referenced in inventory
No .env secrets exposed; no .bak created; identity rules preserved (DRY refs to .hermes.md/user-communication-preferences)
