# Code Block Detection & Language Tagging

## Detection Rules

### Indented Blocks (4+ spaces or 1+ tabs)
```
    def hello():
        print("world")
```
→ Wrap as ```python ... ```

### Fenced Blocks (``` or ~~~)
```
```python
def hello():
    print("world")
```
```
→ Preserve, ensure language tag present

### Inline Code Indicators
- Backticks already present → preserve
- File paths: `src/main.py` → `` `src/main.py` ``
- Commands: `npm install` → `` `npm install` ``
- Technical terms: `JSON`, `API` → leave as-is (not code)

## Language Inference

| Heuristic | Language |
|-----------|----------|
| Shebang `#!/usr/bin/env python` | `python` |
| `import ` / `from X import` | `python` |
| `def ` / `class ` / `async def` | `python` |
| `function ` / `const ` / `let ` / `=>` | `javascript` |
| `type ` / `interface ` / `: string` | `typescript` |
| `SELECT ` / `INSERT ` / `CREATE TABLE` | `sql` |
| `docker ` / `kubectl ` / `helm ` | `bash` |
| `npm ` / `yarn ` / `pnpm ` | `bash` |
| `git ` / `gh ` / `glab ` | `bash` |
| `cargo ` / `rustc ` | `rust` |
| `go ` / `package main` | `go` |
| `package ` / `import ` (Java) | `java` |
| `# ` comment style + `func ` | `go` |
| `<!-- -->` | `html` |
| `{ ` / `} ` + `key: value` | `json` / `yaml` |

## Fallback

If no confident match → use `text` or leave untagged.

## Verification Checklist

- [ ] Every fenced block has a language tag
- [ ] No empty language tags (``` not ```text)
- [ ] Indented blocks converted to fenced with language
- [ ] Inline code uses single backticks
- [ ] No ``` inside code blocks (nested fences)
- [ ] Language tags are lowercase (```python not ```Python)