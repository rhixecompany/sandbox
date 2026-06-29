# Usage

> Extracted from `ruby-mcp-server-generator.prompt.md`.

## Usage

### Stdio Transport

Run the server:

```bash
bundle exec bin/mcp-server
```

Then send JSON-RPC requests:

```bash
{"jsonrpc":"2.0","id":"1","method":"ping"}
{"jsonrpc":"2.0","id":"2","method":"tools/list"}
{"jsonrpc":"2.0","id":"3","method":"tools/call","params":{"name":"greet","arguments":{"name":"Ruby"}}}
```

### Rails Integration

Add to your Rails controller:

```ruby
class McpController < ApplicationController
  def index
    server = MyMcpServer::Server.new(
      server_context: { user_id: current_user.id }
    )
    render json: server.handle_json(request.body.read)
  end
end
```
