# YouTube Transcript MCP Server

**Source:** https://github.com/kyong0612/youtube-mcp

## Overview

**Repository:** `kyong0612/youtube-mcp`
**Description:** A high-performance Model Context Protocol (MCP) server for fetching YouTube video transcripts, implemented in Go.

## Features (MCP Tools)

| Tool | Description |
|------|-------------|
| `get_transcript` | Fetch transcript for a single YouTube video |
| `get_multiple_transcripts` | Fetch transcripts for multiple videos |
| `translate_transcript` | Translate transcript to target language |
| `format_transcript` | Format transcript output (JSON, text, SRT, VTT) |
| `list_available_languages` | List available transcript languages for a video |

## Requirements

- **Go** 1.21+ (for building from source)
- **Docker** (for containerized deployment)
- **Redis** (optional, for caching)

## MCP Client Setup

### Quick Install (Recommended)

```bash
# Automatic installation script
curl -fsSL https://raw.githubusercontent.com/kyong0612/youtube-mcp/main/scripts/install.sh | bash
```

**The installer will:**
- Download the appropriate binary for your platform
- Install to `/usr/local/bin` (or `~/.local/bin` if no sudo)
- Create example configuration files

### Install via Go Install

```bash
go install github.com/kyong0612/youtube-mcp/cmd/youtube-mcp-stdio@latest
```

> **Note:** If installed to `$GOPATH/bin`, ensure it's in your PATH, or use the full path in the command field.

### Manual Setup - Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "youtube-mcp-stdio",
      "args": [],
      "env": {
        "YOUTUBE_DEFAULT_LANGUAGES": "en,ko,ja",
        "CACHE_TYPE": "memory",
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

> **Important:** Claude Desktop requires the **stdio version** (`youtube-mcp-stdio`), not the HTTP server.

**Build the stdio server:**
```bash
make build-stdio
```

### Other Clients

- **Claude Code** (`claude.ai/code`): Auto-detects MCP servers, same config as Claude Desktop
- **Cursor**: Configure via Settings (`Cmd+,` / `Ctrl+,`) → MCP Servers
- **Detailed setup:** See [`docs/mcp-client-setup.md`](docs/mcp-client-setup.md)

## Installation

### Using Go

```bash
# Clone and build
git clone https://github.com/kyong0612/youtube-mcp.git
cd youtube-mcp
make build
```

### Using Docker

```bash
# Pull and run
docker pull ghcr.io/kyong0612/youtube-mcp:latest
docker run -p 8080:8080 ghcr.io/kyong0612/youtube-mcp:latest
```

## Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

### Key Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | HTTP server port | `8080` |
| `YOUTUBE_DEFAULT_LANGUAGES` | Comma-separated preferred languages | `en` |
| `CACHE_TYPE` | Cache backend: `memory`, `redis`, `none` | `memory` |
| `SECURITY_ENABLE_AUTH` | Enable API key authentication | `false` |
| `LOG_LEVEL` | Log level: `debug`, `info`, `warn`, `error` | `info` |
| `REDIS_ADDR` | Redis address (if using Redis cache) | `localhost:6379` |
| `CACHE_TTL` | Cache TTL in seconds | `3600` |

## Usage

### With MCP Clients (Claude Desktop, Cursor, etc.)

The MCP server starts automatically when configured. Use tools directly in conversations:

```
User: "Get the transcript for https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Assistant: [Calls get_transcript tool]
```

### As HTTP Server (Development/Testing)

```bash
# Start HTTP server
make run

# Or directly
./youtube-mcp
```

**Test endpoints:**

```bash
# List available tools
curl http://localhost:8080/mcp/tools

# Get transcript
curl -X POST http://localhost:8080/mcp/tools/get_transcript \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "languages": ["en"]}'

# Get multiple transcripts
curl -X POST http://localhost:8080/mcp/tools/get_multiple_transcripts \
  -H "Content-Type: application/json" \
  -d '{"video_ids": ["dQw4w9WgXcQ", "jNQXAC9IVRw"]}'
```

## Development

### Running Tests

```bash
# All tests
make test

# With coverage
make test-coverage

# Integration tests
make test-integration
```

### Code Quality

```bash
# Linting
make lint

# Format code
make fmt

# Security scan
make security
```

### Hot Reload Development

```bash
# Requires air (installed via Makefile.tools)
make dev
```

## Docker Deployment

### Basic Deployment

```bash
docker-compose up -d
```

### With Redis Cache

```yaml
# docker-compose.yml
services:
  youtube-mcp:
    image: ghcr.io/kyong0612/youtube-mcp:latest
    environment:
      - CACHE_TYPE=redis
      - REDIS_ADDR=redis:6379
    depends_on:
      - redis
  
  redis:
    image: redis:7-alpine
```

### With Monitoring (Prometheus + Grafana)

```bash
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d
```

## Monitoring

### Health Check

```bash
curl http://localhost:8080/health
# Response: {"status": "healthy"}
```

## Hermes Integration

For Hermes Agent (stdio binary mode):

```yaml
mcp_servers:
  youtube-transcript:
    command: "youtube-mcp-stdio"
    args: []
    env:
      YOUTUBE_DEFAULT_LANGUAGES: "en,ko,ja"
      CACHE_TYPE: "memory"
      LOG_LEVEL: "info"
    tools:
      include: [get_transcript, get_multiple_transcripts, translate_transcript, format_transcript, list_available_languages]
```

For Docker STDIO mode:
```yaml
mcp_servers:
  youtube-transcript:
    command: "docker"
    args: ["run", "-i", "--rm", "ghcr.io/kyong0612/youtube-mcp:latest", "stdio"]
    env:
      YOUTUBE_DEFAULT_LANGUAGES: "en,ko,ja"
    tools:
      include: [get_transcript, get_multiple_transcripts]
```

Then run:
```bash
hermes mcp test youtube-transcript
/reload-mcp
```

## References

- GitHub: https://github.com/kyong0612/youtube-mcp
- Docker: ghcr.io/kyong0612/youtube-mcp:latest
- mcpservers.org: https://mcpservers.org/servers/kyong0612/youtube-mcp
- mcpserverfinder.com: https://www.mcpserverfinder.com/servers/jkawamoto/mcp-youtube-transcript
- LobeHub: https://lobehub.com/mcp/sinco-lab-mcp-youtube-transcript