# YouTube Transcript MCP Server

**Source:** https://github.com/kyong0612/youtube-mcp

## Overview
A high-performance **Model Context Protocol (MCP) server** for fetching YouTube video transcripts, implemented in **Go**. Enables AI assistants like Claude Desktop and Cursor to retrieve and process YouTube video content.

---

## 🚀 Key Features

- **`get_transcript`** – Fetch transcript for a single video
- **`get_multiple_transcripts`** – Batch fetch transcripts
- **`translate_transcript`** – Translate transcripts to other languages
- **`format_transcript`** – Format raw transcript data
- **`list_available_languages`** – List available transcript languages for a video

---

## 🎯 MCP Client Setup

### Quick Install (Recommended)
Use the automatic installation script (details in repo).

### Install via Go
```bash
go install
```
> **Note**: Ensure `$GOPATH/bin` is in your PATH or use the full binary path in client config.

### Manual Setup

#### Claude Desktop
Add to `claude_desktop_config.json`:
> ⚠️ **Important**: Claude Desktop requires the **stdio version** (`youtube-mcp-stdio`), not the HTTP server.

Build the stdio server:
```bash
# Build youtube-mcp-stdio binary
```

#### Claude Code
Automatically detects MCP servers; use same config as Claude Desktop.

#### Cursor
Configure via settings (`Cmd+,` / `Ctrl+,`). See [docs/mcp-client-setup.md](https://github.com/kyong0612/youtube-mcp/blob/main/docs/mcp-client-setup.md) for details.

---

## 🛠️ Installation

### Using Go
```bash
go build
```

### Using Docker
```bash
docker build -t youtube-mcp .
```

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and configure:

| Variable | Purpose |
|----------|---------|
| `PORT` | HTTP server port |
| `YOUTUBE_DEFAULT_LANGUAGES` | Default transcript languages |
| `CACHE_TYPE` | Cache backend (e.g., Redis) |
| `SECURITY_ENABLE_AUTH` | Enable authentication |
| `LOG_LEVEL` | Logging verbosity |

---

## 🔧 Usage

### With MCP Clients (Claude Desktop, Cursor, etc.)
Server starts automatically via client config. Use tools directly in conversations.

### As HTTP Server (Development/Testing)
```bash
# Run HTTP server
# Then test with curl or similar
```

---

## 🧪 Development

### Running Tests
```bash
make test
```

### Code Quality
Linting and formatting via configured tools (`.golangci.yml`, `.revive.toml`).

### Hot Reload
Uses `.air.toml` for live-reload during development.

---

## 🐳 Docker Deployment

- **Basic**: Standard Docker build
- **With Redis Cache**: For improved performance
- **With Monitoring**: Includes health/metrics endpoints

---

## 📊 Monitoring

- **Health Check**: Verify server status
- **Readiness Check**: Confirm server can serve requests
- **Metrics**: Performance and usage data

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Empty transcript response" | Ensure using `youtube-mcp-stdio` (not `youtube-transcript-mcp`) |
| "Request timed out" | Enable debug logging: `LOG_LEVEL=debug` |
| "Failed to extract player response" | Check network/Youtube API changes |
| Server not connecting to Claude Desktop | Verify binary path: `ls -la /path/to/youtube-mcp-stdio` |

---

## 🔒 Security

Enable authentication:
```env
SECURITY_ENABLE_AUTH=true
```

---

## 🤝 Contributing

Standard GitHub workflow:
```bash
git checkout -b feature/amazing-feature
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature
```

---

## 📝 License

**MIT License** – See [LICENSE](https://github.com/kyong0612/youtube-mcp/blob/main/LICENSE)

---

## ⚠️ Disclaimer

For **educational and research purposes only**. Respect YouTube's Terms of Service and copyright laws.

---

## Repository Info

- **Language**: Go
- **Releases**: 1
- **Packages**: 0
- **License**: MIT
