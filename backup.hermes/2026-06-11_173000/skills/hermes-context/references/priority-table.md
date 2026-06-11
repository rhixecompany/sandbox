# Context File Priority Reference

## Loading Priority (First Match Wins)
```
1. .hermes.md / HERMES.md     ← Walks to git root
2. AGENTS.md                  ← CWD + progressive subdirectory discovery
3. CLAUDE.md                  ← CWD + progressive subdirectory discovery
4. .cursorrules               ← CWD only
5. .cursor/rules/*.mdc        ← CWD only
```

## SOUL.md
- **Always loaded independently** as agent identity (slot #1)
- Location: `HERMES_HOME/SOUL.md` only
- Not discovered from project directories

## Progressive Discovery
- At session startup: `AGENTS.md` from working directory loaded
- During session: `SubdirectoryHintTracker` watches tool calls
- When agent reads files in subdirectory → discovers that dir's AGENTS.md
- Each subdirectory checked **at most once per session**
- Walks up parent directories (reading `backend/src/main.py` discovers `backend/AGENTS.md`)

## Security Scan
All context files scanned before adding to system prompt:
- Prompt injection patterns
- Malicious instructions
- Attempts to override system behavior