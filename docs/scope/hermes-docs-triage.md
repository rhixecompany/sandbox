# Triage report for hermes docs, instructions, and agent files

This is a recommendation, not an order. You may run the steps below or skip any that do not fit your current session.

## What this report covers

This document lists files found under three areas: the docs folder at docs/hermes, the instructions folder at instructions, and the agent folder at .github/agents. It then points out personality and instructions files that the hermes config should reference. Finally it suggests a profile update plan.

## Reference list of searched paths

- docs/hermes/*.md, *.mdx, *.json (462 files found)
- instructions/**/*.instructions.md (44 files found)
- .github/agents/*.agent.md (30 files found)

## File groups with one line summaries

### docs/hermes group (462 items)

This folder holds documentation for the hermes agent platform. It splits into subfolders like developer guide, getting started, guides, integrations, user guide, reference, and user stories. Most files explain how a feature works or how to configure it.

Key examples:

```
file: docs/hermes/index.mdx
summary: Main landing page for hermes agent documentation.
```

```
file: docs/hermes/user-guide/profiles.md
summary: How to manage agent profiles.
```

```
file: docs/hermes/user-guide/features/skills.md
summary: Overview of the skills system.
```

```
file: docs/hermes/developer-guide/architecture.md
summary: System architecture for contributors.
```

```
file: docs/hermes/reference/cli-commands.md
summary: Command line reference.
```

```
file: docs/hermes/getting-started/quickstart.md
summary: First steps to get running.
```

The group is mostly healthy. No broken links or missing core files were noticed. Some subfolders contain large file counts, which makes scanning slower. You could split them into smaller epics if needed.

### instructions group (44 items)

These files live under .codex/instructions, .config/opencode/instructions, and the prompt templates folder. They describe domain rules, framework rules, and meta rules. They guide how the agent responds to certain contexts.

Key examples:

```
file: .codex/instructions/domains/code-review.instructions.md
summary: Rules for reviewing code with the agent.
```

```
file: .codex/instructions/meta/prompt.instructions.md
summary: How to build effective prompts.
```

```
file: .config/opencode/instructions/domains/security-and-owasp.instructions.md
summary: Security practices for code generation.
```

These are valuable as personality and instruction sources. They should be linked in the hermes config.

### agent group (30 items)

These agent definitions live in .github/agents. Each describes a specialized agent role. They cover architecture decisions, governance, quality assurance, feature planning, and framework expertise.

Key examples:

```
file: .github/agents/adr-generator.agent.md
summary: Creates architecture decision records.
```

```
file: .github/agents/agent-governance-reviewer.agent.md
summary: Reviews governance practices.
```

```
file: .github/agents/implementation-plan.agent.md
summary: Builds implementation plans.
```

```
file: .github/agents/python-mcp-expert.agent.md
summary: Expert on python model context protocol.
```

These agent files are excellent candidates for profile personalities. Each agent describes a role that could become a profile.

## Personality and instructions sources found

The following sources contain personality or instruction content that should feed into the hermes config:

- .copilot/templates/personality.md
- .codex/templates/personality.md
- .config/opencode/templates/personality.md
- .github/agents/*.agent.md (30 agent files)
- .codex/instructions/*.instructions.md (multiple domains and meta files)
- prompts/templates/*/instructions.md (platform specific instructions)

You should treat each agent file as a distinct personality. The instruction files provide behavioral rules that the agent should apply when routed to the matching profile.

## Config update recommendation

The hermes config file is at $HERMES_HOME/config.yaml. It currently has a personalities section with only the default identity. You should expand it with entries that reference each found personality file.

A recommended approach: for each agent file and each personality template file, add a named personality entry. The entry should point to the file path. The instruction files can be referenced as behavior rules within the profile settings.

Since the user asked to update the config with all found personality and instructions files, you may add them as references rather than duplicating their contents. This keeps the config clean and avoids duplication.

## Profile creation recommendation

Profiles currently exist at $HERMES_HOME/profiles/. The default profile is present. You may skip it. For each agent file that defines a unique role, you should create or recreate a profile with a matching name. The profile should reference the agent file as its personality source.

The profile creation can be done via the hermes CLI or by copying profile templates and editing the identity file. You should verify the profile exists and points to the correct agent file after creation.

## Next steps you may take

1. Read the full agent files in .github/agents to decide which ones need profiles.
2. Update $HERMES_HOME/config.yaml with personality references.
3. Create profiles for the non-default roles.
4. Verify each profile loads correctly.
5. Optionally split large docs/hermes subfolders into smaller sections for faster scanning.

This report is a recommendation. You decide which steps to run and in what order.
