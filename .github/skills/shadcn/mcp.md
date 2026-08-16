---
name: shadcn-mcp
description: "shadcn MCP Server"
version: 1.0.0
author: Alexa
---
     1|# shadcn MCP Server
     2|
     3|The CLI includes an MCP server that lets AI assistants search, browse, view, and install components from registries.
     4|
     5|---
     6|
     7|## Setup
     8|
     9|```bash
    10|shadcn mcp        # start the MCP server (stdio)
    11|shadcn mcp init   # write config for your editor
    12|```
    13|
    14|Editor config files:
    15|
    16|| Editor      | Config file                     |
    17|| ----------- | ------------------------------- |
    18|| Claude Code | `.mcp.json`                     |
    19|| Cursor      | `.cursor/mcp.json`              |
    20|| VS Code     | `.vscode/mcp.json`              |
    21|| OpenCode    | `opencode.json`                 |
    22|| Codex       | `~/.codex/config.toml` (manual) |
    23|
    24|---
    25|
    26|## Tools
    27|
    28|> **Tip:** MCP tools handle registry operations (search, view, install). For project configuration (aliases, framework, Tailwind version), use `npx shadcn@latest info` — there is no MCP equivalent.
    29|
    30|### `shadcn:get_project_registries`
    31|
    32|Returns registry names from `components.json`. Errors if no `components.json` exists.
    33|
    34|**Input:** none
    35|
    36|### `shadcn:list_items_in_registries`
    37|
    38|Lists all items from one or more registries.
    39|
    40|**Input:** `registries` (string[]), `limit` (number, optional), `offset` (number, optional)
    41|
    42|### `shadcn:search_items_in_registries`
    43|
    44|Fuzzy search across registries.
    45|
    46|**Input:** `registries` (string[]), `query` (string), `limit` (number, optional), `offset` (number, optional)
    47|
    48|### `shadcn:view_items_in_registries`
    49|
    50|View item details including full file contents.
    51|
    52|**Input:** `items` (string[]) — e.g. `["@shadcn/button", "@shadcn/card"]`
    53|
    54|### `shadcn:get_item_examples_from_registries`
    55|
    56|Find usage examples and demos with source code.
    57|
    58|**Input:** `registries` (string[]), `query` (string) — e.g. `"accordion-demo"`, `"button example"`
    59|
    60|### `shadcn:get_add_command_for_items`
    61|
    62|Returns the CLI install command.
    63|
    64|**Input:** `items` (string[]) — e.g. `["@shadcn/button"]`
    65|
    66|### `shadcn:get_audit_checklist`
    67|
    68|Returns a checklist for verifying components (imports, deps, lint, TypeScript).
    69|
    70|**Input:** none
    71|
    72|---
    73|
    74|## Configuring Registries
    75|
    76|Registries are set in `components.json`. The `@shadcn` registry is always built-in.
    77|
    78|```json
    79|{
    80|  "registries": {
    81|    "@acme": "https://acme.com/r/{name}.json",
    82|    "@private": {
    83|      "url": "https://private.com/r/{name}.json",
    84|      "headers": { "Authorization": "Bearer ${MY_TOKEN}" }
    85|    }
    86|  }
    87|}
    88|```
    89|
    90|- Names must start with `@`.
    91|- URLs must contain `{name}`.
    92|- `${VAR}` references are resolved from environment variables.
    93|
    94|Community registry index: `https://ui.shadcn.com/r/registries.json`
    95|