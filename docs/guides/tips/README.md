# Hermes Agent: Tips & Best Practices — Comprehensive Summary

---

## 🚀 Quick Start

```bash
hermes setup --portal          # 300+ models (Claude, GPT-5, Gemini) under one subscription
```

---

## 🎯 Getting the Best Results

### Be Specific About What You Want

> **Vague prompts produce vague results.** Instead of "fix the code," say:
> > "fix the TypeError in `api/handlers.py` on line 47 — the `process_request()` function receives `None` from `parse_body()`."

**Key files/functions mentioned:** `api/handlers.py`, `process_request()`, `parse_body()`

### Provide Context Up Front

- Front-load: file paths, error messages, expected behavior
- Paste error tracebacks directly — agent parses them
- One well-crafted message beats three rounds of clarification

### Use Context Files for Recurring Instructions

Create `AGENTS.md` in project root for repeated rules:

```markdown
# Project Context
- This is a FastAPI backend with SQLAlchemy ORM
- Always use async/await for database operations
- Tests go in tests/ and use pytest-asyncio
- Never commit .env files
```

- Auto-loaded every session — zero effort after setup
- Example conventions: tabs vs spaces, pytest, API at `/api/v2`

### Let the Agent Use Its Tools

> Don't hand-hold: "find and fix the failing test" > "open `tests/test_foo.py`, look at line 42..."
- Agent has: file search, terminal access, code execution
- Let it explore and iterate

### Use Skills for Complex Workflows

```bash
/skills              # Browse available skills
/axolotl             # Invoke directly
/github-pr-workflow  # Invoke directly
```

Check skills before writing long procedural prompts.

---

## ⌨️ CLI Power User Tips

| Feature | Shortcut | Notes |
|---------|----------|-------|
| **Multi-line input** | `Alt+Enter`, `Ctrl+J`, `Shift+Enter` | `Shift+Enter` needs Kitty keyboard protocol (Kitty/foot/WezTerm/Ghostty default; iTerm2/Alacritty/VS Code with protocol enabled) |
| **Paste detection** | Auto | Multi-line pastes buffered as single message |
| **Interrupt** | `Ctrl+C` (once) | Redirect with new message |
| **Force exit** | `Ctrl+C` (2x within 2s) | |
| **Resume session** | `hermes -c` | Full history restored |
| **Resume by title** | `hermes -r "my research project"` | |
| **Clipboard image paste** | `Ctrl+V` | Vision analyzes screenshots, diagrams, error popups, UI mockups |
| **Slash autocomplete** | `/` + `Tab` | Shows built-ins (`/compress`, `/model`, `/title`) + all skills |
| **Verbose modes** | `/verbose` | Cycles: **off → new → all → verbose** |

---

## 📁 Context Files

### AGENTS.md — Project Brain

- **Location:** Project root (auto-loaded at session start)
- **Subdirectory AGENTS.md:** Discovered lazily during tool calls via `subdirectory_hints.py`
- **Purpose:** Architecture decisions, coding conventions, project-specific instructions
- **Token cost:** Injected into every message — keep focused and concise

### SOUL.md — Personality

- **Location:** `~/AppData/Local/hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`
- **Auto-seeded** with starter personality
- **Use for:** Durable personality (tone, verbosity, approach)
- **Example:**
```markdown
# Soul
You are a senior backend engineer. Be terse and direct.
Skip explanations unless asked. Prefer one-liners over verbose solutions.
Always consider error handling and edge cases.
```

### .cursorrules Compatibility

- Reads `.cursorrules` and `.cursor/rules/*.mdc` automatically
- No duplication needed

### Discovery Rules

| File | When Loaded |
|------|-------------|
| Root `AGENTS.md` | Session start |
| Subdirectory `AGENTS.md` | Lazily during tool calls (injected into tool results) |

---

## 🧠 Memory & Skills

### Memory vs. Skills

| Memory (What) | Skills (How) |
|---------------|--------------|
| Facts: environment, preferences, project locations, learned info | Procedures: multi-step workflows, tool-specific instructions, reusable recipes |

### When to Create Skills

> **If a task takes 5+ steps and you'll repeat it** → ask agent: "save what you just did as a skill called `deploy-staging`"
- Next time: just type `/deploy-staging`

### Managing Memory Capacity

- **MEMORY.md:** ~2,200 chars
- **USER.md:** ~1,375 chars
- Auto-consolidates when full
- Manual cleanup: "clean up your memory" or "replace the old Python 3.9 note — we're on 3.12 now"

### Let the Agent Remember

- "remember this for next time" → saves key takeaways
- Specific: "save to memory that our CI uses GitHub Actions with the `deploy.yml` workflow"
- **Note:** Memory is a frozen snapshot — changes don't appear in system prompt until next session

---

## ⚡ Performance & Cost

### Don't Break the Prompt Cache

- Most LLM providers cache system prompt prefix
- **Stable system prompt** (same context files, same memory) = **cache hits** = significantly cheaper
- Avoid changing model or system prompt mid-session

### Use `/compress` Before Hitting Limits

```bash
/compress    # Summarizes conversation, preserves key context, reduces tokens
/usage       # Check token consumption
```

---

## 🔧 Tool-Specific Tips

### Terminal

- Use `background=true` + `notify_on_complete=true` for long commands
- `pty=true` for interactive tools (Claude Code, Codex, REPL)
- Docker backend = persistent sandbox (packages, cwd persist across calls)

### Browser

- `browser_vision` for visual verification (CAPTCHAs, UI states)
- `browser_console` for JS errors / API failures
- WSL→Windows: use MCP bridge (`chrome-devtools-win`)

### Web Search / Extract

- `web_search` for discovery; `web_extract` for full content
- Large pages truncated — use browser for full content

### Delegation

- `delegate_task` for reasoning-heavy subtasks (debugging, review, research)
- Up to 3 concurrent for this user
- Subagents have NO memory of parent conversation — pass all context explicitly

---

## 🤖 Messaging Platforms

| Platform | Key Tip |
|----------|---------|
| Telegram | Voice messages via `[[audio_as_voice]]`; native photos |
| Discord | Threads supported; `/personality` works in-thread |
| Slack | Use `hermes gateway setup` for bot tokens |
| WhatsApp | Requires gateway; media via native delivery |

---

## 🔍 Debugging

| Issue | Diagnostic |
|-------|------------|
| Tool not firing | Check `hermes tools` — is toolset enabled? |
| Config not applying | `hermes config show` — verify YAML syntax |
| MCP tools missing | `/reload-mcp` then "list MCP tools" |
| Session not resuming | `hermes -c` requires same profile; check `~/AppData/Local/hermes/sessions/` |

---

## 📋 Checklist for New Projects

- [ ] `AGENTS.md` in root with architecture/conventions
- [ ] `SOUL.md` tuned for your voice
- [ ] `.cursorrules` if using Cursor (auto-detected)
- [ ] Provider configured via `hermes model`
- [ ] Toolsets enabled for your workflow
- [ ] Skills installed for recurring tasks
- [ ] Memory enabled (`hermes memory setup`)

---

**Source:** [Hermes Agent Docs - Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)  
**Extracted:** 2026-06-08