# TypeSpec for Microsoft 365 Copilot Plugin

Comprehensive collection of prompts, instructions, and resources for building declarative agents and API plugins using TypeSpec for Microsoft 365 Copilot extensibility.

## Installation

```bash
# Using Copilot CLI
copilot plugin install typespec-m365-copilot@awesome-copilot
```

## What's Included

### Commands (Slash Commands)

| Command | Description |
| --- | --- |
| `/typespec-m365-copilot:typespec-create-agent` | Generate a complete TypeSpec declarative agent with instructions, capabilities, and conversation starters for Microsoft 365 Copilot |
| `/typespec-m365-copilot:typespec-create-api-plugin` | Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot |
| `/typespec-m365-copilot:typespec-api-operations` | Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards |


## Hermes Usage

TypeSpec for Microsoft 365 Copilot. Declarative agents and API plugins.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
