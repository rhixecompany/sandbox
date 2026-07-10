# SOUL.md, MEMORY.md and state.db - Hermes Agent memory architecture

> **Source:** https://lumadock.com/tutorials/hermes-memory-architecture-explained
> **Retrieved:** 2026-07-09T21:15:30
> **Backend:** web_extract
---

One of the things that makes Hermes feel different from a stock LLM chat is that it remembers you. Not in a buzzy "AI with personality" way; in a flat, mechanical, file-on-disk way. Your persona lives in a markdown file. Your facts live in another markdown file. Your conversation history lives in a SQLite database. Each one is a thing you can read, edit and delete with normal command-line tools, which means the memory layer is debuggable in a way that "just trust the LLM" memory systems aren't.

This article walks through what each layer does, when each one fires, what it costs in tokens and how to edit them by hand without breaking things.

## The three layers

Hermes splits memory across three places, each with a different lifetime, granularity and intended purpose.

**Layer 1: persona and frozen facts.** Markdown files at `~/.hermes/SOUL.md` and `~/.hermes/memories/MEMORY.md` and `~/.hermes/memories/USER.md`. These get loaded into the system prompt at the start of every session. Stable, slow-changing, hand-curated. The agent doesn't write to these by default; you do.

`~/.hermes/SOUL.md`
`~/.hermes/memories/MEMORY.md`
`~/.hermes/memories/USER.md`

Tokens spent: typically 1500 to 5000 tokens, depending on how much you've put in. Worth being judicious because every session pays this cost.

**Layer 2: skills.** The `~/.hermes/skills/` directory. Each skill is a folder with a SKILL.md file describing when to invoke it and what to do. Hermes auto-creates skills via the learning loop (after a few successful runs of similar tasks) and the skills then get used automatically when the agent encounters similar tasks again.

`~/.hermes/skills/`

Tokens spent: zero per session unless the skill is invoked, in which case you pay for the SKILL.md content as part of the active context for the duration of that skill's task.

**Layer 3: session search.** A SQLite database at `~/.hermes/state.db` holding every message ever sent in any session, with FTS5 full-text search on top. The agent can call a `session_search` tool to find relevant past conversations.

`~/.hermes/state.db`
`session_search`

Tokens spent: zero per session unless the agent decides to query it. Typical queries pull a few hundred to a few thousand tokens of relevant past context.

## Layer 1, in detail

SOUL.md is the persona file. It defines how the agent talks: tone, register, idioms it uses, things it cares about. Edit it as plain markdown. The format is loose; you can write it as bullet points, prose, dialogue examples, whatever feels right. Hermes loads it whole into the system prompt.

A reasonable SOUL.md for a personal agent:

```markdown
# Persona
You are Alice's assistant. You are concise, direct and slightly dry.
You don't apologise unless you've done something wrong.
You don't use emoji.
You match the user's tone: terse with terse messages, more conversational
when the user is being conversational.
# Boundaries
If the user asks for help with something destructive (deleting files,
sending money, posting publicly), you confirm before acting.
You don't pretend to be a human.
```

MEMORY.md is the agent's working knowledge. It's where the agent (or you) writes down stable facts that should be available every session. Things like project context, ongoing themes, preferences.

```markdown
# Memory
## Projects
- Working on a Next.js SaaS app called BrightCart, deployed on Coolify.
- The codebase is at ~/code/brightcart, main branch is main.
- Stripe is the payment provider. Webhooks point at /api/stripe-webhook.
## Preferences
- Prefer Postgres over MySQL for new projects.
- Use ripgrep over grep for searching code.
- Replies should default to short unless I explicitly ask for detail.
```

USER.md is parallel to MEMORY.md but more strictly factual: things specifically about the user (your name, your timezone, your work hours, things the agent should know about you as a person rather than about your projects).

```markdown
# User
Name: Alice Chen
Timezone: Europe/London
Work hours: Mon-Fri 09:00-18:00
Important: Has a 14-month-old, so don't suggest "let's catch up at 8am Saturday".
```

The split between MEMORY.md and USER.md is a soft convention; both get loaded in the same way. Use the split or don't, depending on how much you have to remember and how you like to organise it.

## How auto-write works (and how to control it)

When you tell the agent something it should remember, it can write to MEMORY.md or USER.md on its own. The trigger phrase is anything like "remember that...", "make a note...", "next time you see X, do Y...". The agent appends to the relevant file with a timestamp comment.

If you don't want the agent writing to memory automatically:

```bash
hermes config set memory.auto_write false
```

Then the agent tells you what it would have written and you can copy-paste into the file by hand if you want. Useful when you want tighter control over what ends up in the persistent context.

If the agent writes too much (you turn around and the file has grown 100 lines in a week), prune. Open the file, delete entries that aren't useful any more, save. The agent picks up the pruned version on next session start.

## Layer 2, the skills system

Skills are the mid-grained memory layer. They capture procedures, not facts. "How do I deploy a Next.js app to Coolify" is a skill; "BrightCart deploys to Coolify" is a memory.

The `~/.hermes/skills/` directory has one folder per skill, each containing a SKILL.md plus optional supporting files (templates, scripts, lookup tables). The SKILL.md frontmatter declares when the skill applies; the body describes what to do.

`~/.hermes/skills/`

The learning loop generates skills automatically from successful task patterns. After three or four successful runs of similar work, Hermes generates a skill that captures the procedure. You can read it, edit it, delete it. Editing a generated skill is fine, but Hermes may regenerate over your edits if it sees similar successful runs again. To prevent that, mark the skill as user-locked in the frontmatter; the skills article covers the lock pattern in detail.

Skills cost tokens only when invoked. The agent decides per task which skills are relevant; only relevant skills get loaded into the active context for that task.

## Layer 3, the session DB

state.db is where every message ever sent through Hermes lives. Each row is a message: who sent it, when, on what channel, with what content. FTS5 full-text indexes the content for efficient search.

The agent doesn't load any of this by default. It queries when it decides search is useful: "did I ever discuss X" or "what did Alice say about Y last month" type prompts trigger the agent to call `session_search` internally, which queries state.db and returns matching rows.

`session_search`

You can query state.db directly with sqlite3:

```bash
sqlite3 ~/.hermes/state.db "SELECT created_at, channel, content FROM messages WHERE content MATCH 'BrightCart' ORDER BY created_at DESC LIMIT 10"
```

This returns the last ten messages mentioning BrightCart, regardless of which channel they came in on. Useful when you're trying to remember what you previously told the agent about a project.

The DB grows over time. A few KB per turn plus the FTS5 indexes; over six months of normal use, expect 20 to 100 MB. Manageable on any reasonable VPS. If you want to prune, the backups guide covers the SQL to delete old rows safely.

## The reflective phase

Periodically, Hermes runs a reflection pass that synthesises across stored memory: it reads recent sessions, distills patterns and writes summaries back into MEMORY.md or generates new skills.

The trigger conditions are heuristic; the user-visible effect is that after a heavy day of conversation, your MEMORY.md may have a new entry capturing the gist of yesterday's work. The agent has had time to think about what mattered and what didn't.

If you don't want this:

```bash
hermes config set memory.reflection_enabled false
```

The agent skips reflection passes. Memories accumulate only when you (or the agent in active conversation) explicitly note them.

I leave it on. The reflection pass occasionally generates entries I find useful and the cost (a small batch of LLM calls per day) is low.

## What the agent sees on each session start

When you open a fresh chat, Hermes builds the system prompt from:

- The agent's core instructions (tool definitions, behavioural rules; ~10K tokens, fixed).
- SOUL.md (~500 to 2000 tokens, your persona).
- MEMORY.md and USER.md (~500 to 3000 tokens, your facts).
- An auto-generated context block summarising recent sessions (~500 to 1500 tokens, generated each session).
- Your current message.

The total fixed overhead per turn is around 12K to 16K tokens before the agent does anything. The token-cost article goes deeper on what eats tokens and how to trim.

## Editing memory by hand without breaking things

Three rules.

Don't edit while the agent is mid-conversation. The agent has the file's content in its current context; editing the file doesn't change what the agent already loaded. Wait for an idle moment, edit, then start a new session.

Keep the format consistent. The agent doesn't strictly parse MEMORY.md or USER.md, so technically any markdown works, but heading structure helps both you and the agent navigate the file. Stick to `# Top-level`, `## Section`, `### Sub-section`.

```markdown
# Top-level
## Section
### Sub-section
```

Don't bury timestamps. The auto-write feature adds `<!-- written 2026-05-05 -->` comments to entries; keep them. Useful for "what did I add to memory last week" and for the reflective phase, which uses timestamps to decide which entries are still relevant.

```markdown
<!-- written 2026-05-05 -->
```

If you accidentally corrupt a memory file (deleted a section you didn't mean to, mangled the format), restore from your last backup. The backups guide covers selective file restore.

## Memory across migrations

[... middle omitted — see footer ...]

## FAQ

### How do I see exactly what's in the agent's context for the current session?

Inside an active Hermes session, the slash command `/context` dumps the current context window with token counts per section. You see the system prompt, persona, memories, recent messages and any retrieved skill content, with their token contribution. Useful when you're wondering why a session feels heavier than expected (often a memory file has grown without you noticing).

```bash
/context
```

### How do I make the agent forget a specific embarrassing thing it remembers?

Find the entry in MEMORY.md or USER.md, delete it, save the file. The agent forgets it on the next session start. If the entry is also reflected in skills (rare; reflection mostly writes to memory files, not skills), delete the relevant skill too. If you're worried it might be in past session messages too, query state.db to see if it's there and delete those rows if needed: `sqlite3 ~/.hermes/state.db "DELETE FROM messages WHERE content LIKE '%embarrassing thing%'; VACUUM;"`. The agent then has no record of the thing across any layer.

```bash
sqlite3 ~/.hermes/state.db "DELETE FROM messages WHERE content LIKE '%embarrassing thing%'; VACUUM;"
```

### How do I share memory between two Hermes installs without making one a clone of the other?

Sync MEMORY.md between the two via your file-sync tool of choice (Syncthing, rclone bisync, a shared NFS mount). Each install has its own state.db, so session histories stay independent, but the shared facts in MEMORY.md keep the agents on the same page about what they know. Useful for a "personal agent on laptop, work agent on VPS" pattern where you want them to share project context but not session histories.

### How do I tell which memory layer the agent is using when it answers a question?

Run with debug logging on (`HERMES_LOG_LEVEL=debug`); the agent logs each memory layer access as a separate event. Layer 1 (SOUL/MEMORY/USER) shows up at session start. Layer 2 (skills) shows up when a skill matches and gets loaded. Layer 3 (session search) shows up when the agent calls the session_search tool. Watching the log during a conversation tells you which layer is doing the heavy lifting for any given question; useful when the agent gets something wrong and you're trying to figure out which file is the source of truth.

```bash
HERMES_LOG_LEVEL=debug
```

---

*Extracted by web-research-pipeline v2.0.0*