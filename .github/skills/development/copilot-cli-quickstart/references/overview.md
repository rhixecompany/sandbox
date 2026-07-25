# GitHub Copilot CLI — Reference Overview

## Key Concepts

- **GitHub Copilot CLI** is a terminal-based AI assistant that provides an interactive chat experience right in the command line. It can read code, edit files, run commands, and create pull requests — all inside a conversational interface accessed via `gh copilot` or the standalone `copilot` command.
- **Modes** — Copilot CLI has three interaction modes: **Interactive** (default, asks before acting), **Plan** (creates structured implementation plans), and **Shell** (quick shell commands via the `!` prefix). Press `Shift+Tab` to cycle between modes.
- **Slash Commands** — Type `/` to access power tools: `/help` (all commands), `/clear` (reset conversation), `/plan` (create implementation plan), `/diff` (view changes), `/compact` (compress context), `/model` (switch AI models), `/mcp` (manage MCP servers), and `/skills` (manage skills).
- **Permissions Model** — Copilot always asks before creating files, running commands, or making changes. Users choose Allow (one-time), Deny (don't do it), or Allow for Session (don't ask again for this type of action during this session).
- **File Mentions** — Use `@` followed by a filename to put a file in context. Copilot reads and references the file when responding. This works for code analysis, comparisons, and focused editing.
- **Instruction Files** — Customize Copilot behavior with markdown instruction files at `.github/copilot-instructions.md` (repo-wide) or `.github/instructions/*.instructions.md` (path-specific), or `~/.copilot/copilot-instructions.md` (global). Use the `/init` command to scaffold these files.