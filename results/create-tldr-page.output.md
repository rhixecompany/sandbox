# TLDR Page: `hermes`

> AI assistant with tool-calling capabilities, persistent memory, and multi-platform messaging. Some commands such as `setup`, `config`, `skills`, and `profile` have their own usage documentation. More information: <https://hermes-agent.nousresearch.com/docs>.

- Start an interactive chat session:

`hermes chat`

- Run the interactive setup wizard:

`hermes setup`

- Show current configuration:

`hermes config show`

- Set a configuration value:

`hermes config set {{config.path}} {{value}}`

- List installed skills:

`hermes skills list`

- Install a skill:

`hermes skills install {{skill-name}}`

- Switch to a different profile:

`hermes profile use {{profile-name}}`

- List all profiles:

`hermes profile list`

- Add an MCP server:

`hermes mcp add {{server-name}}`

- List configured MCP servers:

`hermes mcp list`

- Diagnose configuration and dependency issues:

`hermes doctor`

- Run a single query (non-interactive):

`hermes chat --query "{{your prompt}}"`

- Resume the most recent session:

`hermes chat --continue`

- Start the messaging gateway:

`hermes gateway`

- Check version information:

`hermes version`

- Manage cron jobs:

`hermes cron`

- List configured tools:

`hermes tools`

---

> **Source**: Hermes Agent CLI v0.18.2 — upstream `73b611ad`. Generated from `hermes --help` and subcommand `--help` output against a live Hermes Agent installation.
