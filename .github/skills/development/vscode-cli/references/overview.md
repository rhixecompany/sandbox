# VS Code CLI — Reference Overview

## Key Concepts

- **The `code` CLI** is the command-line interface for Visual Studio Code. It enables opening files, folders, and workspaces; managing extensions; configuring MCP servers; running diagnostics; and using subcommands like `chat`, `agent`, `serve-web`, and `tunnel` — all from the terminal.
- **CLI Version Sensitivity** — VS Code CLI flags and behavior change by version. Always run `code --help` and `code <subcommand> --help` to verify available options before scripting. Never assume a flag exists across versions.
- **Extension Management from CLI** — Extensions can be installed (`--install-extension`), uninstalled (`--uninstall-extension`), listed (`--list-extensions`), and updated (`--update-extensions`) entirely from the terminal. Extension IDs follow the `publisher.name` convention.
- **MCP Server Configuration** — The `--add-mcp` flag adds Model Context Protocol servers to the user profile. For repository-scoped MCP servers, use `.vscode/mcp.json` at the workspace root. Never hardcode secrets in source-controlled config files.
- **Profiles and Isolation** — Use `--profile <name>` for environment-specific configurations, `--user-data-dir <dir>` for full isolation (useful for testing), and `--disable-extensions` for troubleshooting startup issues.
- **Windows Considerations** — On Windows, `code` is a shell script wrapper, not a native executable. Running it from Python `subprocess.run()` may fail; use the terminal tool instead. The `--disable-chromium-sandbox` flag is a last resort for sandbox issues.