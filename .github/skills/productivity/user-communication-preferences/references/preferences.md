Action checklist for Alexa-style sessions

1. Start with a single-line action summary.
2. Display commands / code snippets first, then short explanation.
3. Before any destructive command: show the exact command, list risks, and require explicit confirmation unless an explicit `--yolo` equivalent is present.
4. When claiming a file was read/modified, include the tool output lines (read_file or terminal output) in the same reply.
5. Use git for rollback. Do NOT create .bak/.old files.
6. When user mentions model switch, immediately reflect it in self-ID lines.

Templates

- Model self-identification:
  Active model: {model} ({provider}). Knowledge cutoff: {cutoff}. Session: {session_id}

- Destructive-operation prompt:
  Command: {cmd}
  Risks: {risks}
  Do you want to proceed? (yes/no)

- Commit message template:
  {type}: {short description}

Edge cases

- If a tool reports an auth fallback, capture that in the reply and continue with fallback details. Do not treat fallback as success without verifying provider identity and session_id.
- When user says "ensure nothing is truncated", "write full content", or similar — use `web_extract` (not browser) for full pages; if browser is needed, extract `document.querySelector('article').innerText` and write complete output.
- When user says "execute all X phases", "don't stop until verified", "verify all phases" — run the full workflow to completion with verification gates; do not pause for confirmation between phases.
- When user provides a prompt file (e.g., sample.prompt.md) with explicit phases — follow the phase sequence strictly; produce per-phase artifacts and a final summary.
- If a Hermes CLI command times out (e.g., `hermes profile create --clone-all`), document the timeout as a blocker, run the non-clone variant, and note the workaround (manual config/hook/plugin copy).

Knowledge from this session (2026-06-13)

- `hermes profile create <name> --clone-all` times out (60s) — only bundled skills (73) sync. Hooks/plugins/MCP/config/.env require manual propagation or CLI fix.
- 6-phase sample.prompt.md execution pattern: Phase 1 skills audit → Phase 2 MCP research → Phase 3 docs extraction (12 URLs via web_extract) → Phase 4 profiles (7 created) → Phase 5 inventory → Phase 6 config hierarchy audit.
- web_extract preserves full content for Hermes docs pages; prefer over browser for bulk extraction.
- Profile role matrix used: default (primary), adminbot (devops), code-architect (implementation), research-analyst (research), creative-director (creative), exec-assistant (admin), patient-tutor (teaching).
