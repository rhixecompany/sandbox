# Multi-Language Script Projects (Class Pattern)

For projects consolidating scripts across shell, PowerShell, batch, and shared implementations.

## 6-Phase Execution Model

1. **AUDIT & INVENTORY** — Catalog all scripts, identify issues, verify dependencies
2. **DEBUG & FIX** — Resolve all issues found in Phase 1
3. **CONSOLIDATION** — Centralize logic (src/*.ts), standardize wrappers, enforce DRY
4. **ENHANCEMENT** — Document flags, environment variables, logging, exit codes
5. **EXECUTE & TEST** — Automated test suite (test-all.sh), 100% pass rate gate
6. **DOCUMENTATION** — PLAN.md, SPECS.md, README.md, SUMMARY.md, test suite

## Deliverables Structure

```
project/
├── PLAN.md          What needs to be done (phases, timeline, risks)
├── SPECS.md         How to build it (requirements, acceptance criteria per script)
├── README.md        How to use it (quick start, flags, examples, troubleshooting)
├── SUMMARY.md       Completion report (what was done, test results, metrics)
├── test-all.sh      Automated test suite
├── src/             TypeScript implementations (single source of truth)
└── logs/            Auto-created log directory
```
