# Clojure Interactive Programming Plugin

Tools for REPL-first Clojure workflows featuring Clojure instructions, the interactive programming chat mode and supporting guidance.

## Installation

```bash
# Using Copilot CLI
copilot plugin install clojure-interactive-programming@awesome-copilot
```

## What's Included

### Commands (Slash Commands)

| Command | Description |
| --- | --- |
| `/clojure-interactive-programming:remember-interactive-programming` | A micro-prompt that reminds the agent that it is an interactive programmer. Works great in Clojure when Copilot has access to the REPL (probably via Backseat Driver). Will work with any system that has a live REPL that the agent can use. Adapt the prompt with any specific reminders in your workflow and/or workspace. |

### Agents

| Agent | Description |
| --- | --- |
| `clojure-interactive-programming` | Expert Clojure pair programmer with REPL-first methodology, architectural oversight, and interactive problem-solving. Enforces quality standards, prevents workarounds, and develops solutions incrementally through live REPL evaluation before file modifications. |


## Hermes Usage

Clojure REPL-first workflow tools. Use via Copilot CLI for Clojure development.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
