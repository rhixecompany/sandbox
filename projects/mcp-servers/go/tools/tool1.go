package tools

import (
	"context"
	"encoding/json"
	"fmt"
)

// GreetInput is the input parameters for the greet tool.
type GreetInput struct {
	Name string `json:"name" description:"The name of the person to greet"`
}

// GreetOutput is the output of the greet tool.
type GreetOutput struct {
	Greeting string `json:"greeting" description:"The generated greeting message"`
}

// GreetHandler handles the "greet" tool call.
func GreetHandler(ctx context.Context, args json.RawMessage) (json.RawMessage, error) {
	var input GreetInput
	if err := json.Unmarshal(args, &input); err != nil {
		return nil, fmt.Errorf("invalid arguments: %w", err)
	}
	if input.Name == "" {
		input.Name = "World"
	}

	output := GreetOutput{
		Greeting: fmt.Sprintf("Hello, %s! Welcome to the Go MCP server.", input.Name),
	}

	result, err := json.Marshal(output)
	if err != nil {
		return nil, fmt.Errorf("failed to marshal output: %w", err)
	}
	return result, nil
}

// GreetToolDefinition returns the ToolDefinition for the greet tool.
func GreetToolDefinition() ToolDefinition {
	return ToolDefinition{
		Name:        "greet",
		Description: "Generate a personalized greeting message",
		InputSchema: map[string]interface{}{
			"type": "object",
			"properties": map[string]interface{}{
				"name": map[string]interface{}{
					"type":        "string",
					"description": "The name of the person to greet",
				},
			},
			"required": []string{},
		},
		Handler: GreetHandler,
	}
}
