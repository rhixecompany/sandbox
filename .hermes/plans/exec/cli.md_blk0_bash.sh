#!/bin/bash
# Auto-extracted from: cli.md
# Source block language: bash
# Start an interactive session (default)
hermes

# Single query mode (non-interactive)
hermes chat -q "Hello"

# Single query from a file or stdin — nothing is shell-interpreted, so
# arbitrary text (quotes, $(...), backticks) arrives verbatim
hermes chat --query-file prompt.txt
hermes chat --query-file - < prompt.txt

# With a specific model
hermes chat --model "anthropic/claude-sonnet-4"

# With a specific provider
hermes chat --provider nous        # Use Nous Portal
hermes chat --provider openrouter  # Force OpenRouter

# With specific toolsets
hermes chat --toolsets "web,terminal,skills"

# Start with one or more skills preloaded
hermes -s hermes-agent-dev,github-auth
hermes chat -s github-pr-workflow -q "open a draft PR"

# Resume previous sessions
hermes --continue             # Resume the most recent CLI session (-c)
hermes --resume <session_id>  # Resume a specific session by ID (-r)
hermes --resume latest        # Resume the most recent session (same as -c)
hermes --resume latest --in ./dir  # Resume ./dir's latest session, staying in ./dir

# Verbose mode (debug output)
hermes chat --verbose

# Isolated git worktree (for running multiple agents in parallel)
hermes -w                         # Interactive mode in worktree
hermes -w -z "Fix issue #123"     # Single query in worktree
