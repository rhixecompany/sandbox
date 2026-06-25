# frozen_string_literal: true

require_relative 'my_mcp_server/server'
require_relative 'my_mcp_server/tools/greet_tool'
require_relative 'my_mcp_server/tools/calculate_tool'

# Main entry point for the Ruby MCP server.
module MyMcpServer
  NAME = 'ruby-mcp-server'
  VERSION = '0.1.0'

  def self.start!
    server = Server.new
    server.register_tool(Tools::GreetTool)
    server.register_tool(Tools::CalculateTool)
    server.run
  end
end
