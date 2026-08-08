# Persistent Memory | Hermes Agent - Nous Research

> **Source:** <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
> **Retrieved:** 2026-07-09T21:15:30
> **Backend:** web_extract

---

Hermes Agent has bounded, curated memory that persists across sessions. This lets it remember your preferences, your projects, your environment, and things it has learned.

## How It Works

Two files make up the agent's memory:

| File          | Purpose                                                                 | Char Limit                |
| ------------- | ----------------------------------------------------------------------- | ------------------------- |
| **MEMORY.md** | Agent's personal notes — environment facts, conventions, things learned | 2,200 chars (~800 tokens) |
| **USER.md**   | User profile — your preferences, communication style, expectations      | 1,375 chars (~500 tokens) |

Both are stored in `~/.hermes/memories/` and are injected into the system prompt as a frozen snapshot at session start. The agent manages its own memory via the `memory` tool — it can add, replace, or remove entries.

**Character limits keep memory focused.** Memory does **not** auto-compact: when a write would exceed the limit, the `memory` tool returns an error instead of silently dropping entries. The agent then makes room itself — consolidating or removing entries in the same turn before retrying (see [What Happens When Memory is Full](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory#what-happens-when-memory-is-full)). Note that `replace` is also bound by the limit: swapping an entry for a longer one can still overflow, so the new content must be shortened (or another entry removed) to fit.

## How Memory Appears in the System Prompt

At the start of every session, memory entries are loaded from disk and rendered into the system prompt as a frozen block:

```
══════════════════════════════════════════════MEMORY (your personal notes) [67% — 1,474/2,200 chars]══════════════════════════════════════════════
User's project is a Rust web service at ~/code/myapi using Axum + SQLx§This machine runs Ubuntu 22.04, has Docker and Podman installed§User prefers concise responses, dislikes verbose explanations
```

The format includes:

- A header showing which store (MEMORY or USER PROFILE)
- Usage percentage and character counts so the agent knows capacity
- Individual entries separated by `§` (section sign) delimiters
- Entries can be multiline

**Frozen snapshot pattern:** The system prompt injection is captured once at session start and never changes mid-session. This is intentional — it preserves the LLM's prefix cache for performance. When the agent adds/removes memory entries during a session, the changes are persisted to disk immediately but won't appear in the system prompt until the next session starts. Tool responses always show the live state.

## Memory Tool Actions

The agent uses the `memory` tool with these actions:

- **add** — Add a new memory entry
- **replace** — Replace an existing entry with updated content (uses substring matching via `old_text`)
- **remove** — Remove an entry that's no longer relevant (uses substring matching via `old_text`)

There is no `read` action — memory content is automatically injected into the system prompt at session start. The agent sees its memories as part of its conversation context.

### Substring Matching

The `replace` and `remove` actions use short unique substring matching — you don't need the full entry text. The `old_text` parameter just needs to be a unique substring that identifies exactly one entry:

```python
# If memory contains "User prefers dark mode in all editors"
memory(action="replace", target="memory",
       old_text="dark mode",
       content="User prefers light mode in VS Code, dark mode in terminal")
```

If the substring matches multiple entries, an error is returned asking for a more specific match.

## Two Targets Explained

### `memory` — Agent's Personal Notes

For information the agent needs to remember about the environment, workflows, and lessons learned:

- Environment facts (OS, tools, project structure)
- Project conventions and configuration
- Tool quirks and workarounds discovered
- Completed task diary entries
- Skills and techniques that worked

### `user` — User Profile

For information about the user's identity, preferences, and communication style:

- Name, role, timezone
- Communication preferences (concise vs detailed, format preferences)
- Pet peeves and things to avoid
- Workflow habits
- Technical skill level

## What to Save vs Skip

### Save These (Proactively)

The agent saves automatically — you don't need to ask. It saves when it learns:

- **User preferences:** "I prefer TypeScript over JavaScript" → save to `user`
- **Environment facts:** "This server runs Debian 12 with PostgreSQL 16" → save to `memory`
- **Corrections:** "Don't use `sudo` for Docker commands, user is in docker group" → save to `memory`
- **Conventions:** "Project uses tabs, 120-char line width, Google-style docstrings" → save to `memory`
- **Completed work:** "Migrated database from MySQL to PostgreSQL on 2026-01-15" → save to `memory`
- **Explicit requests:** "Remember that my API key rotation happens monthly" → save to `memory`

### Skip These

- **Trivial/obvious info:** "User asked about Python" — too vague to be useful
- **Easily re-discovered facts:** "Python 3.12 supports f-string nesting" — can web search this
- **Raw data dumps:** Large code blocks, log files, data tables — too big for memory
- **Session-specific ephemera:** Temporary file paths, one-off debugging context
- **Information already in context files:** SOUL.md and AGENTS.md content

## Capacity Management

Memory has strict character limits to keep system prompts bounded:

| Store  | Limit       | Typical entries |
| ------ | ----------- | --------------- |
| memory | 2,200 chars | 8-15 entries    |
| user   | 1,375 chars | 5-10 entries    |

### What Happens When Memory is Full

When the agent attempts a write that would exceed the limit, the `memory` tool returns an error. The agent then:

1. Reviews current entries
2. Consolidates similar entries
3. Removes stale/irrelevant entries
4. Retries the write

The agent is responsible for making room — it does not silently drop data. This ensures the agent is always aware of what it's forgetting.

### Practical Examples of Good Memory Entries

**memory (agent notes):**

- `This machine runs Windows 11, WSL2 Ubuntu 22.04, has Docker Desktop + Podman` (83 chars)
- `Project uses pnpm workspaces, monorepo at ~/code/monorepo, TypeScript strict mode` (85 chars)
- `Docker commands work without sudo — user is in docker group` (53 chars)
- `Completed: migrated auth from JWT to session cookies on 2026-03-14` (59 chars)
- `Avoid`bun install -g`— use`pnpm dlx`or project-local bins instead` (64 chars)

**user (user profile):**

- `Name: Alex. Timezone: America/Los_Angeles (PDT). Work hours: Mon-Fri 9-5` (59 chars)
- `Prefers concise responses — lead with action, explain second` (53 chars)
- `Dislikes emoji and corporate-speak ("I'd be happy to help")` (52 chars)
- `Technical level: senior engineer. Don't explain basics unless asked` (56 chars)
- `Pet peeve: variable names like \`data\`, \`info\`, \`obj\` — use descriptive names` (60 chars)

## Duplicate Prevention

The agent checks for near-duplicate entries before adding. Substring overlap >80% on an existing entry blocks the add. This prevents the same fact from being written repeatedly.

## Security Scanning

All memory writes are scanned for:

- Prompt injection patterns
- PII (emails, API keys, tokens, addresses)
- Suspicious instructions

Flagged writes are blocked and logged. The agent sees the rejection and can retry with sanitized content.

## Session Search

Hermes maintains a full session history in a SQLite database (`state.db`) with FTS5 full-text search. The `session_search` tool queries this independently of the `memory` tool.

### `session_search` vs `memory`

| Aspect          | `session_search`                          | `memory`                     |
| --------------- | ----------------------------------------- | ---------------------------- |
| **Scope**       | All past conversations                    | Curated facts only           |
| **Freshness**   | Real-time — includes last message         | Frozen at session start      |
| **Granularity** | Full messages                             | Condensed entries            |
| **Cost**        | On-demand query                           | Always in prompt             |
| **Use for**     | "What did we discuss about X last month?" | "What OS does the user run?" |

Both can be used in the same turn — the agent decides based on the question.

## Configuration

Memory behavior is controlled via `~/.hermes/config.yaml`:

```yaml
memory:
  auto_write: true # Agent writes to memory when it learns something
  reflection_enabled: true # Daily reflection pass synthesizes memories
  write_approval: prompt # "prompt" | "auto" — ask before writing
  char_limit_memory: 2200 # Custom limit (default 2200)
  char_limit_user: 1375 # Custom limit (default 1375)
```

- `auto_write: false` → agent tells you what it would write, you decide
- `write_approval: "auto"` → agent writes without prompting (use with caution)
- Reflection runs once per day, reads recent sessions, writes summaries to MEMORY.md or generates skills

## Controlling memory writes (`write_approval`)

By default, the agent prompts you before writing to memory (`write_approval: prompt`). You can change this:

```bash
# Auto-approve memory writes
hermes config set memory.write_approval auto

# Require prompt (default)
hermes config set memory.write_approval prompt
```

Note: Even with `write_approval: auto`, the agent will still show you what it's writing in the response.

## Background review notifications (`display.memory_notifications`)

When the background review process (auxiliary model) adds or updates memory entries, you can choose to be notified:

```bash
hermes config set display.memory_notifications true
```

This shows a brief toast/notification when background review writes to memory.

## Running the review on a cheaper model (`auxiliary.background_review`)

The reflection pass runs on a background model. You can specify a cheaper one:

```bash
hermes config set auxiliary.background_review "openrouter:google/gemini-flash-1.5"
```

This runs the daily synthesis on a cheaper model, reducing cost while still updating memory.

## Controlling skill writes (`skills.write_approval`)

Similar to memory, skill generation has a write approval setting:

```bash
hermes config set skills.write_approval auto
# or
hermes config set skills.write_approval prompt
```

## External Memory Providers

Hermes supports pluggable memory backends. The built-in provider uses the local `~/.hermes/memories/` files. Custom providers can store memory in databases, vector stores, or remote services. See the [Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers) page for implementation details.

---

_Extracted by web-research-pipeline v2.0.0_
