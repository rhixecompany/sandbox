# MCP Server Reference Catalog (for prompt `tool:` validation)

When a `.prompt.md` `dependencies:` list contains a `tool:` entry, it must be an
**MCP server** named `mcp-<server>`. Built-in Hermes toolsets (e.g. `terminal`,
`file`, `search_files`, `web_search`) belong in the top-level `toolsets:` field,
NOT under `tool:`. Listing a toolset under `tool:` is a mislabel — the
capability exists, but it is in the wrong field.

## Rule

- `tool:terminal` ❌ wrong → put `terminal` in `toolsets:`
- `tool:mcp-filesystem` ✅ correct → `mcp-filesystem` is an MCP server
- `tool:search_files` ❌ wrong → `search_files` is a toolset, not an MCP server
- `tool:delegate_task` ❌ wrong → agent facility, not an MCP server

## Known-good MCP server set

These `mcp-*` servers are recognized. Any `tool:mcp-<x>` where `<x>` is NOT in
this set should be flagged as `UNKNOWN_MCP` (could be a typo or a newly-added
server that needs cataloging):

```
ast-grep, code-sandbox, codex, copilot-mcp, fetch, filesystem,
github, linear, mcp-docker, memory, mindstudio, playwright,
sequential-thinking, smithery
```

## Observed in this library (all resolved OK)

- `mcp-fetch`, `mcp-filesystem`, `mcp-github`, `mcp-memory`,
  `mcp-playwright`, `mcp-sequential-thinking`

## How to regenerate this catalog

Re-derive the set of physically-available MCP tool servers by scanning the
skills tree for `mcp/` skill dirs that advertise an MCP server, or trust the
hardcoded known-good list above for audit purposes. The reusable audit script
`scripts/audit_skill_mcp_refs.py` encodes this check.
