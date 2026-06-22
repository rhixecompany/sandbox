# lib/my_mcp_server/prompts/code_review_prompt.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## lib/my_mcp_server/prompts/code_review_prompt.rb Template

```ruby
# frozen_string_literal: true

module MyMcpServer
  module Prompts
    class CodeReviewPrompt < MCP::Prompt
      prompt_name 'code_review'
      description 'Generate a code review prompt'

      arguments [
        MCP::Prompt::Argument.new(
          name: 'language',
          description: 'Programming language',
          required: true
        ),
        MCP::Prompt::Argument.new(
          name: 'focus',
          description: 'Review focus area (e.g., performance, security)',
          required: false
        )
      ]

      meta(
        version: '1.0',
        category: 'development'
      )

      def self.template(args, server_context:)
        language = args['language'] || 'Ruby'
        focus = args['focus'] || 'general quality'

        MCP::Prompt::Result.new(
          description: "Code review for #{language} with focus on #{focus}",
          messages: [
            MCP::Prompt::Message.new(
              role: 'user',
              content: MCP::Content::Text.new(
                "Please review this #{language} code with focus on #{focus}."
              )
            ),
            MCP::Prompt::Message.new(
              role: 'assistant',
              content: MCP::Content::Text.new(
                "I'll review the code focusing on #{focus}. Please share the code."
              )
            ),
            MCP::Prompt::Message.new(
              role: 'user',
              content: MCP::Content::Text.new(
                '[paste code here]'
              )
            )
          ]
        )
      end
    end
  end
end
```
