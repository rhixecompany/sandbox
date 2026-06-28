---
name: using-superpowers-copilot-tools
description: "Copilot CLI Tool Mapping"
version: 1.0.0
author: Alexa
---
     1|# Copilot CLI Tool Mapping
     2|
     3|Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:
     4|
     5|| Skill references | Copilot CLI equivalent |
     6|| --- | --- |
     7|| `Read` (file reading) | `view` |
     8|| `Write` (file creation) | `create` |
     9|| `Edit` (file editing) | `edit` |
    10|| `Bash` (run commands) | `bash` |
    11|| `Grep` (search file content) | `grep` |
    12|| `Glob` (search files by name) | `glob` |
    13|| `Skill` tool (invoke a skill) | `skill` |
    14|| `WebFetch` | `web_fetch` |
    15|| `Task` tool (dispatch subagent) | `task` with `agent_type: "general-purpose"` or `"explore"` |
    16|| Multiple `Task` calls (parallel) | Multiple `task` calls |
    17|| Task status/output | `read_agent`, `list_agents` |
    18|| `TodoWrite` (task tracking) | `sql` with built-in `todos` table |
    19|| `WebSearch` | No equivalent — use `web_fetch` with a search engine URL |
    20|| `EnterPlanMode` / `ExitPlanMode` | No equivalent — stay in the main session |
    21|
    22|## Async shell sessions
    23|
    24|Copilot CLI supports persistent async shell sessions, which have no direct Claude Code equivalent:
    25|
    26|| Tool | Purpose |
    27|| --- | --- |
    28|| `bash` with `async: true` | Start a long-running command in the background |
    29|| `write_bash` | Send input to a running async session |
    30|| `read_bash` | Read output from an async session |
    31|| `stop_bash` | Terminate an async session |
    32|| `list_bash` | List all active shell sessions |
    33|
    34|## Additional Copilot CLI tools
    35|
    36|| Tool | Purpose |
    37|| --- | --- |
    38|| `store_memory` | Persist facts about the codebase for future sessions |
    39|| `report_intent` | Update the UI status line with current intent |
    40|| `sql` | Query the session's SQLite database (todos, metadata) |
    41|| `fetch_copilot_cli_documentation` | Look up Copilot CLI documentation |
    42|| GitHub MCP tools (`github-mcp-server-*`) | Native GitHub API access (issues, PRs, code search) |
    43|