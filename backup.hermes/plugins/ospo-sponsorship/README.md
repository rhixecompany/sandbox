# Open Source Sponsorship Plugin

Tools and resources for Open Source Program Offices (OSPOs) to identify, evaluate, and manage sponsorship of open source dependencies through GitHub Sponsors, Open Collective, and other funding platforms.

## Installation

```bash
# Using Copilot CLI
copilot plugin install ospo-sponsorship@awesome-copilot
```

## What's Included

### Skills

| Skill | Description |
| --- | --- |
| `SKILL.md` | Find which of a GitHub repository's dependencies are sponsorable via GitHub Sponsors. Uses deps.dev API for dependency resolution across npm, PyPI, Cargo, Go, RubyGems, Maven, and NuGet. Checks npm funding metadata, FUNDING.yml files, and web search. Verifies every link. Shows direct and transitive dependencies with OSSF Scorecard health data. Invoke by providing a GitHub owner/repo (e.g. "find sponsorable dependencies in expressjs/express"). |


## Hermes Usage

Open Source Program Office sponsorship tools. Find sponsorable dependencies.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
