---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Ruby MCP Server Generator
name: ruby-mcp-server-generator
description: "Generate a complete Model Context Protocol server project in Ruby using the official MCP Ruby SDK gem."
tags: []
---

# Ruby MCP Server Generator

Generate a complete, production-ready MCP server in Ruby using the official Ruby SDK.

## Project Generation

When asked to create a Ruby MCP server, generate a complete project with this structure:

```
my-mcp-server/
├── Gemfile
├── Rakefile
├── lib/
│   ├── my_mcp_server.rb
│   ├── my_mcp_server/
│   │   ├── server.rb
│   │   ├── tools/
│   │   │   ├── greet_tool.rb
│   │   │   └── calculate_tool.rb
│   │   ├── prompts/
│   │   │   └── code_review_prompt.rb
│   │   └── resources/
│   │       └── example_resource.rb
├── bin/
│   └── mcp-server
├── test/
│   ├── test_helper.rb
│   └── tools/
│       ├── greet_tool_test.rb
│       └── calculate_tool_test.rb
└── README.md
```

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

> # frozen_string_literal: true
> attr_reader :mcp_server

> **Full content:** `templates/ruby-mcp-server-generator/libmy_mcp_serverserverrb_templ.md`

## lib/my_mcp_server/tools/greet_tool.rb Template

> # frozen_string_literal: true
> class GreetTool < MCP::Tool

> **Full content:** `templates/ruby-mcp-server-generator/libmy_mcp_servertoolscalculate.md`

## lib/my_mcp_server/tools/calculate_tool.rb Template

> # frozen_string_literal: true
> class CalculateTool < MCP::Tool

> **Full content:** `templates/ruby-mcp-server-generator/libmy_mcp_servertoolscalculate.md`

## lib/my_mcp_server/prompts/code_review_prompt.rb Template

> # frozen_string_literal: true
> class CodeReviewPrompt < MCP::Prompt

> **Full content:** `templates/ruby-mcp-server-generator/libmy_mcp_serverpromptscode_re.md`

## lib/my_mcp_server/resources/example_resource.rb Template

> # frozen_string_literal: true
> class ExampleResource

> **Full content:** `templates/ruby-mcp-server-generator/libmy_mcp_serverresourcesexamp.md`

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

> # frozen_string_literal: true
> require 'test_helper'

> **Full content:** `templates/ruby-mcp-server-generator/testtoolsgreet_tool_testrb_tem.md`

## test/tools/calculate_tool_test.rb Template

> # frozen_string_literal: true
> require 'test_helper'

> **Full content:** `templates/ruby-mcp-server-generator/testtoolscalculate_tool_testrb.md`

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
````

## Usage

> bundle exec bin/mcp-server
> Then send JSON-RPC requests:

> **Full content:** `templates/ruby-mcp-server-generator/usage.md`

## Testing

Run tests:

```bash
bundle exec rake test
```

Run linter:

```bash
bundle exec rake rubocop
```

Run all checks:

```bash
bundle exec rake
```

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "bundle",
      "args": ["exec", "bin/mcp-server"],
      "cwd": "/path/to/my-mcp-server"
    }
  }
}
```

## Project Structure

```
my-mcp-server/
├── Gemfile              # Dependencies
├── Rakefile             # Build tasks
├── lib/                 # Source code
│   ├── my_mcp_server.rb # Main entry point
│   └── my_mcp_server/   # Module namespace
│       ├── server.rb    # Server setup
│       ├── tools/       # Tool implementations
│       ├── prompts/     # Prompt templates
│       └── resources/   # Resource handlers
├── bin/                 # Executables
│   └── mcp-server       # Stdio server
├── test/                # Test suite
│   ├── test_helper.rb   # Test configuration
│   └── tools/           # Tool tests
└── README.md            # This file
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

Detailed templates in `templates/ruby-mcp-server-generator/`:
- `libmy_mcp_serverpromptscode_re.md`
- `libmy_mcp_serverresourcesexamp.md`
- `libmy_mcp_serverserverrb_templ.md`
- `libmy_mcp_servertoolscalculate.md`
- `libmy_mcp_servertoolsgreet_too.md`
- `testtoolscalculate_tool_testrb.md`
- `testtoolsgreet_tool_testrb_tem.md`
- `usage.md`
