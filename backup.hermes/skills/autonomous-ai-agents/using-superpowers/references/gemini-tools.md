---
name: using-superpowers-gemini-tools
description: "Gemini CLI Tool Mapping"
version: 1.0.0
author: Alexa
---
     1|# Gemini CLI Tool Mapping
     2|
     3|Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:
     4|
     5|| Skill references | Gemini CLI equivalent |
     6|| --- | --- |
     7|| `Read` (file reading) | `read_file` |
     8|| `Write` (file creation) | `write_file` |
     9|| `Edit` (file editing) | `replace` |
    10|| `Bash` (run commands) | `run_shell_command` |
    11|| `Grep` (search file content) | `grep_search` |
    12|| `Glob` (search files by name) | `glob` |
    13|| `TodoWrite` (task tracking) | `write_todos` |
    14|| `Skill` tool (invoke a skill) | `activate_skill` |
    15|| `WebSearch` | `google_web_search` |
    16|| `WebFetch` | `web_fetch` |
    17|| `Task` tool (dispatch subagent) | `@agent-name` (see [Subagent support](#subagent-support)) |
    18|
    19|## Subagent support
    20|
    21|Gemini CLI supports subagents natively via the `@` syntax. Use the built-in `@generalist` agent to dispatch any task — it has access to all tools and follows the prompt you provide.
    22|
    23|When a skill says to dispatch a named agent type, use `@generalist` with the full prompt from the skill's prompt template:
    24|
    25|| Skill instruction | Gemini CLI equivalent |
    26|| --- | --- |
    27|| `Task tool (superpowers:implementer)` | `@generalist` with the filled `implementer-prompt.md` template |
    28|| `Task tool (superpowers:spec-reviewer)` | `@generalist` with the filled `spec-reviewer-prompt.md` template |
    29|| `Task tool (superpowers:code-reviewer)` | `@code-reviewer` (bundled agent) or `@generalist` with the filled review prompt |
    30|| `Task tool (superpowers:code-quality-reviewer)` | `@generalist` with the filled `code-quality-reviewer-prompt.md` template |
    31|| `Task tool (general-purpose)` with inline prompt | `@generalist` with your inline prompt |
    32|
    33|### Prompt filling
    34|
    35|Skills provide prompt templates with placeholders like `{WHAT_WAS_IMPLEMENTED}` or `[FULL TEXT of task]`. Fill all placeholders and pass the complete prompt as the message to `@generalist`. The prompt template itself contains the agent's role, review criteria, and expected output format — `@generalist` will follow it.
    36|
    37|### Parallel dispatch
    38|
    39|Gemini CLI supports parallel subagent dispatch. When a skill asks you to dispatch multiple independent subagent tasks in parallel, request all of those `@generalist` or named subagent tasks together in the same prompt. Keep dependent tasks sequential, but do not serialize independent subagent tasks just to preserve a simpler history.
    40|
    41|## Additional Gemini CLI tools
    42|
    43|These tools are available in Gemini CLI but have no Claude Code equivalent:
    44|
    45|| Tool | Purpose |
    46|| --- | --- |
    47|| `list_directory` | List files and subdirectories |
    48|| `save_memory` | Persist facts to GEMINI.md across sessions |
    49|| `ask_user` | Request structured input from the user |
    50|| `tracker_create_task` | Rich task management (create, update, list, visualize) |
    51|| `enter_plan_mode` / `exit_plan_mode` | Switch to read-only research mode before making changes |
    52|