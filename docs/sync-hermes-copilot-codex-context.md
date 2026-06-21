# sync-hermes-copilot-codex — Dependency Context Catalog

> Generated: 2026-06-21T10:00:00Z | Source: `sync-hermes-copilot-codex.prompt.md`
> Status: Fresh re-run (Phase 1)

## Purpose Resolution

- **Purpose slug:** `sync-hermes-copilot-codex`
- **Trigger:** `/sync-hermes-copilot-codex`
- **Source file:** `sync-hermes-copilot-codex.prompt.md`
- **Source reference (legacy):** `sync-hermes-copilot-codex.prompt.txt` — *file removed in previous enhancement; reference is stale*

---

## Forward Dependencies (from this file)

### External Paths Referenced

| Path | Lines | Context |
|------|-------|---------|
| `.github/agents/` | 57, 63, 67, 113 | Copilot agent definitions |
| `.github/instructions/` | 57, 61, 65, 113 | Copilot instruction files |
| `~/.hermes/` | 34, 89 | Hermes root: skills, plugins, hooks, profiles |
| `.github/` | 34, 91 | Copilot root (VS Code workspace) |
| `~/.codex/` | 34, 92 | Codex root (agents, config.toml) |
| `~/.opencode/` | 34 | Alternative Codex root |

### Commands & Triggers Referenced

| Trigger | Lines | Context |
|---------|-------|---------|
| `/sync-hermes-copilot-codex` | 2 | This prompt's trigger |

### Skill Dependencies (from frontmatter)

| Skill | Type | Purpose |
|-------|------|---------|
| `using-superpowers` | workflow | Establishes workflow foundation |
| `user-communication-preferences` | config | Loads user prefs for execution style |
| `plans-and-specs` | planning | Creates implementation plan from goal |

---

## Reverse Dependencies (files referencing this one)

| File | Lines | Context |
|------|-------|---------|
| `test-providers-models.prompt.md` | 515 | Provider sync workflow reference |
| `docs/test-providers-models-context.md` | 55 | Related prompt family entry |
| `docs/audit-skills-judge-fix-context.md` | 82, 91 | Skills judge audit context |
| `reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md` | — | Broad agent inventory report |

---

## File Statistics

| File | Lines | Size | Frontmatter | Tables | Code Fences |
|------|-------|------|-------------|--------|-------------|
| `sync-hermes-copilot-codex.prompt.md` | 153 | 5.6 KB | ✅ Valid YAML | 5 (balanced) | 0 |

### Frontmatter Fields Present
`trigger`, `description`, `tags`, `dependencies`, `skills`

### Frontmatter Fields Missing
`name`, `title`, `version`, `author`, `license`, `metadata`

---

## Related Prompt Family

| File | Relationship |
|------|-------------|
| `test-providers-models.prompt.md` | References this sync prompt |
| `docs/sync-hermes-copilot-codex-issues-context.md` | Audit findings (this run) |
| `docs/sync-hermes-copilot-codex-fix-issues-context.md` | Fix plan & progress (Phase 2+) |
| `thoughts/plans/sync-hermes-copilot-codex-debug.md` | Detailed fix plan (Phase 2) |
