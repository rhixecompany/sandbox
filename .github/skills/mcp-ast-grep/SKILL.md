---
name: mcp-ast-grep
title: MCP ast-grep — AST-based Code Search & Refactor
description: Exposes all ast-grep MCP tools for AST-based code search, pattern matching, YAML rule matching, syntax dumping, code scanning, import analysis, and AST rewrite refactoring. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - ast-grep
  - code-search
  - linting
  - refactoring
---
# MCP ast-grep

Provides AST-level code search and transformation via the [ast-grep MCP server](https://github.com/nicepkg/ast-grep-mcp). Enables structural code analysis that understands syntax, not just text.

## Overview

Automated reasoning and workflow tool for `mcp-ast-grep`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `ast-grep` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @notprolands/ast-grep-mcp`

## Tools

| Tool | Description |
|------|-------------|
| `find_code` | Simple AST pattern search (single node) — uses metavariables like `$VAR` |
| `find_code_by_rule` | Advanced multi-node search via YAML rules — pattern can contain/have another AST |
| `rewrite_code` | AST find-and-replace refactoring using metavariables — ⚠️ modifies files |
| `dump_syntax_tree` | Dump CST or pattern AST structure — debug rules |
| `test_match_code_rule` | Test a YAML rule against sample code without running on project |
| `scan_code` | Scan TypeScript for bugs, perf issues, type safety violations |
| `analyze_imports` | Analyze imports: usage (find unused imports) or discovery (explore all imports) |

## Workflow

### Phase 1: Tool Discovery

```
hermes mcp test ast-grep     # verify connectivity
```

### Phase 2: Use Tools

**find_code** — Simple pattern search:
```
Pattern: `console.log($ARG)`  — find all console.log calls
Language: typescript
Path: src/
```

**find_code_by_rule** — Complex YAML rule:
```yaml
rule:
  pattern: await Promise.all($ARGS)
  inside:
    kind: for_of_statement
```

**rewrite_code** — Refactoring:
```
Pattern: `console.log($ARG)` → Replacement: `logger.info($ARG)`
Language: typescript
```

**dump_syntax_tree** — Debug:
```
Code: `if (x > 5) { return x; }`
Language: typescript
Format: cst
```

**test_match_code_rule** — Validate before running:
```yaml
rule:
  pattern: if ($C) { return; }
```

**scan_code** — Quality scan:
```
Path: /path/to/project
```

**analyze_imports** — Dep analysis:
```
Path: /path/to/project
Mode: usage | discovery
```

### Phase 3: Test Cases

```bash
# 1. Connectivity
hermes mcp test ast-grep

# 2. Simple find pattern (JS/TS)
# Navigate to SandBox, find all console.log
# Call: ast_grep_find_code(pattern="console.log($ARG)", language="typescript", path=".")

# 3. Dump syntax tree (debug rule)
# Call: ast_grep_dump_syntax_tree(code="if (a) { b() }", language="typescript", format="cst")

# 4. Test rule match
# Call: ast_grep_test_match_code_rule(code="console.log('hi')", rule={rule: {pattern: "console.log($ARG)"}}, language="typescript")

# 5. Scan code quality
# Call: ast_grep_scan_code(path=".")

# 6. Import analysis
# Call: ast_grep_analyze_imports(path=".", mode="discovery")
```

## Best Practices

1. **Start with `test_match_code_rule`** before running `find_code_by_rule` on a real project — validates rule syntax without side effects
2. **Use `dump_syntax_tree` with `format=cst`** to discover correct syntax kind names when building complex YAML rules
3. **Prefer `find_code_by_rule`** over `find_code` for multi-node patterns (e.g., find `await` inside `for` loops)
4. **Use metavariables** (`$SINGLE`, `$$$MULTI`) for capture groups — `$` matches one node, `$$$` matches a sequence
5. **Dry-run `rewrite_code`** with `auto_apply=false` first to preview changes, then use `auto_apply=true` when confident
6. **Language support**: TypeScript/JavaScript, Python, Rust, Go, Java, C/C++, and more

## Pitfalls

- `rewrite_code` with `auto_apply=true` **modifies files on disk** — use version control or dry-run first
- `scan_code` currently only supports TypeScript — other languages return empty results
- Pattern syntax varies by language — dump the tree first to understand the AST node types
- Large codebases may take time — scope paths narrowly (subdirectory, not root)
- Metavariable names must be `$UPPERCASE` — lowercase will not match

## Verification Checklist

- [ ] `hermes mcp test ast-grep` passes
- [ ] `find_code` returns matches for known patterns in the project
- [ ] `dump_syntax_tree` produces valid output
- [ ] `test_match_code_rule` validates without error
- [ ] `scan_code` returns analysis (TS projects)

## When to Use


- When you need to perform MCP ast-grep — AST-based Code Search & Refactor operations or tasks
- When managing MCP ast-grep — AST-based Code Search & Refactor infrastructure or configurations
- When automating or debugging MCP ast-grep — AST-based Code Search & Refactor workflows
- **Triggers**: "mcp ast-grep — ast-based code search & refactor" required for a project
