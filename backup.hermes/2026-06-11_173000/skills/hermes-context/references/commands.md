# Context Files Commands Reference

## Verification
```bash
# Check SOUL.md
cat ~/.hermes/SOUL.md

# Check root AGENTS.md
cat AGENTS.md

# Test context loading
hermes chat -q "What project am I in?"

# Test subdirectory discovery
cd projects/Banking && hermes chat -q "What project am I in?"
```

## File Locations
| File | Location | Scope | Priority |
|------|----------|-------|----------|
| `.hermes.md` / `HERMES.md` | Git root | Project | 1 (highest) |
| `AGENTS.md` | CWD + subdirs | Project | 2 |
| `CLAUDE.md` | CWD + subdirs | Project | 3 |
| `.cursorrules` | CWD | Project | 4 |
| `.cursor/rules/*.mdc` | CWD | Project | 4 |
| `SOUL.md` | `HERMES_HOME` | Global | Independent (slot #1) |

## Priority Order
```
.hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
```

## Security
All context files scanned for:
- Prompt injection patterns
- Malicious instructions
- Attempts to override system behavior