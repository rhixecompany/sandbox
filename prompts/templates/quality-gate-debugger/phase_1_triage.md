# Phase 1: Triage

> Extracted from `quality-gate-debugger.prompt.md`.

## Phase 1: Triage

Read all four report files. For each issue found, extract and classify:

### 1.1 — Parse Issues

For **every** error, warning, or problem, record:

- **File path** and **line number**
- **Error code** (e.g., `TS2307`, `react/no-unused-vars`, `NEXT_NOT_FOUND`)
- **Severity**: `error` | `warning` | `info`
- **Message**: the full error/warning text
- **Category**: `type-error` | `import-resolution` | `lint-rule` | `test-failure` | `build-error` | `deprecation` | `other`

### 1.2 — Deduplicate & Cluster

- Group issues that share the same root cause (e.g., 10 files all importing from a wrong path = 1 root cause).
- Identify cascading failures (a single missing export causing errors downstream).
- Count unique vs total occurrences per cluster.

### 1.3 — Priority Matrix

Present a triage summary table:

```
| # | Category          | Root Cause                        | Files | Severity | Fix Complexity |
|---|-------------------|-----------------------------------|-------|----------|----------------|
| 1 | import-resolution | comics/index.ts missing export    |    12 | error    | low            |
| 2 | type-error        | ActionResult generic mismatch     |     3 | error    | medium         |
| …                                                                                              |
```

Sort by: `error` before `warning`, then by file-count descending (highest impact first).
