# audit-227.cjs — Overview

## Purpose
Audit script for analyzing CommonJS module patterns, dependencies, and security across a Node.js project. This script scans JavaScript files for CommonJS `require()` and `module.exports` usage, detects known patterns, and generates an audit report covering dependency depth, circular dependency detection, and module structure.

## Usage

```bash
node audit-227.cjs [--dir PATH] [--output FORMAT] [--report-file FILE] [--ignore PATTERN] [--verbose] [-h]
```

### Options

| Option          | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--dir`        | Directory to audit (default: current working directory)        |
| `--output`     | Report format: `text`, `json`, `html` (default: `text`)      |
| `--report`     | Save the audit report to a file                                |
| `--ignore`     | Glob pattern for files/directories to ignore (repeatable)      |
| `--verbose`    | Show detailed per-file analysis                                |
| `--ci`         | Run in CI mode — exit with non-zero code on issues found       |

## Behavior

- Recursively scans the target directory for `.js`, `.cjs` files.
- Parses each file for CommonJS patterns: `require()`, `module.exports`, `exports`.
- Detects circular dependencies using graph traversal.
- Reports module size, dependency count, and complexity metrics.
- Generates a dependency graph summary identifying unused or missing modules.
- Outputs JSON/HTML reports suitable for CI pipeline integration.

## Example

**Audit the current directory:**
```bash
node audit-227.cjs
```

**Audit a specific project with JSON output:**
```bash
node audit-227.cjs --dir ./src --output json --report audit.json
```

**CI mode ignoring test files:**
```bash
node audit-227.cjs --dir ./project --ignore "**/test/**" --ignore "**/node_modules/**" --ci
```

## Dependencies

- Node.js 14+
- No npm dependencies (vanilla Node.js)

## See Also

- CommonJS specification: https://nodejs.org/api/modules.html
- Circular dependency resolution strategies