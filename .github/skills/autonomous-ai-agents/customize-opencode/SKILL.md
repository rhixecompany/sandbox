---
author: Hermes Agent
description: Use when editing opencode.json/opencode.jsonc, creating or fixing OpenCode
  agents, configuring plugins, setting up MCP servers, or customizing OpenCode behavior.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: customize-opencode
tags:
- opencode
- configuration
- agents
- plugins
- mcp
title: Customize Opencode
version: 1.0.0

---
# Customize Opencode

## Overview

Configure OpenCode's own settings, plugins, skills, and MCP servers. Use only when editing OpenCode configuration files or creating OpenCode agents and subagents.

## When to Use

- Editing opencode.json or opencode.jsonc
- Creating or fixing OpenCode agents
- Configuring OpenCode plugins
- Setting up MCP servers
- Creating permission rules
- Customizing OpenCode behavior

## When NOT to Use

- User application code
- Project-specific configuration
- Non-OpenCode tools or frameworks
- General development tasks

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Scaffold new agent skill files |
| `mcp-builder` | Configure MCP server integrations |

## Workflow

### Phase 1: Identify Configuration

- Determine what needs to be configured
- Locate relevant config file
- Review current settings

### Phase 2: Plan Changes

- Understand configuration schema
- Plan modifications
- Check for dependencies

### Phase 3: Apply Configuration

- Edit config files
- Validate syntax
- Test configuration

### Phase 4: Verify & Document

- Confirm changes work
- Document modifications
- Update related configs if needed

## Tools & References

- **Config Files**: opencode.json, opencode.jsonc, .opencode/
- **Documentation**: OpenCode configuration guide

## Best Practices

- Back up config files before changes
- Validate JSON/JSONC syntax
- Test configuration changes
- Document custom configurations
- Keep configs in version control
- Use schema validation tools

## Verification Checklist

- [ ] Target config file located and backed up
- [ ] Schema validated before editing
- [ ] Changes applied and syntax-checked
- [ ] OpenCode behavior tested after changes
- [ ] Custom configurations documented
- [ ] Version control updated

## Pitfalls

- Editing syntax-invalid JSONC causes silent load failures
- Forgetting to restart OpenCode after config changes leaves old behavior active
- Plugin dependency mismatches only surface at runtime
- Overwriting existing configs without backup loses prior working configuration