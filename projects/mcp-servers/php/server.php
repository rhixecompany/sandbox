<?php

/**
 * PHP MCP Server — stdio entry point.
 *
 * Reads JSON-RPC messages from stdin and writes responses to stdout,
 * implementing the Model Context Protocol.
 */

require __DIR__ . '/vendor/autoload.php';

use McpServer\Tools\GreetTool;
use McpServer\Tools\FileInfoTool;

// ──────────────────────────────────────────────
// 1. Create the MCP server
// ──────────────────────────────────────────────

$server = new \MCP\Server\Server('php-mcp-server', '1.0.0');

// ──────────────────────────────────────────────
// 2. Register tools
// ──────────────────────────────────────────────

$greetTool    = new GreetTool();
$fileInfoTool = new FileInfoTool();

$server->registerTool($greetTool);
$server->registerTool($fileInfoTool);

// ──────────────────────────────────────────────
// 3. Attach stdio transport and run
// ──────────────────────────────────────────────

$transport = new \MCP\Server\Transport\StdioTransport();

$server->setTransport($transport);
$server->run();
