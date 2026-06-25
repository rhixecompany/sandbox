# php-mcp-server

A PHP implementation of a **Model Context Protocol (MCP)** server using stdio transport.

## Requirements

- PHP 8.2 or later
- [Composer](https://getcomposer.org/)

## Setup

```bash
# 1. Install dependencies
composer install

# 2. Start the server
php server.php
```

The server reads JSON-RPC messages from **stdin** and writes responses to **stdout**, as required by the MCP stdio transport.

## Available Tools

### greet

Generate a personalised greeting message.

| Parameter | Type   | Required | Default     | Description                           |
|-----------|--------|----------|-------------|---------------------------------------|
| `name`    | string | yes      | —           | The name of the person to greet       |
| `style`   | string | no       | `friendly`  | One of: `friendly`, `formal`, `shout` |

### file_info

Return metadata (size, permissions, timestamps) for a file.

| Parameter | Type   | Required | Description                      |
|-----------|--------|----------|----------------------------------|
| `path`    | string | yes      | Absolute or relative file path   |

## Project Structure

```
php-mcp-server/
├── composer.json           # Dependencies & autoload config
├── server.php              # Stdio entry point
├── src/
│   └── Tools/
│       ├── GreetTool.php   # Greeting tool
│       └── FileInfoTool.php# File-info tool
└── README.md               # This file
```

## License

MIT
