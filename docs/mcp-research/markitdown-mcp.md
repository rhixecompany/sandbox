# MarkItDown MCP Server

**Source:** https://github.com/trsdn/markitdown-mcp

## Overview

**Repository:** [trsdn/markitdown-mcp](https://github.com/trsdn/markitdown-mcp)
**Description:** Professional MCP server for converting 29+ file formats to clean, structured Markdown - Perfect for Claude Desktop and AI workflows!
**License:** MIT
**Language:** Python 3.10+
**Protocol:** Model Context Protocol (MCP)

## Key Features

| Feature | Description |
|---------|-------------|
| **29+ Formats** | PDF, Office docs, images, audio, web, books, archives, text |
| **MCP Native** | Three tools: `convert_file`, `list_supported_formats`, `convert_directory` |
| **Claude Desktop Ready** | One-command install + config |
| **Batch Processing** | Convert entire directories |
| **Metadata Extraction** | EXIF from images, speech-to-text from audio |
| **Archive Support** | Auto-extract and process `.zip` files |

## Supported File Formats (29+)

| Category | Extensions | Key Features |
|----------|------------|--------------|
| **📊 Office** | `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls` | Full document structure preservation |
| **🖼️ Images** | `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp` | EXIF metadata extraction |
| **🎵 Audio** | `.mp3`, `.wav` | Speech-to-text transcription |
| **🌐 Web** | `.html`, `.htm`, `.xml`, `.json`, `.csv` | Clean formatting |
| **📚 Books** | `.epub` | Chapter extraction |
| **📦 Archives** | `.zip` | Auto-extract and process contents |
| **📝 Text** | `.txt`, `.md`, `.rst` | Direct conversion |

## Installation

### 🚀 One-Command Install (Recommended - All Features)

```bash
pipx install markitdown-mcp && pipx inject markitdown-mcp 'markitdown[all]'
```

### Quick Install (Basic Features Only)

```bash
pipx install markitdown-mcp
```

### Complete Install with All Dependencies (Step by Step)

#### Method 1: Using pipx (Recommended)

```bash
pipx install markitdown-mcp
pipx inject markitdown-mcp 'markitdown[all]'
```

#### Method 2: Using pip with Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install markitdown-mcp
pip install 'markitdown[all]'
```

#### Method 3: For Existing Claude Desktop Installation

```bash
pipx inject markitdown-mcp 'markitdown[all]'
```

### Verify Installation

```bash
markitdown-mcp --help
# or
python -m markitdown_mcp --help
```

## Dependency Requirements by File Type

| File Type | Required Dependencies | Install Command |
|-----------|----------------------|-----------------|
| **PDF** | `pypdf`, `pymupdf`, `pdfplumber` | `pipx inject markitdown-mcp 'markitdown[all]'` |
| **Excel (.xlsx, .xls)** | `openpyxl`, `xlrd`, `pandas` | `pipx inject markitdown-mcp openpyxl xlrd pandas` |
| **PowerPoint (.pptx)** | `python-pptx` | Included in base install |
| **Images** | `PIL`, `exiftool` (optional) | Included in base install |
| **Audio** | `pydub`, `speech_recognition` | `pipx inject markitdown-mcp 'markitdown[all]'` |
| **Basic formats** | None | Base install only |

> **Note:** For the best experience, install all dependencies using the **Complete Install** method above.

## Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "markitdown-mcp",
      "args": []
    }
  }
}
```

### Config File Locations

| OS | Path |
|----|------|
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |

> **Important:** Restart Claude Desktop after adding the configuration.

## Available MCP Tools

### 1. `convert_file`

Convert a single file to Markdown.

**Parameters:**
- `file_path` (string, required): Path to the file to convert
- `output_path` (string, optional): Output file path (defaults to same name with .md extension)

### 2. `list_supported_formats`

Get a complete list of supported file formats with categories.

**Parameters:** None

### 3. `convert_directory`

Convert all supported files in a directory.

**Parameters:**
- `input_dir` (string, required): Input directory path
- `output_dir` (string, optional): Output directory (defaults to `input_dir + "_markdown"`)
- `recursive` (boolean, optional): Process subdirectories (default: `true`)

## Usage Examples

### Convert a PDF

> **User:** "Convert the file `~/Documents/report.pdf` to markdown"

### Batch Process Directory

> **User:** "Convert all files in `~/Downloads/documents/` to markdown"

### Check Supported Formats

> **User:** "What file formats can you convert to markdown?"

## Troubleshooting

### Missing Dependencies Errors

| Error | Solution |
|-------|----------|
| `PdfConverter threw MissingDependencyException` for .pdf | `pipx inject markitdown-mcp 'markitdown[all]'` |
| `DocxConverter threw MissingDependencyException` for .docx | `pipx inject markitdown-mcp 'markitdown[all]'` |
| `XlsxConverter threw MissingDependencyException` for .xlsx | `pipx inject markitdown-mcp openpyxl xlrd pandas` |
| `AudioConverter threw MissingDependencyException` for .mp3/.wav | `pipx inject markitdown-mcp 'markitdown[all]'` |

## Docker Usage

```bash
# Build image
docker build -t markitdown-mcp .

# Run (read-only)
docker run -it --rm markitdown-mcp:latest

# Run with volume mount
docker run -it --rm -v /home/user/data:/workdir markitdown-mcp:latest
```

**Claude Desktop Docker config:**
```json
{
  "mcpServers": {
    "markitdown": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "markitdown-mcp:latest"]
    }
  }
}
```

With volume mount:
```json
{
  "mcpServers": {
    "markitdown": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "-v", "/home/user/data:/workdir", "markitdown-mcp:latest"]
    }
  }
}
```

## Hermes Integration

For Hermes Agent (pipx installed):

```yaml
mcp_servers:
  markitdown:
    command: "markitdown-mcp"
    args: []
    tools:
      include: [convert_file, list_supported_formats, convert_directory]
```

For Docker mode:

```yaml
mcp_servers:
  markitdown:
    command: "docker"
    args: ["run", "--rm", "-i", "markitdown-mcp:latest"]
    tools:
      include: [convert_file, list_supported_formats, convert_directory]
```

For Docker with volume mount:

```yaml
mcp_servers:
  markitdown:
    command: "docker"
    args: ["run", "--rm", "-i", "-v", "C:/Users/Alexa/Desktop/SandBox:/workdir", "markitdown-mcp:latest"]
    tools:
      include: [convert_file, list_supported_formats, convert_directory]
```

Then run:
```bash
hermes mcp test markitdown
/reload-mcp
```

## References

- GitHub: https://github.com/trsdn/markitdown-mcp
- LobeHub (IT): https://lobehub.com/it/mcp/trsdn-markitdown-mcp
- mdskills.ai: https://www.mdskills.ai/skills/markitdown
- PulseMCP: https://www.pulsemcp.com/servers/markitdown
- Microsoft MarkItDown: https://github.com/microsoft/markitdown (139k stars)