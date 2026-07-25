---
author: Hermes Agent
description: Guides the Copilot CLI on how to use the WorkIQ CLI/MCP server to query Microsoft 365 Copilot data (emails, meetings, docs, Teams, people) for live context, summaries, and recommendations.
license: MIT
metadata:
  hermes:
    tags: [imported, m365, copilot, workiq, productivity, mcp]
name: workiq-copilot
tags:
- imported
- m365
- copilot
- workiq
- productivity
- mcp
- scripts
title: WorkIQ Copilot
version: 1.1.0
---

# WorkIQ Copilot Skill

## Overview

WorkIQ (Public Preview) lets Copilot query Microsoft 365 data with natural language. It supports schedules, documents, Teams messages, email threads, follow-up tracking, stakeholder summaries, and more. Use this skill whenever a task needs live organizational intelligence beyond the local repository.

## When to Use

- Querying calendar, emails, documents, or Teams for live organizational data
- Summarizing meetings, tracking action items, finding documents
- People/project search within Microsoft 365 tenant
- Needing real-time organizational context for planning or decisions

## When NOT to Use

- Local repository-only tasks (code, files, git)
- Non-Microsoft 365 environments
- Tasks not requiring live org data

## Supported Data & Sample Prompts

| Data Type | Sample Prompts |
|-----------|----------------|
| **Emails** | "Summarize emails from Sarah about the budget" |
| **Meetings** | "What are my upcoming meetings this week?" |
| **Documents** | "Find recent documents about Q4 planning" |
| **Teams** | "Summarize messages in the Engineering channel today" |
| **People/Projects** | "Who is working on Project Alpha?" |

## Getting Access

### Option 1: Copilot CLI Plugin (Preferred)

```bash
copilot
/plugin marketplace add github/copilot-plugins
/plugin install workiq@copilot-plugins
# Restart Copilot CLI
```

### Option 2: Standalone CLI / MCP Server

```bash
npm install -g @microsoft/workiq
# or
npx -y @microsoft/workiq mcp
# Run MCP server
workiq mcp
```

### Option 3: Tenant Consent

First use prompts for Microsoft 365 admin consent (EULA + permissions). Non-admins must contact tenant admin to approve per the Tenant Administrator Enablement Guide.

## Pre-flight Checklist

- [ ] Run `Get-Command workiq` to ensure binary is available
- [ ] Accept EULA once via `workiq accept-eula`
- [ ] Confirm correct tenant (`-t <tenant-id>` if different from `common`)
- [ ] Be ready to complete device login in browser when prompted

## Workflow

### Phase 1: Clarify Intent

Determine the query type:
- **Agenda** — "What's on my calendar tomorrow?"
- **Action items** — "Summarize follow-ups from today's customer sync"
- **Documents** — "List PowerPoints about Contoso FY26 roadmap"
- **Communications** — "What did my manager say about the deadline?"
- **Insights** — "What blockers came up in the last three meetings?"
- **Planning** — "Suggest focus blocks for Tuesday afternoon"

### Phase 2: Craft Precise Prompt

Include timeframe, source, or topic for best results:
```
"Summarize Teams posts in #eng for today"
"Find emails from @manager about deadline in last week"
"Action items from Monday's planning meeting"
```

### Phase 3: Run Command

```bash
# Single question
workiq ask --question "What's on my calendar tomorrow?"

# With specific tenant
workiq ask -t mycompany.onmicrosoft.com -q "List Q4 planning docs"

# Interactive mode
workiq ask
```

### Phase 4: Monitor Execution

Long answers may stream — wait for completion before additional requests.

### Phase 5: Summarize & Redact

- Keep summaries concise (2–3 sentences): load, priorities, blockers, next steps
- Refer to meetings/documents generically unless user needs links
- Mention if WorkIQ can continue (e.g., "WorkIQ can show Thu–Sun if needed")
- Map WorkIQ's suggested actions to clear offers (block time, send follow-up, request recording, run deeper query)

### Phase 6: Offer Follow-ups

- Block focus/overflow holds at suggested times
- Draft reschedule/decline messages referencing WorkIQ guidance
- Request recordings or summaries for overlapping sessions
- Capture action items into task trackers
- Run additional WorkIQ queries (by project, stakeholder, time range) for deeper analysis

## Command Reference

| Command | Purpose |
|---------|---------|
| `workiq --help` | Show global options |
| `workiq version` | Display installed version |
| `workiq accept-eula` | Accept license (first use) |
| `workiq ask` | Interactive mode |
| `workiq ask --question "..."` | Ask specific question (`-q` shorthand) |
| `workiq ask -t <tenant> -q "..."` | Target specific tenant |
| `workiq mcp` | Start MCP stdio server |

## Prompt Patterns

| Intent | Prompt Template |
|--------|-----------------|
| Agenda | "What's on my calendar [tomorrow/this week]?" |
| Action Items | "Summarize follow-ups from [meeting/timeframe]" |
| Documents | "List [format] documents about [topic]" |
| Communications | "What did [person] say about [topic]?" |
| Insights | "What blockers came up in [timeframe]?" |
| Planning | "Suggest focus blocks for [day/time]" |

## Response Guidelines

- Keep summaries concise (2–3 sentences): load, priorities, blockers, optional next steps
- Refer to meetings/documents generically unless user specifically needs links
- Mention if WorkIQ can continue (e.g., "WorkIQ can show Thu–Sun if needed")
- Map WorkIQ's suggested actions to clear offers (block time, send follow-up, request recording, run deeper query)

## Best Practices

- Prefer narrow prompts to reduce noise; run multiple queries if needed
- Combine outputs logically (agenda + conflicts + action items) before responding
- Respect privacy: do not expose attendee lists or confidential snippets unless explicitly requested
- Log which commands were run so future steps can reference them
- Use MCP mode (`workiq mcp`) when another agent/workflow needs direct tool access

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Missing CLI | Install via npm or ensure PATH is set; notify user if unavailable |
| Consent/auth errors | Re-run command after admin grants permissions or after completing device login |
| Long/incomplete output | Rerun with refined scope or ask for specific data slices (per day/project/person) |
| Command hanging | Cancel with Ctrl+C or restart Copilot CLI session, then retry; ensure browser login completed |

## Follow-up Actions to Offer

- Block focus/overflow holds at suggested times
- Draft reschedule/decline messages referencing WorkIQ guidance
- Request recordings or summaries for overlapping sessions
- Capture action items into task trackers
- Run additional WorkIQ queries (by project, stakeholder, time range) for deeper analysis

## Verification Checklist

- [ ] Pre-flight checklist completed
- [ ] Intent clarified and prompt crafted
- [ ] Command executed successfully
- [ ] Response summarized concisely
- [ ] Follow-up actions offered
- [ ] Commands logged for future reference

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `copilot-sdk` | Copilot integration |
| `mcp` | MCP server management |

## Related Skills

- `copilot-cli-quickstart` — Learn Copilot CLI basics
- `copilot-sdk` — Embed Copilot in applications
- `mcp` — MCP server management

## Usage Examples

```bash
# Quick agenda
workiq ask -q "What's on my calendar tomorrow?"

# Action items from meeting
workiq ask -q "Summarize action items from today's standup"

# Document search
workiq ask -q "Find PowerPoints about FY26 roadmap"

# Teams channel summary
workiq ask -q "Summarize #engineering channel today"

# People search
workiq ask -q "Who is working on Project Alpha?"

# Multi-tenant
workiq ask -t other-tenant.onmicrosoft.com -q "Agenda for Monday"
```

## Error Handling

- **CLI not found:** Exits with code 127, prints installation instructions
- **Auth required:** Prints device code URL, waits for browser completion
- **Tenant mismatch:** Warns, uses default `common` tenant
- **Rate limit:** Backs off with exponential delay, retries up to 3 times
- **Timeout:** Uses `--timeout` flag (default 30s), exits with code 124

## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
- **Tenant boundaries:** Data is tenant-scoped — cross-tenant queries need explicit `-t` flags
- **Permission scope:** Only data user has access to is returned — no admin override
- **Streaming responses:** May arrive in chunks — wait for `session.idle` before next query

## References

- WorkIQ GitHub: <https://github.com/microsoft/workiq>
- M365 Admin Consent: <https://learn.microsoft.com/microsoft-365/admin/manage/consent-requests>
- `references/workiq-prompt-patterns.md` — Additional prompt templates
- `references/workiq-mcp-config.md` — MCP server configuration