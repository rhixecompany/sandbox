# test/tools/calculate_tool_test.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## test/tools/calculate_tool_test.rb Template

```ruby
# frozen_string_literal: true

require 'test_helper'

module MyMcpServer
  module Tools
    class CalculateToolTest < Minitest::Test
      def test_addition
        response = CalculateTool.call(
          operation: 'add',
          a: 5,
          b: 3,
          server_context: {}
        )

        refute response.is_error
        assert_equal 8, response.structured_content[:result]
      end

      def test_subtraction
        response = CalculateTool.call(
          operation: 'subtract',
          a: 10,
          b: 4,
          server_context: {}
        )

        refute response.is_error
        assert_equal 6, response.structured_content[:result]
      end

      def test_multiplication
        response = CalculateTool.call(
          operation: 'multiply',
          a: 6,
          b: 7,
          server_context: {}
        )

        refute response.is_error
        assert_equal 42, response.structured_content[:result]
      end

      def test_division
        response = CalculateTool.call(
          operation: 'divide',
          a: 15,
          b: 3,
          server_context: {}
        )

        refute response.is_error
        assert_equal 5.0, response.structured_content[:result]
      end

      def test_division_by_zero
        response = CalculateTool.call(
          operation: 'divide',
          a: 10,
          b: 0,
          server_context: {}
        )

        assert response.is_error
        assert_match(/Division by zero/, response.content.first[:text])
      end

      def test_unknown_operation
        response = CalculateTool.call(
          operation: 'modulo',
          a: 10,
          b: 3,
          server_context: {}
        )

        assert response.is_error
        assert_match(/Unknown operation/, response.content.first[:text])
      end
    end
  end
end
```
