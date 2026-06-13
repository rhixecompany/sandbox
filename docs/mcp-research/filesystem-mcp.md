# Filesystem MCP Server

**Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

## Overview

Node.js server implementing Model Context Protocol (MCP) for filesystem operations.
**Repository:** `modelcontextprotocol/servers/src/filesystem` | **License:** MIT

## Project Structure

```
src/filesystem/
├── __tests__/           # Test files
├── Dockerfile           # Container configuration
├── README.md            # Documentation
├── index.ts             # Main entry point
├── lib.ts               # Core library
├── package.json         # Dependencies & scripts
├── path-utils.ts        # Path utilities
├── path-validation.ts   # Path validation logic
├── roots-utils.ts       # Roots protocol utilities
├── tsconfig.json        # TypeScript config
└── vitest.config.ts     # Test configuration
```

## Directory Access Control

The server uses a **flexible directory access control system** with two methods:

### Method 1: Command-Line Arguments (Static)

```bash
# Specify allowed directories at startup
npx @modelcontextprotocol/server-filesystem /path/to/allowed/dir1 /path/to/allowed/dir2
```

### Method 2: MCP Roots (Recommended) 🌟

- **Dynamic runtime updates** via `roots/list_changed` notifications
- **No server restart required** for directory changes
- Roots **completely replace** any server-side allowed directories when provided
- **Error if:** Server starts without args AND client doesn't support roots (or provides empty roots)

### Access Control Flow

```
Server Startup → Client Connection (initialize + capabilities.roots)
    ↓
Roots Protocol (if supported): roots/list → notifications/roots/list_changed
    ↓
Fallback (if no roots): Command-line args only
    ↓
Access Control: list_allowed_directories
```

> **Key Rule:** Operations only allowed within directories specified via `args` **or** Roots.

## API Tools

### Read Operations (readOnlyHint: true)

| Tool | Parameters | Description |
|------|------------|-------------|
| `read_text_file` | `path`, `head?`, `tail?` | Read text file with optional line limits |
| `read_media_file` | `path` | Read binary/media files |
| `read_multiple_files` | `paths[]` | Batch read multiple files |
| `list_directory` | `path` | List directory contents |
| `list_directory_with_sizes` | `path`, `sortBy?` | List with file sizes |
| `directory_tree` | `path`, `excludePatterns?` | Recursive tree: `{name, type, children[]}` |
| `search_files` | `path`, `pattern`, `excludePatterns?` | Glob pattern search |
| `get_file_info` | `path` | File metadata (size, dates, permissions) |
| `list_allowed_directories` | — | Returns currently allowed directories |

### Write Operations (readOnlyHint: false)

| Tool | Parameters | Idempotent | Destructive | Notes |
|------|------------|------------|-------------|-------|
| `create_directory` | `path` | ✅ | ❌ | Re-creating same dir = no-op |
| `write_file` | `path`, `content` | ✅ | ✅ | **Overwrites** existing files |
| `edit_file` | `path`, `edits[]`, `dryRun?` | ❌ | ✅ | Re-applying may fail/double-apply |
| `move_file` | `source`, `destination` | ❌ | ✅ | **Deletes source** file |

> **MCP ToolAnnotations:** Clients use these hints for safety (confirmations, undo, etc.)

## Installation & Usage

### With Claude Desktop

**Docker (Recommended for isolation)**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "--mount", "type=bind,src=/host/path,dst=/projects,ro",
        "mcp/filesystem", "/projects"
      ]
    }
  }
}
```

- Mount directories to `/projects` (add `ro` for read-only)

**NPX**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    }
  }
}
```

- **Windows:** Use `cmd /c npx ...`

### With VS Code

#### Quick Install Buttons

| Method | VS Code | VS Code Insiders |
|--------|---------|------------------|
| **NPX** | [![Install](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-filesystem%22%2C%22%24%7BworkspaceFolder%7D%22%5D%7D) | [![Install](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-filesystem%22%2C%22%24%7BworkspaceFolder%7D%22%5D%7D&quality=insiders) |
| **Docker** | [![Install](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22--mount%22%2C%22type%3Dbind%2Csrc%3D%24%7BworkspaceFolder%7D%2Cdst%3D%2Fprojects%22%5D%7D) | [![Install](https://img.shields.io/badge/VS_Code_Insiders-Docker-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22--mount%22%2C%22type%3Dbind%2Csrc%3D%24%7BworkspaceFolder%7D%2Cdst%3D%2Fprojects%22%5D%7D&quality=insiders) |

## Alternative Filesystem Implementations

### 1. Go Implementation (mark3labs/mcp-filesystem-server)

**Source:** https://github.com/mark3labs/mcp-filesystem-server

```bash
git clone https://github.com/mark3labs/mcp-filesystem-server.git
go install ./cmd/mcp-fs-server@latest
```

**Config (config.yaml):**
```yaml
listen: ":8000"
rootDir: "/var/mcp-data"
token: "<your-bearer-token>"
```

```bash
mcp-fs-server --config ./config.yaml
```

**Docker:**
```bash
docker build -t mark3labs/mcp-fs-server .
docker run -d -p 8000:8000 -v $PWD/data:/var/mcp-data mark3labs/mcp-fs-server
```

### 2. Java Implementation (brunorozendo/mcp-server-filesystem)

**Source:** LobeHub listing

```bash
# Build fat JAR
./gradlew shadowJar
# Or download pre-built JAR

java -jar build/libs/filesystem-mcp-server-all.jar /path/to/allowed/directory [additional directories...]
```

## Hermes Integration

For Hermes Agent (NPX mode with workspace):

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "C:/Users/Alexa/Desktop/SandBox"]
    tools:
      include: [read_text_file, write_file, edit_file, list_directory, search_files, directory_tree, get_file_info, list_allowed_directories]
```

For Docker mode (read-only):

```yaml
mcp_servers:
  filesystem:
    command: "docker"
    args: ["run", "-i", "--rm", "--mount", "type=bind,src=C:/Users/Alexa/Desktop/SandBox,dst=/projects,ro", "mcp/filesystem", "/projects"]
    tools:
      include: [read_text_file, list_directory, search_files, directory_tree, get_file_info, list_allowed_directories]
```

Then run:
```bash
hermes mcp test filesystem
/reload-mcp
```

## References

- GitHub (Official): https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Go Implementation: https://github.com/mark3labs/mcp-filesystem-server
- Augment Code: https://www.augmentcode.com/mcp/mcp-filesystem-server
- LobeHub (Java): https://lobehub.com/mcp/brunorozendo-mcp-server-filesystem