<?php

namespace McpServer\Tools;

use MCP\Server\Tool\BaseTool;
use MCP\Server\Tool\Attribute\ToolParameter;

/**
 * FileInfoTool — returns metadata about a given file path.
 *
 * Parameters:
 *   path (string, required) — absolute or relative file path.
 */
class FileInfoTool extends BaseTool
{
    public function __construct()
    {
        parent::__construct(
            name: 'file_info',
            description: 'Return metadata (size, permissions, timestamps) for a file.',
            parameters: [
                new ToolParameter(
                    name: 'path',
                    type: 'string',
                    description: 'Absolute or relative path to the file',
                    required: true,
                ),
            ],
        );
    }

    /**
     * Execute the file_info tool.
     *
     * @param  array<string, mixed>  $arguments
     * @return string  JSON-encoded file metadata.
     */
    public function execute(array $arguments): string
    {
        $path = $arguments['path'];

        if (! file_exists($path)) {
            return json_encode([
                'error' => "File not found: {$path}",
            ]);
        }

        $stat = stat($path);

        return json_encode([
            'path'         => realpath($path) ?: $path,
            'size'         => $stat['size'],
            'permissions'  => substr(sprintf('%o', fileperms($path)), -4),
            'type'         => filetype($path),
            'is_readable'  => is_readable($path),
            'is_writable'  => is_writable($path),
            'modified_at'  => date('c', $stat['mtime']),
            'accessed_at'  => date('c', $stat['atime']),
            'created_at'   => date('c', $stat['ctime']),
        ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    }
}
