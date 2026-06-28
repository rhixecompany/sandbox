---
author: Alexa
description: 'Use when controlling Visual Studio Code from the `code` command: launching
  windows, editing files, managing extensions, MCP servers, profiles, chat/agent/tunnel
  subcommands, and troubleshooting.'
license: MIT
name: vscode-cli
tags:
- imported
title: Visual Studio Code CLI
version: 1.0.0

---
# Visual Studio Code CLI

## Purpose

Use this skill when the user asks about Visual Studio Code itself, the `code` CLI, `code-insiders`, extensions, MCP server configuration, or CLI subcommands.

## Operating rule

Treat `code --help` and `code <subcommand> --help` as the source of truth. VS Code CLI behavior changes by version; verify before assuming a flag exists.

## When to use

- Launching VS Code from the terminal
- Opening files, folders, workspaces, or URLs
- Diffing or merging files from the CLI
- Managing extensions from the CLI
- Configuring or adding MCP servers
- Using CLI subcommands like `chat`, `agent`, `serve-web`, or `tunnel`
- Troubleshooting startup, extension, or profile issues

## Workflow

### 1) Inspect the current surface

Run:

```bash
code --help
code <subcommand> --help
code --version
```

Use the installed version's output, not stale memory.

### 2) Classify the task

Choose the smallest command surface that solves it:

- launch/editing
- extension management
- MCP configuration
- subcommand workflow
- troubleshooting/diagnostics

### 3) Execute with safe defaults

Prefer explicit paths, profiles, and isolated configs when behavior matters.

### 4) Verify

Confirm with one of:

- `code --status`
- `code --list-extensions`
- `code --version`
- the relevant subcommand output
- file or config inspection after a change

## Command groups

### Launching and file operations

Current CLI options commonly include:

- `code <paths...>` open files/folders/projects
- `-` read from stdin
- `-g, --goto <file:line[:character]>` open at a location
- `-d, --diff <file> <file>` compare two files
- `-m, --merge <path1> <path2> <base> <result>` three-way merge
- `-n, --new-window` open a new window
- `-r, --reuse-window` reuse the last active window
- `-a, --add <folder>` add folder(s) to the active window
- `--remove <folder>` remove folder(s) from the active window
- `-w, --wait` wait for file closure before returning
- `--locale <locale>` set UI language for the session
- `--profile <profileName>` open with a profile
- `--user-data-dir <dir>` isolate user data
- `--agents` open the agents window

Typical patterns:

```bash
code .
code -n path/to/workspace
code -g src/app.ts:42
code -d before.txt after.txt
code --profile "Web Development" .
```

### Extension management

Use the extension flags when you need reproducible setup or cleanup.

Common flags:

- `--extensions-dir <dir>` set the extension root
- `--list-extensions` list installed extensions
- `--show-versions` show versions with `--list-extensions`
- `--category <category>` filter listed extensions
- `--install-extension <ext-id | path>` install or update an extension
- `--pre-release` install pre-release when installing
- `--uninstall-extension <ext-id>` remove an extension
- `--update-extensions` update installed extensions
- `--enable-proposed-api <ext-id>` enable proposed APIs for an extension
- `--disable-extensions` disable all installed extensions for a new window
- `--disable-extension <ext-id>` disable one extension for a new window

Rules:

- Extension IDs are `publisher.name`
- Use `@version` to pin a version
- Use `--force` when updating deliberately
- Prefer a profile or isolated `--extensions-dir` when testing

Examples:

```bash
code --list-extensions --show-versions
code --install-extension ms-python.python
code --install-extension vscode.csharp@1.2.3 --force
code --uninstall-extension ms-python.python
```

### Model Context Protocol (MCP)

Use MCP when VS Code must talk to external tools or services.

Current CLI support includes:

- `--add-mcp <json>` add an MCP server to the user profile

Operational rules:

- Prefer workspace-scoped `mcp.json` when the server belongs to a repo
- Prefer user-profile MCP config when the server should be available everywhere
- Do not hardcode secrets in `mcp.json`
- Use input variables or env files for tokens
- Treat local stdio servers as executable code; trust only known sources

Configuration locations:

- Workspace: `.vscode/mcp.json`
- User profile: the profile-level `mcp.json`

Examples:

```bash
code --add-mcp '{"name":"playwright","command":"npx","args":["-y","@microsoft/mcp-server-playwright"]}'
```

### Subcommands

The installed CLI commonly exposes these subcommands:

- `chat` — run a chat session in the current working directory
- `serve-web` — serve the editor UI in a browser
- `agent` — start and interact with AI agent hosts
- `tunnel` — expose the machine through a secure tunnel

For each one, run `code <subcommand> --help` before relying on flags.

Examples:

```bash
code chat --help
code agent --help
code serve-web --help
code tunnel --help
```

### Troubleshooting

Use these when the CLI or editor misbehaves:

- `-h, --help` print usage
- `-v, --version` print version
- `-s, --status` print process usage and diagnostics
- `--verbose` increase output and imply wait
- `--log <level>` set log verbosity
- `--prof-startup` profile startup performance
- `--inspect-extensions <port>` debug extensions
- `--inspect-brk-extensions <port>` pause extension host at startup
- `--disable-extensions` isolate startup without extensions
- `--disable-extension <ext-id>` isolate one extension
- `--sync <on | off>` control sync
- `--transient` run with temporary data and extension directories
- `--telemetry` show collected telemetry events

Windows and sandbox notes:

- `code` must be on `PATH` or called by full path
- `--disable-chromium-sandbox` is a last resort, not a default
- `--locate-shell-integration-path <shell>` helps debug shell integration

## Pitfalls

- Do not assume old CLI flags still exist.
- Do not hardcode MCP secrets in source-controlled config.
- Do not use detached mode for stdio MCP servers.
- Do not rely on disabled extensions staying disabled across all window types unless the CLI option is documented for that version.
- Do not mix user-profile and workspace extension state when debugging reproducibility.

## Verification checklist

- [ ] `code --help` matches the installed version
- [ ] The correct subcommand help was checked
- [ ] The command used the right profile or user-data directory
- [ ] Extension or MCP changes were verified after execution
- [ ] No secrets were written into config files
