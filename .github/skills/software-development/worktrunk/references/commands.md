---
name: worktrunk-commands
description: "Worktrunk Commands Reference"
version: 1.0.0
author: Alexa
---
     1|# Worktrunk Commands Reference
     2|
     3|## wt switch
     4|
     5|Switch to or create a worktree.
     6|
     7|```bash
     8|wt switch <branch>                    # Switch to existing worktree
     9|wt switch --create <branch>           # Create branch + worktree, then switch
    10|wt switch -c -x claude <branch>       # Create + launch Claude
    11|wt switch -c -x claude <branch> -- '<prompt>'  # With initial prompt
    12|wt switch -                           # Previous worktree
    13|wt switch @                           # Current worktree (no-op, useful with --execute)
    14|```
    15|
    16|### Key flags
    17|
    18|| Flag | Short | Description |
    19|| --- | --- | --- |
    20|| `--create` | `-c` | Create new branch and worktree |
    21|| `--execute <cmd>` | `-x` | Run command after switching (after post-create hooks) |
    22|| `--base <branch>` |  | Base branch for creation (default: default branch) |
    23|| `--base=@` |  | Base from current HEAD (stacked branches) |
    24|| `--no-verify` |  | Skip hooks |
    25|| `--yes` |  | Skip approval prompts |
    26|
    27|### Interactive Picker
    28|
    29|`wt switch` with no arguments opens an interactive picker with:
    30|
    31|- Tab 1: Worktrees (live diff preview)
    32|- Tab 2: All branches (log preview)
    33|- Tab 3: Remote branches
    34|- Tab 4: PRs (if gh/glab configured)
    35|- Tab 5: LLM branch summaries (if configured)
    36|
    37|### Shortcuts
    38|
    39|```bash
    40|wt switch - prefix-*         # Fuzzy match on branch prefix
    41|wt switch --create hotfix --base=@   # Branch from current HEAD
    42|```
    43|
    44|## wt list
    45|
    46|Show all worktrees with rich status.
    47|
    48|```bash
    49|wt list                    # All worktrees
    50|wt list --full             # Add CI status, PR links, LLM summaries
    51|wt list --branches         # Include remote branches without worktrees
    52|wt list --format=json      # JSON output
    53|wt list statusline --format=claude-code  # Single-line for Claude Code statusline
    54|```
    55|
    56|### Status Column Indicators
    57|
    58|| Symbol    | Meaning                           |
    59|| --------- | --------------------------------- |
    60|| `@`       | Current worktree                  |
    61|| `+` / `-` | Staged / unstaged changes         |
    62|| `?`       | Untracked files                   |
    63|| `↑` / `↓` | Ahead / behind remote             |
    64|| `⇡` / `⇣` | Ahead / behind default branch     |
    65|| `^`       | Up to date with remote            |
    66|| `🤖`      | Claude working (plugin)           |
    67|| `💬`      | Claude waiting for input (plugin) |
    68|
    69|### Custom URL Column
    70|
    71|```toml
    72|# .config/wt.toml
    73|[list]
    74|url = "http://localhost:{{ branch | hash_port }}"
    75|```
    76|
    77|## wt merge
    78|
    79|Squash, rebase, merge, and clean up in one command.
    80|
    81|```bash
    82|wt merge main              # Merge current branch into main
    83|wt merge staging           # Merge into staging
    84|```
    85|
    86|### Pipeline
    87|
    88|1. Run `pre-commit` hooks (optional lint/format)
    89|2. Stage any remaining changes + generate LLM commit message
    90|3. Squash all commits if needed
    91|4. Rebase onto target branch
    92|5. Run `pre-merge` hooks (tests, builds)
    93|6. Fast-forward merge to target
    94|7. Remove worktree + branch (`pre-remove` / `post-remove` hooks)
    95|8. Run `post-merge` hooks in target worktree
    96|
    97|### Flags
    98|
    99|| Flag          | Description             |
   100|| ------------- | ----------------------- |
   101|| `--no-squash` | Keep individual commits |
   102|| `--no-rebase` | Skip rebase step        |
   103|| `--no-verify` | Skip all hooks          |
   104|| `--yes`       | Skip prompts            |
   105|
   106|## wt remove
   107|
   108|Remove worktree and branch.
   109|
   110|```bash
   111|wt remove                  # Remove current worktree
   112|wt remove <branch>         # Remove specific worktree
   113|wt remove @                # Remove current (same as no args)
   114|wt remove --all            # Remove all non-default worktrees
   115|```
   116|
   117|Runs `pre-remove` (blocking) and `post-remove` (background) hooks.
   118|
   119|## wt step
   120|
   121|Utility commands for worktree workflows.
   122|
   123|```bash
   124|wt step commit             # Commit staged changes (with optional LLM message)
   125|wt step commit --all       # Stage all + commit
   126|wt step copy-ignored       # Copy gitignored files from nearest worktree (deps, caches, .env)
   127|```
   128|
   129|### copy-ignored
   130|
   131|Copies gitignored files between worktrees to eliminate cold starts.
   132|
   133|Control scope with `.worktreeinclude`:
   134|
   135|```
   136|# Only copy files matching these patterns (must also be gitignored)
   137|node_modules/
   138|.env.local
   139|target/
   140|.venv/
   141|```
   142|
   143|Without `.worktreeinclude`, all gitignored files are copied.
   144|
   145|## wt config
   146|
   147|Manage configuration and state.
   148|
   149|```bash
   150|# Shell integration
   151|wt config shell install    # Install shell function (enables directory changes)
   152|
   153|# State inspection
   154|wt config state default-branch              # Show detected default branch
   155|wt config state logs get                    # List all hook log files
   156|wt config state logs get --hook=project:post-start:server  # Specific log
   157|wt config state marker set "🚧"            # Set status marker for current branch
   158|wt config state marker set "✅" --branch feat  # Set for specific branch
   159|
   160|# Hook approvals
   161|wt config state approvals  # Alias for wt hook approvals
   162|```
   163|
   164|### Config File Locations
   165|
   166|| File                              | Scope                       |
   167|| --------------------------------- | --------------------------- |
   168|| `~/.config/worktrunk/config.toml` | User/global                 |
   169|| `.config/wt.toml`                 | Project (checked into repo) |
   170|
   171|### Global Config Options
   172|
   173|```toml
   174|# ~/.config/worktrunk/config.toml
   175|
   176|# Worktree path template (default: sibling directory)
   177|worktree-path = "../{{ repo }}.{{ branch | sanitize }}"
   178|
   179|# Bare repo layout (worktrees as subdirectories)
   180|# worktree-path = "../{{ branch | sanitize }}"
   181|
   182|[commit.generation]
   183|provider = "anthropic"
   184|model = "claude-opus-4-5"
   185|
   186|[list]
   187|summary = true   # LLM branch summaries (sends diffs to LLM)
   188|```
   189|
   190|### Setting Overrides (per-repo user hooks)
   191|
   192|```toml
   193|# ~/.config/worktrunk/config.toml
   194|[settings_overrides.myrepo]
   195|[settings_overrides.myrepo.post-create]
   196|special = "echo 'myrepo-specific setup'"
   197|```
   198|
   199|## wt hook
   200|
   201|Run hooks manually. See `references/hooks.md` for full documentation.
   202|
   203|```bash
   204|wt hook <type>                    # Run all hooks of that type
   205|wt hook <type> <name>             # Run specific hook
   206|wt hook <type> user:              # Only user hooks
   207|wt hook <type> project:<name>     # Specific project hook
   208|wt hook <type> --var branch=feat  # Override template variable
   209|wt hook approvals add             # Pre-approve all project hooks
   210|wt hook approvals clear           # Reset approvals
   211|```
   212|
   213|## Global Flags (all commands)
   214|
   215|| Flag              | Description               |
   216|| ----------------- | ------------------------- |
   217|| `-C <path>`       | Set working directory     |
   218|| `--config <path>` | Use alternate config file |
   219|| `-v` / `-vv`      | Verbose / debug output    |
   220|| `-h` / `--help`   | Help                      |
   221|
   222|## Useful Aliases
   223|
   224|```bash
   225|# ~/.config/fish/config.fish (or .bashrc/.zshrc)
   226|alias wsc='wt switch --create --execute=claude'
   227|alias wtlog='f() { tail -f "$(wt config state logs get --hook="$1")"; }; f'
   228|
   229|# Usage
   230|wsc feature-auth                           # Create worktree + launch Claude
   231|wsc feature-auth -- 'Implement OAuth2'     # With prompt
   232|wtlog project:post-start:server            # Follow dev server log
   233|```
   234|
   235|## Bare Repository Layout
   236|
   237|Alternative layout with worktrees as subdirectories:
   238|
   239|```bash
   240|git clone --bare <url> myproject/.git
   241|cd myproject
   242|```
   243|
   244|```toml
   245|# ~/.config/worktrunk/config.toml
   246|worktree-path = "../{{ branch | sanitize }}"
   247|```
   248|
   249|```bash
   250|wt switch --create main   # Creates myproject/main/
   251|wt switch --create feat   # Creates myproject/feat/
   252|```
   253|