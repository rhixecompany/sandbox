---
author: Hermes Agent
description: Instrument a webapp to send useful telemetry data to Azure App Insights.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: appinsights-instrumentation
tags:
- azure
- appinsights
- observability
- telemetry
- instrumentation
title: AppInsights Instrumentation
version: 1.0.0

---
# AppInsights Instrumentation

## Overview

Instrument a webapp to send telemetry to Azure Application Insights. This skill supports ASP.NET Core, Node.js, Python, and general guidance for hosted web applications.

## When to Use

- Adding observability to a new or existing webapp
- Troubleshooting production incidents with telemetry
- Integrating automatic or manual App Insights instrumentation
- Verifying telemetry flows end to end after deployment

## When NOT to Use

- Non-web applications or console-only workloads
- Observability tooling that is not App Insights
-當 instrumentation should remain outside the product boundary

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Diagnose missed telemetry or broken SDK setup |
| `log-analysis-and-triage` | Cross-check logs against App Insights telemetry |

## Prerequisites

This workflow targets web applications. Confirm the app type before instrumenting.

- ASP.NET Core app hosted in Azure or container
- Node.js app hosted in Azure or container
- Python web app with supported hosting target

## Workflow

### Phase 1: Identify app context

1. Confirm programming language and framework.
2. Confirm hosting target: Azure App Service, container, Azure Container Apps, or local.
3. Review existing telemetry or monitoring configuration.
4. Identify supported instrumentation path: auto or manual.

### Phase 2: Use auto-instrumentation when possible

Prefer auto-instrumentation when the app is an ASP.NET Core app hosted in Azure App Service and the documented auto-instrumentation path applies.

1. Follow the auto-instrumentation reference for the environment.
2. Verify connection strings and resource targets.
3. Run validation checks and confirm telemetry appears in App Insights.

### Phase 3: Manual instrumentation

If auto-instrumentation is not applicable or the environment is different:

1. Create the App Insights resource in a meaningful resource group.
2. Configure the connection string or instrumentation key in the app.
3. Modify the app code using the SDK for the runtime.
4. Send representative request, dependency, exception, and custom telemetry.
5. Verify telemetry is flowing to the resource.

## Verification Checklist

- [ ] App type and hosting target confirmed
- [ ] Instrumentation method selected: auto or manual
- [ ] App Insights resource exists and target resource group is appropriate
- [ ] App updated to send telemetry
- [ ] Validation request produces expected telemetry
- [ ] Logs, requests, and exceptions visible in App Insights
- [ ] Instrumentation keys or connection strings are not hardcoded in public artifacts

## Pitfalls

- Skipping hosting-context confirmation often leads to choosing the wrong instrumentation method.
- Hardcoding instrumentation keys in public repositories or sample artifacts creates credential exposure risk.
- Validating only the first event may miss missing dependency or exception telemetry paths.
- Removing instrumentation without deleting related resources leaves orphan monitoring configuration.
