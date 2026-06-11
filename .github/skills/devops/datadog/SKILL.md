---
name: datadog
title: Datadog
description: "Use when investigating production errors, tracing distributed requests, comparing error trends, checking service health, or tailing real-time logs in Datadog."
---

## datadog

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Datadog operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Datadog observability for debugging and incident triage. Search logs, query metrics, compare error trends, and check service health in real-time.

## When to Use

- Investigating production errors
- Tracing distributed requests
- Comparing error trends over time
- Checking service health status
- Tailing real-time error logs
- Finding log patterns and anomalies
- Tracing request IDs through system

## When NOT to Use

- Local development debugging (use systematic-debugging)
- Code-level debugging (use debugger instead)
- Offline analysis without Datadog access
- Non-production environments

## Workflow

### Phase 1: Access Datadog

- Log into Datadog dashboard
- Identify relevant service or environment
- Determine time range for investigation

### Phase 2: Search & Filter

- Search logs by keywords or patterns
- Filter by service, environment, level
- Narrow down to relevant entries

### Phase 3: Analyze Patterns

- Identify error trends
- Compare metrics across time periods
- Trace requests through system

### Phase 4: Take Action

- Document findings
- Create alerts if needed
- Escalate or fix issues

## Tools & References

- **Related Skills**: systematic-debugging
- **Datadog Dashboard**: https://app.datadoghq.com
- **Log Search**: Query syntax and filters
- **Metrics**: Performance and error tracking

## Best Practices

- Use specific time ranges for searches
- Filter by service and environment
- Look for patterns, not just individual errors
- Create dashboards for common queries
- Set up alerts for critical errors
- Document investigation findings
- Share dashboards with team
