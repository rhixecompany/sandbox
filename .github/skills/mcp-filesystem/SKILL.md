---
name: mcp-filesystem
title: MCP Filesystem — File & Directory Operations
description: Exposes all filesystem MCP tools for reading, writing, editing, moving, and listing files and directories. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - filesystem
  - file-ops
  - directory
---
# MCP Filesystem

Provides secure file system access via the standard `@modelcontextprotocol/server-filesystem`. All operations are restricted to allowed directories (configured as `C:/Users/Alexa`).

## Overview

Automated reasoning and workflow tool for `mcp-filesystem`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `filesystem` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @modelcontextprotocol/server-filesystem C:/Users/Alexa`

## Tools

| Tool | Description |
|------|-------------|
| `list_allowed_directories` | List directories the server can access |
| `read_text_file` | Read file as text (with optional head/tail) |
| `read_multiple_files` | Read multiple files simultaneously |
| `read_media_file` | Read image/audio file (base64-encoded) |
| `write_file` | Create or overwrite a file |
| `edit_file` | Line-based find/replace edits |
| `create_directory` | Create nested directories |
| `list_directory` | List files/dirs with `[FILE]`/`[DIR]` prefixes |
| `list_directory_with_sizes` | List with file sizes |
| `move_file` | Move or rename files/dirs |
| `get_file_info` | Get metadata (size, timestamps, permissions) |

## Workflow

### Phase 1: Verify

```
hermes mcp test filesystem
```

### Phase 2: Use Tools

**Read operations:**
```
list_allowed_directories()
read_text_file(path: "C:/Users/Alexa/test.txt", head: 20)
read_multiple_files(paths: ["a.txt", "b.txt"])
get_file_info(path: "C:/Users/Alexa/file.txt")
```

**Directory operations:**
```
list_directory(path: "C:/Users/Alexa/Desktop")
list_directory_with_sizes(path: "C:/Users/Alexa/project")
create_directory(path: "C:/Users/Alexa/test-dir")
```

**Write operations (⚠️ destructive):**
```
write_file(path: "C:/Users/Alexa/test.txt", content: "hello")
edit_file(path: "C:/Users/Alexa/test.txt", edits: [{oldText: "hello", newText: "world"}])
move_file(source: "C:/Users/Alexa/a.txt", destination: "C:/Users/Alexa/b.txt")
```

### Phase 3: Test Cases

```bash
# 1. Connectivity
hermes mcp test filesystem

# 2. List allowed dirs
# Call: mcp_filesystem_list_allowed_directories()

# 3. List directory
# Call: mcp_filesystem_list_directory(path="C:/Users/Alexa/Desktop")

# 4. Get file info (use any known file)
# Call: mcp_filesystem_get_file_info(path="C:/Users/Alexa/.bashrc")

# 5. Read file
# Call: mcp_filesystem_read_text_file(path="C:/Users/Alexa/.bashrc", head: 5)

# 6. Read multiple files (if multiple known files exist)
# Call: mcp_filesystem_read_multiple_files(paths=["C:/Users/Alexa/.bashrc", "C:/Users/Alexa/.gitconfig"])
```

## Best Practices

1. **Prefer `read_text_file`** over deprecated `read_file` — same result, clearer API
2. **Use `head`/`tail` params** for large files — avoid flooding context
3. **`read_multiple_files`** is more efficient than sequential single reads for independent files
4. **Check `list_allowed_directories` first** — confirms what's accessible before other operations
5. **`write_file` overwrites without warning** — use `edit_file` for surgical changes when possible
6. **`create_directory` is idempotent** — safe to call even if directory exists
7. **`get_file_info` before operations** — confirms path, size, and type

## Pitfalls

- `write_file` **silently overwrites** existing files — no confirmation prompt
- All operations are scoped to the allowed directory (`C:/Users/Alexa`) — files outside fail
- `read_file` is deprecated — use `read_text_file` instead
- File paths use forward slashes or escaped backslashes; raw `C:\...` may fail
- Media files are returned as base64 — large files may exceed token limits
- `move_file` fails if destination already exists (no overwrite)
- Line numbers in `edit_file` are **1-indexed** content lines, not byte offsets

## Verification Checklist

- [ ] `hermes mcp test filesystem` passes
- [ ] `list_allowed_directories` returns the configured root
- [ ] `list_directory` returns entries for a known path
- [ ] `get_file_info` returns metadata for a known file
- [ ] `read_text_file` returns file content

## When to Use


- When you need to perform MCP Filesystem — File & Directory Operations operations or tasks
- When managing MCP Filesystem — File & Directory Operations infrastructure or configurations
- When automating or debugging MCP Filesystem — File & Directory Operations workflows
- **Triggers**: "mcp filesystem — file & directory operations" required for a project
