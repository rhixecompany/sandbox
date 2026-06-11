# Context Engineering Plugin

Tools and techniques for maximizing GitHub Copilot effectiveness through better context management. Includes guidelines for structuring code, an agent for planning multi-file changes, and prompts for context-aware development.

## Installation

```bash
# Using Copilot CLI
copilot plugin install context-engineering@awesome-copilot
```

## What's Included

### Commands (Slash Commands)

| Command | Description |
| --- | --- |
| `/context-engineering:context-map` | Generate a map of all files relevant to a task before making changes |
| `/context-engineering:what-context-needed` | Ask Copilot what files it needs to see before answering a question |
| `/context-engineering:refactor-plan` | Plan a multi-file refactor with proper sequencing and rollback steps |

### Agents

| Agent | Description |
| --- | --- |
| `context-architect` | An agent that helps plan and execute multi-file changes by identifying relevant context and dependencies |


## Hermes Usage

Context management patterns for Copilot. The `context-map` command is useful for planning multi-file changes.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
