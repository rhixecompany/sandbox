# Output Format

> Extracted from `suggest-awesome-github-copilot-agents.prompt.md`.

## Output Format

Display analysis results in structured table comparing awesome-copilot custom agents with existing repository custom agents:

| Awesome-Copilot Custom Agent | Description | Already Installed | Similar Local Custom Agent | Suggestion Rationale |
| --- | --- | --- | --- | --- |
| [amplitude-experiment-implementation.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/amplitude-experiment-implementation.agent.md) | This custom agent uses Amplitude's MCP tools to deploy new experiments inside of Amplitude, enabling seamless variant testing capabilities and rollout of product features | ❌ No | None | Would enhance experimentation capabilities within the product |
| [launchdarkly-flag-cleanup.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/launchdarkly-flag-cleanup.agent.md) | Feature flag cleanup agent for LaunchDarkly | ✅ Yes | launchdarkly-flag-cleanup.agent.md | Already covered by existing LaunchDarkly custom agents |
| [principal-software-engineer.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/principal-software-engineer.agent.md) | Provide principal-level software engineering guidance with focus on engineering excellence, technical leadership, and pragmatic implementation. | ⚠️ Outdated | principal-software-engineer.agent.md | Tools configuration differs: remote uses `'web/fetch'` vs local `'fetch'` - Update recommended |
