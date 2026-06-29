# test/tools/greet_tool_test.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## test/tools/greet_tool_test.rb Template

```ruby
# frozen_string_literal: true

require 'test_helper'

module MyMcpServer
  module Tools
    class GreetToolTest < Minitest::Test
      def test_greet_with_name
        response = GreetTool.call(
          name: 'Ruby',
          server_context: {}
        )

        refute response.is_error
        assert_equal 1, response.content.length
        assert_match(/Ruby/, response.content.first[:text])

        assert response.structured_content
        assert_equal 'Hello, Ruby! Welcome to MCP.', response.structured_content[:message]
      end

      def test_output_schema_validation
        response = GreetTool.call(
          name: 'Test',
          server_context: {}
        )

        assert response.structured_content.key?(:message)
        assert response.structured_content.key?(:timestamp)
      end
    end
  end
end
```
