// Package config provides environment-based configuration for the MCP server.
package config

import (
	"fmt"
	"os"
	"strconv"
)

// Config holds all server configuration values.
type Config struct {
	// ServerName is the name advertised by the MCP server.
	ServerName string

	// ServerVersion is the version of the MCP server.
	ServerVersion string

	// LogLevel controls the verbosity of logging.
	LogLevel string

	// MaxToolResults caps the number of results returned by tools.
	MaxToolResults int
}

// Default returns a Config populated with sensible defaults.
func Default() Config {
	return Config{
		ServerName:     "go-mcp-server",
		ServerVersion:  "1.0.0",
		LogLevel:       "info",
		MaxToolResults: 100,
	}
}

// FromEnv overlays environment variables on top of a base Config.
func FromEnv(base Config) Config {
	if v := os.Getenv("MCP_SERVER_NAME"); v != "" {
		base.ServerName = v
	}
	if v := os.Getenv("MCP_SERVER_VERSION"); v != "" {
		base.ServerVersion = v
	}
	if v := os.Getenv("MCP_LOG_LEVEL"); v != "" {
		base.LogLevel = v
	}
	if v := os.Getenv("MCP_MAX_TOOL_RESULTS"); v != "" {
		if n, err := strconv.Atoi(v); err == nil && n > 0 {
			base.MaxToolResults = n
		}
	}
	return base
}

// String returns a human-readable representation of the config.
func (c Config) String() string {
	return fmt.Sprintf(
		"ServerName=%s, ServerVersion=%s, LogLevel=%s, MaxToolResults=%d",
		c.ServerName, c.ServerVersion, c.LogLevel, c.MaxToolResults,
	)
}
