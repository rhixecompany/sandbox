#!/usr/bin/env bash
# Run the agent/provider matrix against a single live cell to validate the integration.
# Uses the default profile + openai-codex provider to confirm hermes chat --query-file works.
root="$(cygpath -u "$(dirname "$0")/..")"
query="$("$root/scripts/agent_provider_matrix.py" --dry-run --limit-cells 1 --quiet >/dev/null 2>&1; find "$root/.hermes/plans/results/agent-provider-matrix" -name request.md -path '*default*' | sort -r | head -1)"
if [ -z "$query" ]; then
  echo "No rendered request.md found" >&2
  exit 2
fi
echo "Using query: $query"
hermes -p default chat --query-file "$query" --provider openai-codex --quiet --max-turns 2 --run-budget 60 2>&1 | tee "$root/.hermes/plans/results/agent-provider-matrix/live-test.out"
echo "exit=$?"
