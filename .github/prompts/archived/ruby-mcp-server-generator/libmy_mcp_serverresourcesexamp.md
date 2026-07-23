# lib/my_mcp_server/resources/example_resource.rb Template

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## lib/my_mcp_server/resources/example_resource.rb Template

```ruby
# frozen_string_literal: true

module MyMcpServer
  module Resources
    class ExampleResource
      RESOURCE_URI = 'resource://data/example'

      def self.resource
        MCP::Resource.new(
          uri: RESOURCE_URI,
          name: 'example-data',
          description: 'Example resource data',
          mime_type: 'application/json'
        )
      end

      def self.read(uri)
        return [] unless uri == RESOURCE_URI

        data = {
          message: 'Example resource data',
          timestamp: Time.now.iso8601,
          version: MyMcpServer::VERSION
        }

        [{
          uri: uri,
          mimeType: 'application/json',
          text: data.to_json
        }]
      end
    end
  end
end
```
