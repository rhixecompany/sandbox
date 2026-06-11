# Windows interactive-add behavior

## Observation
- On Windows, `hermes mcp add ...` often prompts interactively: “Does this server require authentication? [Y/n]”.
- In non-interactive sessions (background terminal, tool-driven CI, subagents, `execute_code` wrappers), this blocks until timeout.
- Supplying `--url`, `--command`, and `--args` together does not bypass the prompt in current builds.

## Lesson
- Treat `hermes mcp add` on Windows as **interactive-by-default**.
- In automated flows, prefer **editing `config.yaml`** (`mcp_servers:`) and then reloading.
- If you must use `add`, run it in an interactive shell and wait for the prompt response.

## Workaround checklist
1. Check current servers first: `hermes mcp catalog`.
2. If `add` blocks: stop the loop instead of retrying the same call.
3. Switch to manual config YAML edit for fleet/batch setup.
4. For single dev machines, use `hermes mcp add` in an interactive terminal.
5. After YAML edits, reload: `/reload-mcp` then `hermes mcp test <name>`.
