package main

import (
	"context"
	"encoding/json"
	"testing"

	"go-mcp-server/tools"
)

func TestGreetTool(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	def, ok := reg.Get("greet")
	if !ok {
		t.Fatal("greet tool not registered")
	}

	args := mustMarshal(map[string]string{"name": "Alice"})
	result, err := def.Handler(context.Background(), args)
	if err != nil {
		t.Fatalf("greet handler error: %v", err)
	}

	var output tools.GreetOutput
	if err := json.Unmarshal(result, &output); err != nil {
		t.Fatalf("failed to unmarshal output: %v", err)
	}

	if output.Greeting == "" {
		t.Error("expected non-empty greeting")
	}
	if output.Greeting != "Hello, Alice! Welcome to the Go MCP server." {
		t.Errorf("unexpected greeting: %s", output.Greeting)
	}
}

func TestGreetToolDefaultName(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	def, ok := reg.Get("greet")
	if !ok {
		t.Fatal("greet tool not registered")
	}

	// Empty name should default to "World"
	args := mustMarshal(map[string]string{"name": ""})
	result, err := def.Handler(context.Background(), args)
	if err != nil {
		t.Fatalf("greet handler error: %v", err)
	}

	var output tools.GreetOutput
	if err := json.Unmarshal(result, &output); err != nil {
		t.Fatalf("failed to unmarshal output: %v", err)
	}

	if output.Greeting != "Hello, World! Welcome to the Go MCP server." {
		t.Errorf("unexpected default greeting: %s", output.Greeting)
	}
}

func TestFileInfoToolNotFound(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	def, ok := reg.Get("file_info")
	if !ok {
		t.Fatal("file_info tool not registered")
	}

	args := mustMarshal(map[string]string{"path": "/nonexistent/path/xyz123"})
	result, err := def.Handler(context.Background(), args)
	if err != nil {
		t.Fatalf("file_info handler error: %v", err)
	}

	var output tools.FileInfoOutput
	if err := json.Unmarshal(result, &output); err != nil {
		t.Fatalf("failed to unmarshal output: %v", err)
	}

	if output.Exists {
		t.Error("expected exists=false for nonexistent path")
	}
}

func TestFileInfoToolMissingPath(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	def, ok := reg.Get("file_info")
	if !ok {
		t.Fatal("file_info tool not registered")
	}

	// Empty path should return an error
	args := mustMarshal(map[string]string{"path": ""})
	_, err := def.Handler(context.Background(), args)
	if err == nil {
		t.Error("expected error for empty path")
	}
}

func TestRegistryDuplicate(t *testing.T) {
	reg := tools.NewRegistry()
	err := reg.Register(tools.GreetToolDefinition(), tools.GreetToolDefinition())
	if err == nil {
		t.Error("expected error when registering duplicate tool")
	}
}

func TestInitializeMessage(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	msg := mcpMessage{
		JSONRPC: "2.0",
		ID:      json.RawMessage(`1`),
		Method:  "initialize",
		Params:  json.RawMessage(`{}`),
	}

	resp := handleMessage(context.Background(), msg, reg)
	if resp == nil {
		t.Fatal("expected response for initialize")
	}
	if resp.Error != nil {
		t.Fatalf("unexpected error: %+v", resp.Error)
	}
	if resp.Result == nil {
		t.Fatal("expected result in initialize response")
	}

	var result map[string]interface{}
	if err := json.Unmarshal(resp.Result, &result); err != nil {
		t.Fatalf("failed to parse result: %v", err)
	}
	if result["protocolVersion"] != "2024-11-05" {
		t.Errorf("unexpected protocol version: %v", result["protocolVersion"])
	}
}

func TestToolsListMessage(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	msg := mcpMessage{
		JSONRPC: "2.0",
		ID:      json.RawMessage(`2`),
		Method:  "tools/list",
	}

	resp := handleMessage(context.Background(), msg, reg)
	if resp == nil {
		t.Fatal("expected response for tools/list")
	}
	if resp.Error != nil {
		t.Fatalf("unexpected error: %+v", resp.Error)
	}

	var result listToolsResult
	if err := json.Unmarshal(resp.Result, &result); err != nil {
		t.Fatalf("failed to parse tools list: %v", err)
	}
	if len(result.Tools) != 2 {
		t.Errorf("expected 2 tools, got %d", len(result.Tools))
	}
}

func TestUnknownMethod(t *testing.T) {
	reg := tools.NewRegistry()
	tools.MustRegisterDefaults(reg)

	msg := mcpMessage{
		JSONRPC: "2.0",
		ID:      json.RawMessage(`3`),
		Method:  "bogus_method",
	}

	resp := handleMessage(context.Background(), msg, reg)
	if resp == nil {
		t.Fatal("expected error response for unknown method")
	}
	if resp.Error == nil {
		t.Fatal("expected error in response")
	}
	if resp.Error.Code != -32601 {
		t.Errorf("expected error code -32601, got %d", resp.Error.Code)
	}
}

func mustMarshal(v interface{}) json.RawMessage {
	data, err := json.Marshal(v)
	if err != nil {
		panic(err)
	}
	return data
}
