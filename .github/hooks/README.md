# Hermes Hooks (Workspace)

Shared hooks live in `~/AppData/Local/hermes/hooks/`; the workspace copy under
`.github/hooks/` is the synced source (see `session-logger`, `session-auto-commit`,
`governance-audit`).

## Repo-init hook (optional, post-clone)

When a repo is opened for the first time, initialize it for all installed AI
agents so every agent sees its context files immediately.

**Hook type:** `on_session_start` (or wire into your clone script).

**Action:** run the repo-init scaffold if the repo has no `AGENTS.md`:

```bash
cd <repo>
if [ ! -f AGENTS.md ]; then
  MSYS_NO_PATHCONV=1 python scripts/repo-init.py --init .
fi
```

**Source of truth:** `scripts/repo-init.py` in the workspace; skill
`repo-init`; prompt `repo-init.prompt.md`. The script is idempotent — it never
overwrites existing `AGENTS.md`, `CLAUDE.md`, or `.github/agents/` content, so
it is safe to run on any repo at any time.

**Pitfall:** the script writes only 3 generic files (AGENTS.md,
docs/ai-agents-inventory.md, .github/agents/README.md). It does not create
per-profile Hermes context or copy secrets — do not add those to a hook.
