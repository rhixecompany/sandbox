---
author: Hermes Agent
description: Use when investigating production errors, tracing distributed requests,
  comparing error trends, checking service health, or tailing real-time logs in Datadog.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: datadog
tags:
- observability
- debugging
- monitoring
- datadog
- production
title: Datadog
version: 1.0.0

---
# Datadog

## Overview

Use Datadog for observability, production debugging, and incident triage. Search logs, query metrics, compare error trends, check service health, and trace requests through distributed systems.

## When to Use

- Investigating production errors and incidents
- Tracing distributed requests across services
- Comparing error trends over time
- Checking service health status
- Tailing real-time error logs
- Finding log patterns and anomalies
- Creating alerts for critical conditions

## When NOT TO Use

- Local development debugging (use systematic-debugging)
- Code-level debugging (use a debugger)
- Offline analysis without Datadog access
- Non-production environments (use structured logging locally)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug production issues methodically |
| `log-analysis-and-triage` | Analyze and prioritize log patterns |

## Workflow

### Phase 1: Access & Scope

1. Log into Datadog dashboard (https://app.datadoghq.com)
2. Identify the relevant service, environment, and time range
3. Start with a broad search, then narrow down

### Phase 2: Search & Filter

**Log Search:**
```
# Search by service and error level
service:web-api status:error

# Search by trace ID
trace_id:abc123

# Search by custom tags
env:production team:backend

# Full-text search
"OutOfMemoryError"
```

**Common filters:**
- `service:<name>` — Filter by service
- `env:<environment>` — Filter by environment
- `status:error|warn` — Filter by log level
- `@host:<hostname>` — Filter by host
- `#tag:value` — Filter by custom tags

### Phase 3: Analyze Patterns

1. Use **Log Patterns** to group similar log entries
2. Compare metrics across time periods (1h, 24h, 7d)
3. Check **Service Map** for dependency health
4. Use **APM Traces** to follow requests through the system
5. Review **Dashboards** for high-level health indicators

### Phase 4: Take Action

1. Document findings with specific log examples
2. Create or update alerts for recurring issues
3. Escalate to on-call if critical
4. Create tickets for non-urgent fixes

## Verification Checklist

- [ ] Time range set correctly for the incident
- [ ] Filters applied to narrow results
- [ ] Error patterns identified and grouped
- [ ] Root cause traced through services
- [ ] Findings documented with evidence
- [ ] Alerts created/updated if needed

## Pitfalls

- **Too broad a time range:** Start narrow (last 15-60 min) and expand
- **Ignoring correlation IDs:** Use trace IDs to follow requests across services
- **Missing the service map:** Visual dependency view often reveals the issue faster than log search
- **Not saving queries:** Save frequently-used searches as dashboard widgets
- **Alert fatigue:** Don't create alerts for every error — focus on actionable, high-signal conditions
