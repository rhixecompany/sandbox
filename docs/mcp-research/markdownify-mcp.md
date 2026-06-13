# Markdownify MCP Server

**Source:** https://github.com/zcaceres/markdownify-mcp

## Project Overview

**Markdownify** is a **Model Context Protocol (MCP) server** that converts various file types and web content to Markdown format. It provides tools to transform PDFs, images, audio files, web pages, YouTube videos, Office documents, and more into easily readable and shareable Markdown text.

- **Repository:** `zcaceres/markdownify-mcp`
- **License:** MIT
- **Commits:** 123
- **MCP Registry:** Listed on [Glama.ai](https://glama.ai/mcp/servers/bn5q4b0ett)

## Features

Converts **10+ content types** to Markdown:
- 📄 PDF files
- 🖼️ Images (with metadata extraction)
- 🎵 Audio files (with transcription)
- 🌐 Web pages
- 🔍 Bing search results
- ▶️ YouTube videos
- 📝 DOCX documents
- 📊 XLSX spreadsheets
- 📽️ PPTX presentations
- 📁 Git repositories (via repomix)
- 📂 Existing Markdown files (retrieval)

## Getting Started

### Prerequisites

- **Bun** (JavaScript runtime)
- **Python** (for `markitdown` via virtual environment)

### Installation

```bash
# Clone repository
git clone https://github.com/zcaceres/markdownify-mcp.git
cd markdownify-mcp

# Install dependencies (creates .venv with markitdown[all])
bun install

# Build the project
bun run build

# Start the server
bun start
```

### Development Mode

```bash
# Run with hot reload
bun run dev

# Key source files:
# - src/server.ts  (MCP server entry point)
# - src/tools.ts   (Tool definitions)
```

## Configuration: Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `MARKITDOWN_PATH` | `<project>/.venv/bin/markitdown` → `markitdown` on PATH | Absolute path to `markitdown` executable. Override if using system-wide install (e.g., `pipx install "markitdown[pdf]"`) |
| `REPOMIX_PATH` | `<project>/node_modules/.bin/repomix` → `repomix` on PATH | Absolute path to `repomix` executable for `git-repo-to-markdown` |
| `MD_ALLOWED_PATHS` | *unset (unrestricted)* | Colon-separated (POSIX) / semicolon-separated (Windows) list of directories the server may read. **Restricts all file-input tools** when set |
| `MD_SHARE_DIR` | *unset* | **Deprecated** alias for `MD_ALLOWED_PATHS` (single directory). Kept for backward compatibility |

### Example: Restrict File Access

```bash
# Only allow reading from /data/in and /data/out
MD_ALLOWED_PATHS=/data/in:/data/out bun start
```

## Docker Usage

```bash
# Build image
docker build -t markdownify .

# Run container
docker run -v /Users/you/Documents:/data markdownify
```

**Docker MCP Catalog:** `mcp/markdownify`

### Important Docker Notes

- Mount host directories to `/data` inside container: `-v /host/path:/data`
- File tools receive paths like `/data/foo.pdf`
- **Requires `markitdown[pdf]`** for PDF support (included in `[all]` extra)
- **Audio/Image tools** need full `[all]` dependencies
- Run `bun install` in Dockerfile to ensure `repomix` is available

## Available Tools (10 Total)

| Tool | Description |
|------|-------------|
| `youtube-to-markdown` | Convert YouTube videos to Markdown |
| `pdf-to-markdown` | Convert PDF files to Markdown |
| `bing-search-to-markdown` | Convert Bing search results to Markdown |
| `webpage-to-markdown` | Convert web pages to Markdown |
| `image-to-markdown` | Convert images to Markdown with metadata |
| `audio-to-markdown` | Convert audio files to Markdown with transcription |
| `docx-to-markdown` | Convert DOCX files to Markdown |
| `xlsx-to-markdown` | Convert XLSX files to Markdown |
| `pptx-to-markdown` | Convert PPTX files to Markdown |
| `get-markdown-file` | Retrieve existing Markdown file (extensions: `.md`, `.markdown`) |

> **Security Note:** All file-input tools (`pdf-to-markdown`, `get-markdown-file`, etc.) respect `MD_ALLOWED_PATHS` restriction when configured.

## Project Structure

```
markdownify-mcp/
├── .github/              # GitHub workflows
├── scripts/              # Utility scripts
├── src/                  # TypeScript source
│   ├── server.ts         # MCP server entry point
│   └── tools.ts          # Tool implementations
├── .dockerignore
├── .gitignore
├── .python-version       # Python version for venv
├── CLAUDE.md             # Claude Code instructions
├── Dockerfile
├── LICENSE               # MIT License
├── README.md
├── bun.lock
├── logo.jpg
├── package.json
├── preinstall.js         # Creates .venv + installs markitdown[all]
├── pyproject.toml        # Python project config
├── setup.bat             # Windows setup script
├── setup.sh              # Unix setup script
├── tsconfig.json
└── uv.lock
```

## Key Technical Details

### Preinstall Process (`preinstall.js`)

- Creates Python virtual environment at `.venv`
- Installs `markitdown[all]` (includes PDF, audio, image, Office support)
- Runs automatically during `bun install`

### Dependencies

- **Runtime:** Bun + Node.js (for `repomix`)
- **Python:** `markitdown[all]` via bundled `.venv`
- **Build:** TypeScript → JavaScript via `bun run build`

## Alternative: Enhanced UTF-8 Version (jdjr2024)

**Source:** https://lobehub.com/es/mcp/jdjr2024-markdownify-mcp-utf8

Enhanced version with:
- Comprehensive UTF-8 encoding support
- Optimized handling of multilingual content
- Optimized memory usage for large file conversions

```bash
# Windows UTF-8 setup
setx PYTHONIOENCODING UTF-8
# or current session
set PYTHONIOENCODING=UTF-8
chcp 65001
```

## Hermes Integration

For Hermes Agent (Bun mode - local):

```yaml
mcp_servers:
  markdownify:
    command: "bun"
    args: ["start"]
    cwd: "C:/path/to/markdownify-mcp"
    env:
      MARKITDOWN_PATH: "C:/path/to/markdownify-mcp/.venv/bin/markitdown"
      MD_ALLOWED_PATHS: "C:/Users/Alexa/Desktop/SandBox"
    tools:
      include: [youtube-to-markdown, pdf-to-markdown, bing-search-to-markdown, webpage-to-markdown, image-to-markdown, audio-to-markdown, docx-to-markdown, xlsx-to-markdown, pptx-to-markdown, get-markdown-file]
```

For Docker mode:

```yaml
mcp_servers:
  markdownify:
    command: "docker"
    args: ["run", "-i", "--rm", "-v", "C:/Users/Alexa/Desktop/SandBox:/data", "mcp/markdownify"]
    tools:
      include: [pdf-to-markdown, webpage-to-markdown, image-to-markdown, docx-to-markdown, xlsx-to-markdown, pptx-to-markdown, get-markdown-file]
```

Then run:
```bash
hermes mcp test markdownify
/reload-mcp
```

## References

- GitHub: https://github.com/zcaceres/markdownify-mcp
- Docker Hub: mcp/markdownify
- Glama.ai: https://glama.ai/mcp/servers/bn5q4b0ett
- explainx.ai: https://explainx.ai/mcp-servers/markdownify-mcp
- MCPCursor: https://mcpcursor.com/server/markdownify-1-mcp
- LobeHub (UTF-8): https://lobehub.com/es/mcp/jdjr2024-markdownify-mcp-utf8
- MarkItDown Library: https://github.com/microsoft/markitdown