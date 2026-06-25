// Package tools provides the tool definitions and handlers for the MCP server.
package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"sync"
)

// HandlerFunc is the signature for a function that handles a tool call.
type HandlerFunc func(ctx context.Context, args json.RawMessage) (json.RawMessage, error)

// ToolDefinition describes a single tool that the MCP server exposes.
type ToolDefinition struct {
	// Name is the unique identifier for this tool.
	Name string

	// Description is a human-readable explanation of what the tool does.
	Description string

	// InputSchema is a JSON Schema object describing the expected input parameters.
	InputSchema map[string]interface{}

	// Handler is the function invoked when the tool is called.
	Handler HandlerFunc
}

// Registry holds all registered tool definitions.
type Registry struct {
	mu    sync.RWMutex
	tools map[string]ToolDefinition
}

// NewRegistry creates an empty tool registry.
func NewRegistry() *Registry {
	return &Registry{
		tools: make(map[string]ToolDefinition),
	}
}

// Register adds one or more tool definitions to the registry.
// It returns an error if any tool name is already registered.
func (r *Registry) Register(defs ...ToolDefinition) error {
	r.mu.Lock()
	defer r.mu.Unlock()

	for _, def := range defs {
		if _, exists := r.tools[def.Name]; exists {
			return fmt.Errorf("tool %q is already registered", def.Name)
		}
		if def.Name == "" {
			return fmt.Errorf("tool name cannot be empty")
		}
		r.tools[def.Name] = def
	}
	return nil
}

// Get returns the tool definition for the given name.
func (r *Registry) Get(name string) (ToolDefinition, bool) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	def, ok := r.tools[name]
	return def, ok
}

// List returns all registered tool definitions.
func (r *Registry) List() []ToolDefinition {
	r.mu.RLock()
	defer r.mu.RUnlock()

	defs := make([]ToolDefinition, 0, len(r.tools))
	for _, def := range r.tools {
		defs = append(defs, def)
	}
	return defs
}

// Execute looks up a tool by name and calls its handler with the given arguments.
func (r *Registry) Execute(ctx context.Context, name string, args json.RawMessage) (json.RawMessage, error) {
	def, ok := r.Get(name)
	if !ok {
		return nil, fmt.Errorf("unknown tool: %s", name)
	}
	return def.Handler(ctx, args)
}

// DefaultTools returns the tool definitions that ship with the server.
func DefaultTools() []ToolDefinition {
	return []ToolDefinition{
		GreetToolDefinition(),
		FileInfoToolDefinition(),
	}
}

// MustRegisterDefaults registers all default tools and panics on error.
func MustRegisterDefaults(r *Registry) {
	if err := r.Register(DefaultTools()...); err != nil {
		panic(fmt.Sprintf("failed to register default tools: %v", err))
	}
}
