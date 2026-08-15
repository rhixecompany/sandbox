# Canonical YAML Frontmatter Template

Every `.prompt.md` file MUST include complete YAML frontmatter between `---` markers.

## Required Fields

```yaml
---
# Unique identifier (lowercase, no spaces, used in file naming)
name: prompt-name

# Human-readable title
title: "Descriptive title of the prompt"

# Short description of what this prompt does
description: |
  Multi-line description explaining the purpose, inputs, and outputs.
  Used for discovery and indexing.

# Semantic version (e.g., 1.0.0, 2.1.3)
version: 1.0.0

# License (e.g., MIT, Apache-2.0, CC-BY-4.0)
license: MIT

# Author name or organization
author: "Hermes Agent"

# CLI trigger command (e.g., /setup, /dev, /debug-issue)
# Must be unique across all prompts, CLI-safe, start with /
trigger: /prompt-name

# Required MCP server toolsets for this prompt
# Valid values: file, terminal, web, browser, code_execution, vision, image_gen, tts
toolsets:
  - file
  - terminal
  - code_execution

# Hermes skill IDs required by this prompt
# Format: skill:skill-name
skills:
  - skill:subagent-driven-development
  - skill:using-superpowers

# Prompt/skill dependencies
# Format: prompt:name or skill:name
dependencies:
  - prompt:create-implementation-plan
  - skill:validation-checklist

# Output formatter (default|markdown|json|yaml|html)
formatter: default

# Path to phases/breakdown template (optional)
plan: null

# Metadata for agent-specific configuration
metadata:
  # Hermes Agent configuration
  hermes:
    # Target profile for routing (code-architect|research-analyst|creative-director|exec-assistant|patient-tutor|alexa|default)
    profile: code-architect
    # Required MCP servers for this prompt
    mcp_servers:
      - github
      - filesystem
      - ast-grep
    # Session context needed (small|medium|large)
    context_size: medium

  # GitHub Copilot (VS Code) configuration
  copilot:
    # Estimated context requirement (small|medium|large)
    context_size: medium
    # VS Code extension dependencies (optional)
    extensions: []
    # Keybinding for quick access (optional)
    keybinding: null

  # OpenCode CLI configuration
  opencode:
    # CLI command syntax (e.g., opencode /prompt-name --flag value)
    command: "opencode /prompt-name"
    # Supported CLI flags and defaults
    flags:
      --mode: "interactive"
      --output: "text"
    # Help text for CLI discovery
    help: "Short description shown in opencode --help"

  # Codex AI configuration
  codex:
    # Preferred model (claude|deepseek|gpt|gemma|etc)
    model_override: null
    # System prompt variant ID (optional)
    system_prompt_id: null
    # Temperature hint (0.0-1.0, null for default)
    temperature: null
    # Max tokens hint (null for default)
    max_tokens: null

# Search/discovery tags (lowercase, hyphenated)
# Categories: agent-type, domain, framework, tool, language, complexity
tags:
  - agent-type:hermes
  - agent-type:copilot
  - domain:setup
  - complexity:advanced

# Scripts to run before/after prompt execution (optional)
scripts: []
---
```

## Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Unique kebab-case identifier |
| `title` | string | ✅ | Human-readable title |
| `description` | string | ✅ | Multi-line description |
| `version` | string | ✅ | Semantic version (e.g., 1.0.0) |
| `license` | string | ✅ | License identifier |
| `author` | string | ✅ | Author or org name |
| `trigger` | string | ✅ | CLI trigger (must start with `/`, be unique) |
| `toolsets` | array | ✅ | Required MCP toolsets |
| `skills` | array | ✅ | Required Hermes skills |
| `dependencies` | array | ✅ | Prompt/skill dependencies |
| `formatter` | string | ✅ | Output format |
| `plan` | string | ❌ | Path to phases breakdown |
| `metadata.hermes` | object | ✅ | Hermes profile + MCP config |
| `metadata.copilot` | object | ✅ | VS Code Copilot config |
| `metadata.opencode` | object | ✅ | OpenCode CLI config |
| `metadata.codex` | object | ✅ | Codex AI model hints |
| `tags` | array | ✅ | Discovery tags |
| `scripts` | array | ❌ | Pre/post-execution scripts |

## Validation Rules

1. **`trigger` must be unique** across all 226 prompts
2. **`trigger` must be CLI-safe**: start with `/`, contain only `a-z`, `-`, digits, no spaces
3. **All required fields must be present** and non-empty
4. **YAML must parse without errors** (validate with `yamllint` or similar)
5. **`metadata` fields must have all subfields** (hermes, copilot, opencode, codex)
6. **`skills` and `dependencies`** must reference existing prompts/skills
7. **`tags` must include at least one of**: agent-type, domain, framework, tool, language, complexity

## Examples

### Example 1: Setup Prompt (Hermes Profile)

```yaml
---
name: hermes-setup
title: "Hermes Agent Setup & Configuration"
description: "Complete Hermes Agent setup, MCP configuration, and profile routing."
version: 1.0.0
license: MIT
author: "Hermes Agent"
trigger: /hermes-setup
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: default
plan: null
metadata:
  hermes:
    profile: default
    mcp_servers:
      - filesystem
      - github
      - sequential-thinking
    context_size: large
  copilot:
    context_size: large
    extensions: []
  opencode:
    command: "opencode /hermes-setup"
    flags:
      --profile: "default"
  codex:
    model_override: null
tags:
  - agent-type:hermes
  - domain:setup
  - complexity:intermediate
scripts: []
---
```

### Example 2: Code Review Prompt (Multi-Agent)

```yaml
---
name: code-review
title: "Code Review Assistant"
description: "Comprehensive code review covering security, performance, maintainability."
version: 2.0.0
license: MIT
author: "Copilot Code Review"
trigger: /code-review
toolsets:
  - file
  - code_execution
  - terminal
skills:
  - skill:subagent-driven-development
dependencies:
  - prompt:security-review
formatter: markdown
plan: null
metadata:
  hermes:
    profile: code-architect
    mcp_servers:
      - github
      - ast-grep
      - filesystem
    context_size: large
  copilot:
    context_size: large
    extensions: ["GitHub.copilot"]
  opencode:
    command: "opencode /code-review --file <path>"
    flags:
      --file: ""
      --language: "auto"
  codex:
    model_override: claude
    temperature: 0.1
tags:
  - agent-type:copilot
  - agent-type:opencode
  - domain:code-quality
  - framework:generic
  - complexity:advanced
scripts: []
---
```

## Cross-Reference Examples

```yaml
# Referencing another prompt
dependencies:
  - prompt:create-implementation-plan

# Referencing a skill
dependencies:
  - skill:using-superpowers

# Referencing a template body
# (Note: Template content is extracted into templates/{trigger}/README.md)
# This is handled in Phase 3: Deduplication
```

## Agent Routing Semantics

The `metadata` section controls how different agents discover and execute this prompt:

| Agent | Discovery Method | Routing Field | Example |
|-------|------------------|---------------|---------|
| **Hermes** | `hermes profile use <profile>` | `metadata.hermes.profile` | Routes to `code-architect`, `research-analyst`, etc. |
| **Copilot** | VS Code command palette | `metadata.copilot.extensions` | Requires `GitHub.copilot` extension |
| **OpenCode CLI** | `opencode /trigger` | `metadata.opencode.command` | Parses CLI flags and arguments |
| **Codex AI** | Model selection | `metadata.codex.model_override` | Forces specific LLM (claude, gpt, deepseek) |

