# lib/my_mcp_server/server.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## lib/my_mcp_server/server.rb Template

```ruby
# frozen_string_literal: true

module MyMcpServer
  class Server
    attr_reader :mcp_server

    def initialize(server_context: {})
      @mcp_server = MCP::Server.new(
        name: 'my_mcp_server',
        version: MyMcpServer::VERSION,
        tools: [
          Tools::GreetTool,
          Tools::CalculateTool
        ],
        prompts: [
          Prompts::CodeReviewPrompt
        ],
        resources: [
          Resources::ExampleResource.resource
        ],
        server_context: server_context
      )

      setup_resource_handler
    end

    def handle_json(json_string)
      mcp_server.handle_json(json_string)
    end

    def start_stdio
      transport = MCP::Server::Transports::StdioTransport.new(mcp_server)
      transport.open
    end

    private

    def setup_resource_handler
      mcp_server.resources_read_handler do |params|
        Resources::ExampleResource.read(params[:uri])
      end
    end
  end
end
```
