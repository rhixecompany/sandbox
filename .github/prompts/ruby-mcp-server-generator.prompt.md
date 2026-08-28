---
name: ruby-mcp-server-generator
title: Ruby MCP Server Generator
description: Scaffolds a complete, production-ready Model Context Protocol server in Ruby using the official MCP Ruby SDK, with tools, prompts, resources, and tests.
version: 1.0.0
author: Hermes Agent
tags:
- tool
- automation
- backend
- ruby
- mcp
- scaffolding
- documentation
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

## Context

## Phases

# Table of Contents

- [Goal](#goal)
- [Project Generation](#project-generation)
- [Gemfile Template](#gemfile-template)
- [Rakefile Template](#rakefile-template)
- [lib/my_mcp_server.rb Template](#lib/my_mcp_serverrb-template)
- [lib/my_mcp_server/server.rb Template](#lib/my_mcp_server/serverrb-template)
- [lib/my_mcp_server/tools/greet_tool.rb Template](#lib/my_mcp_server/tools/greet_toolrb-template)
- [lib/my_mcp_server/tools/calculate_tool.rb Template](#lib/my_mcp_server/tools/calculate_toolrb-template)
- [lib/my_mcp_server/prompts/code_review_prompt.rb Template](#lib/my_mcp_server/prompts/code_review_promptrb-template)
- [lib/my_mcp_server/resources/example_resource.rb Template](#lib/my_mcp_server/resources/example_resourcerb-template)
- [bin/mcp-server Template](#bin/mcp-server-template)
- [test/test_helper.rb Template](#test/test_helperrb-template)
- [test/tools/greet_tool_test.rb Template](#test/tools/greet_tool_testrb-template)
- [test/tools/calculate_tool_test.rb Template](#test/tools/calculate_tool_testrb-template)
- [README.md Template](#readmemd-template)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Test](#test)
- [Integration with Claude Desktop](#integration-with-claude-desktop)
- [Project Structure](#project-structure)
- [License](#license)
- [Generation Instructions](#generation-instructions)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Project Generation](#project-generation)
- [Gemfile Template](#gemfile-template)
- [Rakefile Template](#rakefile-template)
- [lib/my_mcp_server.rb Template](#lib/my_mcp_serverrb-template)
- [lib/my_mcp_server/server.rb Template](#lib/my_mcp_server/serverrb-template)
- [lib/my_mcp_server/tools/greet_tool.rb Template](#lib/my_mcp_server/tools/greet_toolrb-template)
- [lib/my_mcp_server/tools/calculate_tool.rb Template](#lib/my_mcp_server/tools/calculate_toolrb-template)
- [lib/my_mcp_server/prompts/code_review_prompt.rb Template](#lib/my_mcp_server/prompts/code_review_promptrb-template)
- [lib/my_mcp_server/resources/example_resource.rb Template](#lib/my_mcp_server/resources/example_resourcerb-template)
- [bin/mcp-server Template](#bin/mcp-server-template)
- [test/test_helper.rb Template](#test/test_helperrb-template)
- [test/tools/greet_tool_test.rb Template](#test/tools/greet_tool_testrb-template)
- [test/tools/calculate_tool_test.rb Template](#test/tools/calculate_tool_testrb-template)
- [README.md Template](#readmemd-template)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Test](#test)
- [Integration with Claude Desktop](#integration-with-claude-desktop)
- [Project Structure](#project-structure)
- [License](#license)
- [Generation Instructions](#generation-instructions)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)
- [Hooks](#hooks)
- [Scripts](#scripts)





Generate a complete Model Context Protocol server project in Ruby using the official MCP Ruby SDK gem.

## Ruby MCP Server GeneratorGenerate a complete, production-ready MCP server in Ruby using the official Ruby SDK.

## Project Generation

When asked to create a Ruby MCP server, generate a complete project with this structure:```my-mcp-server/├── Gemfile├── Rakefile├── lib/│ ├── my_mcp_server.rb│ ├── my_mcp_server/│ │ ├── server.rb│ │ ├── tools/│ │ │ ├── greet_tool.rb│ │ │ └── calculate_tool.rb│ │ ├── prompts/│ │ │ └── code_review_prompt.rb│ │ └── resources/│ │ └── example_resource.rb├── bin/│ └── mcp-server├── test/│ ├── test_helper.rb│ └── tools/│ ├── greet_tool_test.rb│ └── calculate_tool_test.rb└── README.md```

## Gemfile Template

```ruby
source 'https://rubygems.org'

gem 'mcp', '~> 0.4.0'

group :development, :test do
gem 'minitest', '~> 5.0'
gem 'rake', '~> 13.0'
gem 'rubocop', '~> 1.50'
end
```

## Rakefile Template

```ruby
require 'rake/testtask'
require 'rubocop/rake_task'

Rake::TestTask.new(:test) do |t|
t.libs << 'test'
t.libs << 'lib'
t.test_files = FileList['test/**/*_test.rb']
end

RuboCop::RakeTask.new

task default: %i[test rubocop]
```

## lib/my_mcp_server.rb Template

```ruby
# frozen_string_literal: true

require 'mcp'
require_relative 'my_mcp_server/server'
require_relative 'my_mcp_server/tools/greet_tool'
require_relative 'my_mcp_server/tools/calculate_tool'
require_relative 'my_mcp_server/prompts/code_review_prompt'
require_relative 'my_mcp_server/resources/example_resource'

module MyMcpServer
VERSION = '1.0.0'
end
```

## lib/my_mcp_server/server.rb Template

> `# frozen_string_literal: true`
> attr_reader :mcp_server
> **Full content:**

## lib/my_mcp_server/tools/greet_tool.rb Template

> `# frozen_string_literal: true`
> class GreetTool < MCP::Tool
> **Full content:**

## lib/my_mcp_server/tools/calculate_tool.rb Template

> `# frozen_string_literal: true`
> class CalculateTool < MCP::Tool
> **Full content:**

## lib/my_mcp_server/prompts/code_review_prompt.rb Template

> `# frozen_string_literal: true`
> class CodeReviewPrompt < MCP::Prompt
> **Full content:**

## lib/my_mcp_server/resources/example_resource.rb Template

> `# frozen_string_literal: true`
> class ExampleResource
> **Full content:**

## bin/mcp-server Template

```ruby
#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../lib/my_mcp_server'

begin
server = MyMcpServer::Server.new
server.start_stdio
rescue Interrupt
warn "\nShutting down server..."
exit 0
rescue StandardError => e
warn "Error: #{e.message}"
warn e.backtrace.join("\n")
exit 1
end
```

Make the file executable:

```bash
chmod +x bin/mcp-server

```

## test/test_helper.rb Template

```ruby
# frozen_string_literal: true

$LOAD_PATH.unshift File.expand_path('../lib', __dir__)
require 'my_mcp_server'
require 'minitest/autorun'
```

## test/tools/greet_tool_test.rb Template

> `# frozen_string_literal: true`
> require 'test_helper'
> **Full content:**

## test/tools/calculate_tool_test.rb Template

> `# frozen_string_literal: true`
> require 'test_helper'
> **Full content:**

## README.md Template

````markdown
# My MCP Server

A Model Context Protocol server built with Ruby and the official MCP Ruby SDK.

## Features

- ✅ Tools: greet, calculate
- ✅ Prompts: code_review
- ✅ Resources: example-data
- ✅ Input/output schemas
- ✅ Tool annotations
- ✅ Structured content
- ✅ Full test coverage

## Requirements

- Ruby 3.0 or later

## Installation

```bash
bundle install
```

## Usage

> bundle exec bin/mcp-server
> Then send JSON-RPC requests:

## Test

ing

Run tests:```bashbundle exec rake test```Run linter:```bashbundle exec rake rubocop```Run all checks:```bashbundle exec rake```

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:```json{ "mcpServers": { "my-mcp-server": { "command": "bundle", "args": ["exec", "bin/mcp-server"], "cwd": "/path/to/my-mcp-server" } }}```

## Project Structure

```
my-mcp-server/
├── Gemfile # Dependencies
├── Rakefile # Build tasks
├── lib/ # Source code
│ ├── my_mcp_server.rb # Main entry point
│ └── my_mcp_server/ # Module namespace
│ ├── server.rb # Server setup
│ ├── tools/ # Tool implementations
│ ├── prompts/ # Prompt templates
│ └── resources/ # Resource handlers
├── bin/ # Executables
│ └── mcp-server # Stdio server
├── test/ # Test suite
│ ├── test_helper.rb # Test configuration
│ └── tools/ # Tool tests
└── README.md # This file
```

## License

MIT

```

## Generation Instructions

1. **Ask for project name and description**
2. **Generate all files** with proper naming and module structure
3. **Use classes for tools and prompts** for better organization
4. **Include input/output schemas** for type safety
5. **Add tool annotations** for behavior hints
6. **Include structured content** in responses
7. **Implement comprehensive tests** for all tools
8. **Follow Ruby conventions** (snake_case, modules, frozen_string_literal)
9. **Add proper error handling** with is_error flag
10. **Provide both stdio and HTTP** usage examples
```

## Template References

Detailed templates in `templates/ruby-mcp-server-generator/`:- `libmy_mcp_serverpromptscode_re.md`- `libmy_mcp_serverresourcesexamp.md`- `libmy_mcp_serverserverrb_templ.md`- `libmy_mcp_servertoolscalculate.md`- `libmy_mcp_servertoolsgreet_too.md`- `testtoolscalculate_tool_testrb.md`- `testtoolsgreet_tool_testrb_tem.md`- `usage.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.


### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings .
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Related Prompts

Other language variants of this MCP server generator:

| Language | Prompt |
| ---------- | -------- |
| TypeScript | [`typescript-mcp-server-generator.prompt.md`](typescript-mcp-server-generator.prompt.md) |
| Python | [`python-mcp-server-generator.prompt.md`](python-mcp-server-generator.prompt.md) |
| Rust | [`rust-mcp-server-generator.prompt.md`](rust-mcp-server-generator.prompt.md) |
| Go | [`go-mcp-server-generator.prompt.md`](go-mcp-server-generator.prompt.md) |
| Swift | [`swift-mcp-server-generator.prompt.md`](swift-mcp-server-generator.prompt.md) |
| Kotlin | [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md) |
| Java | [`java-mcp-server-generator.prompt.md`](java-mcp-server-generator.prompt.md) |
| C# | [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md) |
| PHP | [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md) |

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section