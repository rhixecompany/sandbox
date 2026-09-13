---
name: webhook-template
version: 1.0.0
description: Prompt template for webhook adapter routes (agent mode) using dot-notation payload access.
---

# Webhook Agent Prompt Template

## Purpose

This template is used by webhook adapter routes (`platforms.webhook.extra.routes.*.prompt`) to transform an incoming webhook payload into an agent prompt. It uses dot-notation (`{dot.notation}`) for nested payload access and includes the special `{__raw__}` token.

## Template Variables

- `{pull_request.title}` → `payload["pull_request"]["title"]`
- `{pull_request.user.login}` → nested user login
- `{repository.full_name}` → repo identifier
- `{number}` → PR / MR / issue number (from payload root or nested object, depending on event)
- `{action}` → event action (e.g. `opened`, `synchronize`, `edited`)
- `{ref}` → git reference for `push` events
- `{head_commit.message}` → commit message
- `{payload.labels}` → labels array (serialized if list; checked via `contains` operator in filters)
- `{payload.content}` → flat payload body content (for flat payloads without `payload` wrapper)

## Special Token

- `{__raw__}` → dumps the **entire payload** as indented JSON. Truncated at 4000 characters. Useful when the agent needs full context (e.g. generic monitoring alert) rather than a curated subset.

## Example Template (GitHub PR review — agent mode)

```yaml
prompt: |
  Review this pull request:
  Repository: {repository.full_name}
  PR #{number}: {pull_request.title}
  Author: {pull_request.user.login}
  URL: {pull_request.html_url}
  Diff URL: {pull_request.diff_url}
  Action: {action}
```

## Example Template with `{__raw__}` (monitoring / generic)

```yaml
prompt: |
  System alert: {__raw__}
  Please summarize and recommend action.
```

## Template Rendering Rules (verified from docs)

- Missing key → literal `{key}` preserved (no error raised, no exception thrown).
- Nested dict values → JSON-serialized; truncated at 2000 characters per nested value.
- Nested list values → JSON-serialized; `contains` filter checks membership.
- `deliver_extra` values use the **same syntax** (e.g. `repo: "{repository.full_name}"`, `pr_number: "{number}"`, `chat_id: "{match.telegram_chat_id}"`).

## Trusted vs Untrusted Use

- **Trusted route** (`github-pr`, internal CI): named fields preferred; `{__raw__}` used sparingly.
- **Untrusted route** (public issue webhook, external service): prefer named fields (`{issue.title}`) over `{__raw__}`; if `{__raw__}` needed, pair with narrow `filters` (e.g. `field: event`, `equals: push`) so only intended payloads reach the agent.

## Security Note (from docs warning)

> HMAC validates sender identity, not payload content. PR titles, commit messages, issue descriptions, and any upstream text are authored by arbitrary third parties and must be treated as untrusted. Template narrowly; prefer named fields over full payload dumps.
