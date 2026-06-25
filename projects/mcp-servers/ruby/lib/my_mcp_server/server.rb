# frozen_string_literal: true

require 'mcp'

module MyMcpServer
  # Configures and runs the MCP server using the `mcp` gem.
  class Server
    def initialize
      @tools = {}
    end

    # Register a tool class (must respond to .name, .description, .schema and .execute).
    def register_tool(tool_class)
      name = tool_class.name
      @tools[name] = tool_class
    end

    # Start the MCP server and listen for requests.
    def run
      Mcp::Server.start(
        name: MyMcpServer::NAME,
        version: MyMcpServer::VERSION,
        tools: @tools.values.map { |klass|
          {
            name: klass.name,
            description: klass.description,
            inputSchema: klass.schema
          }
        }
      ) do |request|
        handle_request(request)
      end
    end

    private

    def handle_request(request)
      tool_name = request[:tool]
      tool_class = @tools[tool_name]

      unless tool_class
        { error: "Unknown tool: #{tool_name}" }
        next
      end

      tool_class.execute(request[:arguments])
    end
  end
end
