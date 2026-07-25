---
name: using-superpowers-codex-tools
description: "Codex Tool Mapping"
version: 1.0.0
author: Alexa
---
     1|# Codex Tool Mapping
     2|
     3|Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:
     4|
     5|| Skill references | Codex equivalent |
     6|| --- | --- |
     7|| `Task` tool (dispatch subagent) | `spawn_agent` (see [Subagent dispatch requires multi-agent support](#subagent-dispatch-requires-multi-agent-support)) |
     8|| Multiple `Task` calls (parallel) | Multiple `spawn_agent` calls |
     9|| Task returns result | `wait_agent` |
    10|| Task completes automatically | `close_agent` to free slot |
    11|| `TodoWrite` (task tracking) | `update_plan` |
    12|| `Skill` tool (invoke a skill) | Skills load natively — just follow the instructions |
    13|| `Read`, `Write`, `Edit` (files) | Use your native file tools |
    14|| `Bash` (run commands) | Use your native shell tools |
    15|
    16|## Subagent dispatch requires multi-agent support
    17|
    18|Add to your Codex config (`~/.codex/config.toml`):
    19|
    20|```toml
    21|[features]
    22|multi_agent = true
    23|```
    24|
    25|This enables `spawn_agent`, `wait_agent`, and `close_agent` for skills like `dispatching-parallel-agents` and `subagent-driven-development`.
    26|
    27|Legacy note: Codex builds before `rust-v0.115.0` exposed spawned-agent waiting as `wait`. Current Codex uses `wait_agent` for spawned agents. The `wait` name now belongs to code-mode `exec/wait`, which resumes a yielded exec cell by `cell_id`; it is not the spawned-agent result tool.
    28|
    29|## Environment Detection
    30|
    31|Skills that create worktrees or finish branches should detect their environment with read-only git commands before proceeding:
    32|
    33|```bash
    34|GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
    35|GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
    36|BRANCH=$(git branch --show-current)
    37|```
    38|
    39|- `GIT_DIR != GIT_COMMON` → already in a linked worktree (skip creation)
    40|- `BRANCH` empty → detached HEAD (cannot branch/push/PR from sandbox)
    41|
    42|See `using-git-worktrees` Step 0 and `finishing-a-development-branch` Step 1 for how each skill uses these signals.
    43|
    44|## Codex App Finishing
    45|
    46|When the sandbox blocks branch/push operations (detached HEAD in an externally managed worktree), the agent commits all work and informs the user to use the App's native controls:
    47|
    48|- **"Create branch"** — names the branch, then commit/push/PR via App UI
    49|- **"Hand off to local"** — transfers work to the user's local checkout
    50|
    51|The agent can still run tests, stage files, and output suggested branch names, commit messages, and PR descriptions for the user to copy.
    52|