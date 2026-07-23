# lib/my_mcp_server/tools/greet_tool.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## lib/my_mcp_server/tools/greet_tool.rb Template

```ruby
# frozen_string_literal: true

module MyMcpServer
  module Tools
    class GreetTool < MCP::Tool
      tool_name 'greet'
      description 'Generate a greeting message'

      input_schema(
        properties: {
          name: {
            type: 'string',
            description: 'Name to greet'
          }
        },
        required: ['name']
      )

      output_schema(
        properties: {
          message: { type: 'string' },
          timestamp: { type: 'string', format: 'date-time' }
        },
        required: ['message', 'timestamp']
      )

      annotations(
        read_only_hint: true,
        idempotent_hint: true
      )

      def self.call(name:, server_context:)
        timestamp = Time.now.iso8601
        message = "Hello, #{name}! Welcome to MCP."

        structured_data = {
          message: message,
          timestamp: timestamp
        }

        MCP::Tool::Response.new(
          [{ type: 'text', text: message }],
          structured_content: structured_data
        )
      end
    end
  end
end
```
