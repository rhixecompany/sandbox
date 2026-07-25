# docs — Technology Stack Blueprint

## Core Technologies

| Technology | Usage | Evidence |
| ------------ | ------- | ---------- |
| Markdown | Primary documentation format | `.md` files |
| YAML | CI/GitHub Actions configuration | `.yml` files |
| JSON | Data/configuration storage | `.json` files |

## Tooling

| Tool | Purpose |
|------|---------|
| GitHub Actions | CI — TODO scanner workflow |
| markdownlint | Markdown quality validation |

## Build & CI

```yaml
# .github/workflows/todo-scan.yml
# Scans for TODO/FIXME/HACK markers on push/PR
```

## Dependencies

- **Runtime:** None (static documentation)
- **Dev:** None (no build step required)
- **CI:** GitHub Actions (free tier)

## Notes

- Zero runtime dependencies — renders natively on GitHub and VS Code
- No build/compile step; markdown is the source and output
- Designed for both human readers and AI agent consumption
