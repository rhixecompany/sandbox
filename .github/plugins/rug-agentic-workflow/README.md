# RUG Agentic Workflow Plugin

Three-agent workflow for orchestrated software delivery with an orchestrator plus implementation and QA subagents.

## Installation

```bash
# Using Copilot CLI
copilot plugin install rug-agentic-workflow@awesome-copilot
```

## What's Included

### Agents

| Agent | Description |
| --- | --- |
| `rug-orchestrator` | Pure orchestration agent that decomposes requests, delegates all work to subagents, validates outcomes, and repeats until complete. |
| `swe-subagent` | Senior software engineer subagent for implementation tasks: feature development, debugging, refactoring, and testing. |
| `qa-subagent` | Meticulous QA subagent for test planning, bug hunting, edge-case analysis, and implementation verification. |


## Hermes Usage

Three-agent workflow: orchestrator + implementation + QA subagents.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
