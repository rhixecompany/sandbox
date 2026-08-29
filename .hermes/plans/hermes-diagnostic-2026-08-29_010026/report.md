# Hermes Diagnostic Report

Generated: 2026-08-29T01:01:53.946795+00:00
Total: 11 | OK: 10 | FAIL: 1

## Per-command

| # | Label | Exit | Elapsed (s) | OK |
|---|---|---|---|---|
| 1 | doctor | 0 | 43.33 | ✓ |
| 2 | security | 0 | 3.37 | ✓ |
| 3 | status | 0 | 6.47 | ✓ |
| 4 | insights | 0 | 4.64 | ✓ |
| 5 | logs-list | 0 | 1.44 | ✓ |
| 6 | logs-errors | 0 | 1.58 | ✓ |
| 7 | logs-desktop | 0 | 1.25 | ✓ |
| 8 | logs-gateway | 0 | 1.47 | ✓ |
| 9 | logs-gui | 0 | 1.39 | ✓ |
| 10 | logs-agent | 0 | 1.21 | ✓ |
| 11 | bun-run-check | 1 | 21.55 | ✗ |

## Failures (stderr tail)
### bun-run-check
```
$ bun run lint && bun run format:check && bun run markdownlint && bun run spellcheck
$ eslint . --no-error-on-unmatched-pattern
$ prettier --check --ignore-unknown .
[[33mwarn[39m] .codex/mcp.json
[[33mwarn[39m] Code style issues found in the above file. Run Prettier with --write to fix.
error: script "format:check" exited with code 1
error: script "check" exited with code 1

```