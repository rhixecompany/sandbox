package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
)

// FileInfoInput is the input parameters for the file_info tool.
type FileInfoInput struct {
	Path string `json:"path" description:"The file path to inspect"`
}

// FileInfoOutput is the output of the file_info tool.
type FileInfoOutput struct {
	Name    string `json:"name" description:"The base name of the file"`
	Size    int64  `json:"size" description:"The size of the file in bytes"`
	IsDir   bool   `json:"is_dir" description:"Whether the path is a directory"`
	Mode    string `json:"mode" description:"The file permission mode"`
	ModTime string `json:"mod_time" description:"The last modification time as RFC3339 string"`
	Exists  bool   `json:"exists" description:"Whether the file or directory exists"`
}

// FileInfoHandler handles the "file_info" tool call.
func FileInfoHandler(ctx context.Context, args json.RawMessage) (json.RawMessage, error) {
	var input FileInfoInput
	if err := json.Unmarshal(args, &input); err != nil {
		return nil, fmt.Errorf("invalid arguments: %w", err)
	}
	if input.Path == "" {
		return nil, fmt.Errorf("path is required")
	}

	output := FileInfoOutput{Exists: false}

	info, err := os.Stat(input.Path)
	if err != nil {
		if os.IsNotExist(err) {
			output.Name = input.Path
			result, marshalErr := json.Marshal(output)
			if marshalErr != nil {
				return nil, fmt.Errorf("failed to marshal output: %w", marshalErr)
			}
			return result, nil
		}
		return nil, fmt.Errorf("failed to stat file: %w", err)
	}

	output.Name = info.Name()
	output.Size = info.Size()
	output.IsDir = info.IsDir()
	output.Mode = info.Mode().String()
	output.ModTime = info.ModTime().Format("2006-01-02T15:04:05Z07:00")
	output.Exists = true

	result, err := json.Marshal(output)
	if err != nil {
		return nil, fmt.Errorf("failed to marshal output: %w", err)
	}
	return result, nil
}

// FileInfoToolDefinition returns the ToolDefinition for the file_info tool.
func FileInfoToolDefinition() ToolDefinition {
	return ToolDefinition{
		Name:        "file_info",
		Description: "Get metadata about a file or directory on the local filesystem",
		InputSchema: map[string]interface{}{
			"type": "object",
			"properties": map[string]interface{}{
				"path": map[string]interface{}{
					"type":        "string",
					"description": "The file path to inspect",
				},
			},
			"required": []string{"path"},
		},
		Handler: FileInfoHandler,
	}
}
