# Hermes Diagnostic Report

Generated: 2026-09-10T19:48:21.545242+00:00
Total: 12 | OK: 10 | FAIL: 2

## Per-command

| # | Label | Exit | Elapsed (s) | OK |
|---|---|---|---|---|
| 1 | doctor | 0 | 45.9 | ✓ |
| 2 | doctor-fix | 0 | 36.78 | ✓ |
| 3 | security | 1 | 7.77 | ✗ |
| 4 | status | 0 | 14.39 | ✓ |
| 5 | insights | 0 | 3.23 | ✓ |
| 6 | logs-list | 0 | 2.52 | ✓ |
| 7 | logs-errors | 0 | 1.74 | ✓ |
| 8 | logs-desktop | 0 | 1.63 | ✓ |
| 9 | logs-gateway | 0 | 1.53 | ✓ |
| 10 | logs-gui | 0 | 1.73 | ✓ |
| 11 | logs-agent | 0 | 3.48 | ✓ |
| 12 | bun-run-check | 2 | 1.12 | ✗ |

## Failures (stderr tail)
### security
```

```
### bun-run-check
```
hedDefaultResolve (node:internal/modules/esm/loader:708:20)
    at #resolveAndMaybeBlockOnLoaderThread (node:internal/modules/esm/loader:728:38)
    at ModuleLoader.resolveSync (node:internal/modules/esm/loader:766:56)
    at #resolve (node:internal/modules/esm/loader:690:17)
    at ModuleLoader.getOrCreateModuleJob (node:internal/modules/esm/loader:610:35)
    at ModuleJob.syncLink (node:internal/modules/esm/module_job:277:33)
    at ModuleJob.link (node:internal/modules/esm/module_job:389:17)

```