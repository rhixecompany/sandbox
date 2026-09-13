# Webhook Routes Config — Reference (verified from docs)

> This file is a reference document, not an active `config.yaml`. It documents the 3 live routes configured for this repo: `github-pr`, `deploy-notify`, `oom-emergency`. The user applies these to `~/.hermes/config.yaml` manually; secrets are configured in `~/.hermes/.env`.

## Environment Variables (`.env` snippet — see `.env.webhook-example`)

```
WEBHOOK_ENABLED=true
WEBHOOK_PORT=8644
WEBHOOK_SECRET=global-fallback-secret-placeholder  # replace in production
```

## Route Definitions (3 live routes — none use `INSECURE_NO_AUTH`)

### Route 1: `github-pr` (agent mode — GitHub PR review)

```yaml
routes:
  github-pr:
    events: ["pull_request"]
    secret: "github-webhook-secret"   # real HMAC secret (not placeholder in prod)
    profile: "default"
    prompt: |
      Review this pull request:
      Repository: {repository.full_name}
      PR #{number}: {pull_request.title}
      Author: {pull_request.user.login}
      URL: {pull_request.html_url}
      Diff URL: {pull_request.diff_url}
      Action: {action}
    skills: ["github-code-review"]
    deliver: "github_comment"
    deliver_extra:
      repo: "{repository.full_name}"
      pr_number: "{number}"
```

### Route 2: `deploy-notify` (direct delivery mode — monitoring push notification)

```yaml
routes:
  deploy-notify:
    events: ["push"]
    secret: "deploy-secret"
    profile: "default"
    prompt: "New push to {repository.full_name} branch {ref}: {head_commit.message}"
    filters:
      - field: "ref"
        equals: "refs/heads/main"
    deliver: "telegram"
    deliver_only: true
    deliver_extra:
      chat_id: "-100123456789"  # replace with real chat ID in production
```

Notes:
- `deliver_only: true` skips agent; zero LLM cost; sub-second delivery.
- `deliver` is real (`telegram`), not `log` — adapter requires this.
- `filters` ensures only pushes to `refs/heads/main` trigger delivery.

### Route 3: `oom-emergency` (trusted route — elevated toolset granted manually)

```yaml
routes:
  oom-emergency:
    events: ["monitor"]
    secret: "monitor-secret"
    profile: "default"
    prompt: "Memory emergency: {detail}. Diagnose with ps/free/py-spy and report."
    skills: ["system-monitoring"]
    toolsets: ["terminal", "file", "code_execution", "web"]
    deliver: "telegram"
    deliver_extra:
      chat_id: "-100987654321"
```

Notes:
- `toolsets` granted ONLY to this trusted route; not settable via `hermes webhook subscribe` (manual edit only — prevents self-grant at runtime).
- Route sends to `telegram`; if `chat_id` missing in `deliver_extra`, falls back to platform home channel.
- Secret is real HMAC; never `"INSECURE_NO_AUTH"`; adapter binds to loopback by default but refuses non-loopback + no-auth combo.

## Dynamic Subscriptions File Example (`~/.hermes/webhook_subscriptions.json`)

See `.env.webhook-example` and `webhook_subscriptions-example.json` for live dynamic subscriptions matching these routes.
