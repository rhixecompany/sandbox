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
