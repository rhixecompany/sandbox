---
name: note-taking-apps
title: Note-Taking Apps (Obsidian & Notion)
description: Personal knowledge management across Obsidian (local Markdown vault) and Notion (API/ntn CLI). Capture, query, and sync notes.
license: MIT
author: Hermes Agent
version: 1.0.0
tags: [note-taking, obsidian, notion, pkm, markdown, knowledge-base]
metadata:
  hermes:
    tags: [note-taking, obsidian, notion, pkm]
---

# Note-Taking Apps (Obsidian & Notion)

Class-level umbrella for personal knowledge management. Two backends, one PKM class:

- **Obsidian** — local-first Markdown vault, persona-driven capture, no external API. See `references/obsidian.md`.
- **Notion** — hosted workspace via integration token + `ntn` CLI (or raw HTTP/curl). See `references/notion.md`.

## When to Use

- "Save this to my notes / vault" (Obsidian or Notion)
- "Find / read a note or page I wrote earlier"
- "Create a Notion page/database entry from Markdown"
- "Sync or query my knowledge base"

## 1. Obsidian — quick orientation

Local Markdown. Persona-based capture and retrieval; no tokens, no network. Use when the user's
knowledge base lives in a local vault. Profile selection, when-to-use / when-not-to-use, and the
3-phase workflow (prep → execute → verify) are in `references/obsidian.md`.

## 2. Notion — quick orientation

```bash
# 1. Create an integration, copy the token
# 2. Install the CLI
pip install ntn            # or: npm i -g ntn
# 3. Use it (macOS/Linux preferred)
ntn search "quarterly plan"
ntn read <page-id> --markdown
ntn create --markdown note.md
ntn patch <page-id> --markdown update.md
ntn query "<database-id>" --filter "..."
```

Token setup, `ntn` CLI commands (search/read/create/patch/query/file-upload), and the cross-platform
raw-HTTP/curl path are in `references/notion.md`.

## Picking a backend

- Local, private, Markdown-native, offline → **Obsidian**.
- Shared workspace, databases, team collaboration, API automation → **Notion**.

## Related Skills

- `note-taking-apps` subsumes the former `obsidian` and `notion` skills.
- For local semantic search over notes, see `qmd`, `llm-wiki`.
- For docs/knowledge bases hosted elsewhere, see `siyuan`, `google-workspace`.

## Reference Library

| File | Contents |
|------|----------|
| `references/obsidian.md` | Personas, profile selection, when-to-use, 3-phase capture/retrieval workflow |
| `references/notion.md` | Token setup, `ntn` CLI (search/read/create/patch/query/upload), curl path |
