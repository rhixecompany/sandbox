// go-mcp-server is a Go implementation of an MCP (Model Context Protocol) server
// that exposes greeting and file-info tools over stdio transport.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"

	"go-mcp-server/config"
	"go-mcp-server/tools"
)

// mcpMessage represents a JSON-RPC message for the MCP protocol.
type mcpMessage struct {
	JSONRPC string          `json:"jsonrpc"`
	ID      json.RawMessage `json:"id,omitempty"`
	Method  string          `json:"method,omitempty"`
	Params  json.RawMessage `json:"params,omitempty"`
	Result  json.RawMessage `json:"result,omitempty"`
	Error   *mcpError       `json:"error,omitempty"`
}

// mcpError represents a JSON-RPC error object.
type mcpError struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// listToolsResult is the result of the "tools/list" method.
type listToolsResult struct {
	Tools []toolDescription `json:"tools"`
}

// toolDescription describes a tool in the MCP list response.
type toolDescription struct {
	Name        string      `json:"name"`
	Description string      `json:"description"`
	InputSchema interface{} `json:"inputSchema"`
}

// callToolParams is the params for the "tools/call" method.
type callToolParams struct {
	Name      string          `json:"name"`
	Arguments json.RawMessage `json:"arguments"`
}

// callToolResult is the result of the "tools/call" method.
type callToolResult struct {
	Content []contentItem `json:"content"`
	IsError bool          `json:"isError,omitempty"`
}

// contentItem holds a single piece of tool output content.
type contentItem struct {
	Type string `json:"type"`
	Text string `json:"text"`
}

func main() {
	cfg := config.FromEnv(config.Default())
	log.SetFlags(0)
	log.SetPrefix("")

	log.Printf("Starting %s v%s (log level: %s)", cfg.ServerName, cfg.ServerVersion, cfg.LogLevel)

	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Handle OS signals for graceful shutdown.
	sigCh := make(chan os.Signal, 1)
	signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		<-sigCh
		log.Println("Shutting down...")
		cancel()
	}()

	// Main loop: read JSON-RPC messages from stdin and write responses to stdout.
	decoder := json.NewDecoder(os.Stdin)
	encoder := json.NewEncoder(os.Stdout)

	log.Println("MCP server ready (stdio transport)")
	for {
		var msg mcpMessage
		if err := decoder.Decode(&msg); err != nil {
			// EOF or decode error — exit gracefully
			if ctx.Err() != nil {
				return
			}
			log.Printf("Decode error: %v", err)
			return
		}

		response := handleMessage(ctx, msg, reg)
		if response != nil {
			if err := encoder.Encode(response); err != nil {
				log.Printf("Encode error: %v", err)
				return
			}
		}
	}
}

// handleMessage processes a single MCP message and returns the response.
func handleMessage(ctx context.Context, msg mcpMessage, reg *tools.Registry) *mcpMessage {
	switch msg.Method {
	case "initialize":
		return &mcpMessage{
			JSONRPC: "2.0",
			ID:      msg.ID,
			Result: mustMarshal(map[string]interface{}{
				"protocolVersion": "2024-11-05",
				"serverInfo": map[string]interface{}{
					"name":    "go-mcp-server",
					"version": "1.0.0",
				},
				"capabilities": map[string]interface{}{
					"tools": map[string]interface{}{},
				},
			}),
		}

	case "tools/list":
		toolDefs := reg.List()
		descs := make([]toolDescription, len(toolDefs))
		for i, def := range toolDefs {
			descs[i] = toolDescription{
				Name:        def.Name,
				Description: def.Description,
				InputSchema: def.InputSchema,
			}
		}
		return &mcpMessage{
			JSONRPC: "2.0",
			ID:      msg.ID,
			Result:  mustMarshal(listToolsResult{Tools: descs}),
		}

	case "tools/call":
		var params callToolParams
		if err := json.Unmarshal(msg.Params, &params); err != nil {
			return errorResponse(msg.ID, -32602, "Invalid params: "+err.Error())
		}

		result, err := reg.Execute(ctx, params.Name, params.Arguments)
		if err != nil {
			return &mcpMessage{
				JSONRPC: "2.0",
				ID:      msg.ID,
				Result: mustMarshal(callToolResult{
					Content: []contentItem{
						{Type: "text", Text: fmt.Sprintf("Error: %v", err)},
					},
					IsError: true,
				}),
			}
		}

		return &mcpMessage{
			JSONRPC: "2.0",
			ID:      msg.ID,
			Result: mustMarshal(callToolResult{
				Content: []contentItem{
					{Type: "text", Text: string(result)},
				},
			}),
		}

	case "notifications/initialized":
		// No response needed for this notification.
		return nil

	default:
		return errorResponse(msg.ID, -32601, fmt.Sprintf("Method not found: %s", msg.Method))
	}
}

// errorResponse creates a JSON-RPC error response.
func errorResponse(id json.RawMessage, code int, message string) *mcpMessage {
	return &mcpMessage{
		JSONRPC: "2.0",
		ID:      id,
		Error: &mcpError{
			Code:    code,
			Message: message,
		},
	}
}

// mustMarshal panics if marshaling fails — used for responses we know will succeed.
func mustMarshal(v interface{}) json.RawMessage {
	data, err := json.Marshal(v)
	if err != nil {
		panic(fmt.Sprintf("mustMarshal: %v", err))
	}
	return data
}
