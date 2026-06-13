# Source: https://hermes-agent.nousresearch.com/docs/guides/tips

# Hermes Agent: Tips & Best Practices — Comprehensive Summary

---

## 🚀 Quick Start

```bash
# Get 300+ models (Claude, GPT-5, Gemini) under one subscription
hermes setup --portal
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
Create `AGENTS.md` in project root for repeated instructions:
- "use tabs not spaces"
- "we use pytest"
- "the API is at `/api/v2`"
- **Auto-loaded every session** — zero effort after setup

### Let the Agent Use Its Tools
- Say "find and fix the failing test" not "open `tests/test_foo.py`, look at line 42..."
- Agent has: file search, terminal access, code execution
- Let it explore and iterate

### Use Skills for Complex Workflows
```bash
/skills          # Browse available skills
/axolotl         # Invoke skill directly
/github-pr-workflow
```

---

## ⌨️ CLI Power User Tips

| Feature | Shortcut | Notes |
|---------|----------|-------|
| **Multi-line input** | `Alt+Enter`, `Ctrl+J`, `Shift+Enter` | `Shift+Enter` needs Kitty keyboard protocol (Kitty/foot/WezTerm/Ghostty default; iTerm2/Alacritty/VS Code with protocol enabled) |
| **Paste detection** | Auto | Multi-line pastes buffered as single message |
| **Interrupt** | `Ctrl+C` (once) | Redirect agent mid-response |
| **Force exit** | `Ctrl+C` (2x within 2s) | |
| **Resume last session** | `hermes -c` | Full conversation history restored |
| **Resume by title** | `hermes -r "my research project"` | |
| **Clipboard image paste** | `Ctrl+V` | Vision analyzes screenshots, diagrams, error popups, UI mockups |
| **Slash autocomplete** | `/` + `Tab` | Shows built-in commands + installed skills |

### Verbose Modes (`/verbose` cycles through)
```
off → new → all → verbose
```
- **"all"** — great for watching agent actions
- **"off"** — cleanest for simple Q&A

---

## 📁 Context Files

### AGENTS.md — Your Project's Brain
**Location:** Project root (auto-loaded at session start)

```markdown
# Project Context
- This is a FastAPI backend with SQLAlchemy ORM
- Always use async/await for database operations
- Tests go in tests/ and use pytest-asyncio
- Never commit .env files
```

**Discovery behavior:**
- Top-level `AGENTS.md` → loaded at session start
- Subdirectory `AGENTS.md` → discovered lazily during tool calls (via `subdirectory_hints.py`), injected into tool results only

### SOUL.md — Customize Personality
**Location:** `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`

```markdown
# Soul
You are a senior backend engineer. Be terse and direct.
Skip explanations unless asked. Prefer one-liners over verbose solutions.
Always consider error handling and edge cases.
```

| File | Purpose | Scope |
|------|---------|-------|
| `SOUL.md` | Durable personality | Instance-wide |
| `AGENTS.md` | Project-specific instructions | Per-project |

### .cursorrules Compatibility
- Reads `.cursorrules` and `.cursor/rules/*.mdc` automatically
- No need to duplicate conventions

### Token Budget Warning
> **Keep context files focused and concise. Every character counts against your token budget since they're injected into every single message.**

---

## 🧠 Memory & Skills

### Memory vs. Skills

| | Memory | Skills |
|---|--------|--------|
| **For** | Facts: environment, preferences, project locations, learned info | Procedures: multi-step workflows, tool-specific instructions, reusable recipes |
| **Think** | "What" | "How" |

### When to Create Skills
> **If a task takes 5+ steps and you'll do it again** → ask agent to create a skill:
> > "save what you just did as a skill called `deploy-staging`"
> > Next time: just type `/deploy-staging`

### Managing Memory Capacity
- **MEMORY.md** ~2,200 chars
- **USER.md** ~1,375 chars
- Auto-consolidates when full
- Help by saying: "clean up your memory" or "replace the old Python 3.9 note — we're on 3.12 now"

### Let the Agent Remember
- "remember this for next time" → saves key takeaways
- "save to memory that our CI uses GitHub Actions with the `deploy.yml` workflow"
- **Note:** Memory is a frozen snapshot — changes don't appear in system prompt until next session

---

## ⚡ Performance & Cost

### Don't Break the Prompt Cache
- Most LLM providers cache system prompt prefix
- **Keep system prompt stable** (same context files, same memory) → cache hits = significantly cheaper
- Avoid changing model or system prompt mid-session

### Use `/compress` Before Hitting Limits
```bash
/compress    # Summarizes conversation, preserves key context
```

---

## 🔐 Security

- Never paste API keys in chat — use `hermes config set KEY value`
- Context files are scanned for prompt injection before loading
- Use `hermes skills check` before installing third-party skills
- Gateway: use platform-native auth (OAuth) over long-lived tokens