# ast-grep MCP Server

**Source:** <https://github.com/ast-grep/ast-grep-mcp>

## Overview

**Repository:** `ast-grep/ast-grep-mcp`
**Purpose:** Experimental Model Context Protocol (MCP) server providing AI assistants with structural code search capabilities using [ast-grep](https://ast-grep.github.io/)
**Key Value:** Enables AST pattern matching instead of simple text-based search for codebase analysis

## Prerequisites

| Requirement    | Details                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------- |
| **ast-grep**   | Follow [installation guide](https://ast-grep.github.io/guide/quick-start.html#installation) |
| **uv**         | Python package manager                                                                      |
| **MCP Client** | Cursor, Claude Desktop, or other MCP-compatible clients                                     |

## Installation

```bash
# Clone repository
git clone https://github.com/ast-grep/ast-grep-mcp.git
cd ast-grep-mcp

# Install dependencies
uv sync

# Verify ast-grep installation
ast-grep --version
```

### Quick Run with `uvx` (No Clone Required)

```bash
# Run directly from GitHub
uvx --from git+https://github.com/ast-grep/ast-grep-mcp.git ast-grep-mcp
```

## Configuration

### For Cursor (`.cursor-mcp/settings.json`)

```json
{
	"mcpServers": {
		"ast-grep": {
			"command": "uvx",
			"args": [
				"--from",
				"git+https://github.com/ast-grep/ast-grep-mcp.git",
				"ast-grep-mcp"
			]
		}
	}
}
```

### For Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"ast-grep": {
			"command": "uvx",
			"args": [
				"--from",
				"git+https://github.com/ast-grep/ast-grep-mcp.git",
				"ast-grep-mcp"
			]
		}
	}
}
```

### Custom ast-grep Configuration (`sgconfig.yaml`)

The server supports custom ast-grep configuration via `sgconfig.yaml` (see [ast-grep config docs](https://ast-grep.github.io/guide/project/project-config.html)).

**Precedence order:**

1. CLI flag: `--config /path/to/sgconfig.yaml`
2. Environment variable: `AST_GREP_CONFIG=/path/to/sgconfig.yaml`

## Core Tools (4 Main Functions)

### 1. `dump_syntax_tree`

Visualize AST structure of code snippets — essential for writing effective search patterns.

**Use cases:**

- Understanding code structure before writing patterns
- Debugging why a pattern doesn't match
- Learning ast-grep's node types for specific languages

### 2. `test_match_code_rule`

Test ast-grep YAML rules against code snippets before applying to larger codebases.

**Use cases:**

- Validating rule correctness
- Iterative rule development
- Preventing false positives/negatives

### 3. `find_code`

Search codebases using simple ast-grep patterns for straightforward structural matches.

**Parameters:**

| Parameter       | Type                 | Default  | Description                                |
| --------------- | -------------------- | -------- | ------------------------------------------ |
| `pattern`       | string               | required | ast-grep pattern to search                 |
| `language`      | string               | optional | Target language (auto-detected if omitted) |
| `path`          | string               | `.`      | Directory to search                        |
| `max_results`   | integer              | 100      | Maximum matches to return                  |
| `output_format` | `"text"` \| `"json"` | `"text"` | Output format                              |

**Text Output Example:**

```
Found 2 matches:
path/to/file.py:10-15
def example_function():
    # function body
    return result
path/to/file.py:20-22
def another_function():
    pass
```

**Use cases:**

- Quick pattern searches
- Finding specific code constructs
- Simple structural queries

### 4. `find_code_by_rule`

Advanced search using complex YAML rules with sophisticated matching criteria.

**Parameters:**

| Parameter       | Type                 | Default  | Description               |
| --------------- | -------------------- | -------- | ------------------------- |
| `rule`          | string               | required | YAML rule content         |
| `path`          | string               | `.`      | Directory to search       |
| `max_results`   | integer              | 100      | Maximum matches to return |
| `output_format` | `"text"` \| `"json"` | `"text"` | Output format             |

**Use cases:**

- Multi-condition searches
- Context-aware matching
- Complex refactoring patterns
- Security vulnerability detection

## Usage Examples

### Basic Pattern Search

**User Query:** "Find all console.log statements"

**AI-Generated Rule:**

```yaml
rule:
  pattern: console.log($$$)
```

### Complex Rule Example

**User Query:** "Find async functions that use await"

**AI-Generated Rule:**

```yaml
rule:
  pattern: async function $NAME($$$) { $$$ await $$$ $$$ }
  # Or for arrow functions:
  pattern: const $NAME = async ($$$) => { $$$ await $$$ $$$ }
```

## Supported Languages

ast-grep supports **many programming languages** including (but not limited to):

- Python, JavaScript, TypeScript
- Rust, Go, Java, C/C++
- And many more...

**Complete list:** [ast-grep language support documentation](https://ast-grep.github.io/reference/languages.html)

**Custom Languages:** Add support via `sgconfig.yaml` — see [custom language guide](https://ast-grep.github.io/guide/project/project-config.html#languagecustomlanguage)

## Documentation & Rule Writing

The repository includes comprehensive rule documentation in **[ast-grep.mdc](https://github.com/ast-grep/ast-grep-mcp/blob/main/ast-grep.mdc)** covering:

- Simple patterns to complex multi-condition searches

## Alternative: Rust Implementation

**Repository:** [lib.rs/crates/ast-grep-mcp](https://lib.rs/crates/ast-grep-mcp) - Rust port of the original Python implementation

**Installation:**

```bash
# Via Cargo
cargo install ast-grep-mcp

# Or download binary from GitHub Releases
```

**Run:**

```bash
# With custom config
ast-grep-mcp-server --config /absolute/path/to/sgconfig.yaml

# Note: Transport must be stdio (not SSE)
```

## Hermes Integration

For Hermes Agent (uvx mode):

```yaml
mcp_servers:
  ast-grep:
    command: "uvx"
    args:
      [
        "--from",
        "git+https://github.com/ast-grep/ast-grep-mcp.git",
        "ast-grep-mcp",
      ]
    env:
      AST_GREP_CONFIG: "/path/to/sgconfig.yaml" # Optional
    tools:
      include:
        [dump_syntax_tree, test_match_code_rule, find_code, find_code_by_rule]
```

For Docker mode (build from source):

```yaml
mcp_servers:
  ast-grep:
    command: "docker"
    args:
      [
        "run",
        "-i",
        "--rm",
        "-v",
        "C:/Users/Alexa/Desktop/SandBox:/workspace",
        "ast-grep-mcp:latest",
      ]
    tools:
      include:
        [dump_syntax_tree, test_match_code_rule, find_code, find_code_by_rule]
```

Then run:

```bash
hermes mcp test ast-grep
/reload-mcp
```

## References

- GitHub: <https://github.com/ast-grep/ast-grep-mcp>
- ast-grep: <https://ast-grep.github.io/>
- mcpservers.org: <https://mcp.so/server/ast-grep/ast-grep>
- Rust Port: <https://lib.rs/crates/ast-grep-mcp>

Then run:

```bash
hermes mcp test ast-grep
/reload-mcp
```

## References

- GitHub: <https://github.com/ast-grep/ast-grep-mcp>
- ast-grep: <https://ast-grep.github.io/>
- mcpservers.org: <https://mcp.so/server/ast-grep/ast-grep>
- Rust Port: <https://lib.rs/crates/ast-grep-mcp>
