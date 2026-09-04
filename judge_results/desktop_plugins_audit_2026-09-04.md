# Hermes Desktop-Plugins Audit — 2026-09-04

**Scope:** `C:\Users\Alexa\AppData\Local\hermes\desktop-plugins\`
**Auditor:** Subagent (depth 1)
**Date:** 2026-09-04

---

## Summary

- 8 directories found under `desktop-plugins/`
- **5** had a valid runtime `plugin.js` (1 with a double-import bug, now fixed)
- **3** were non-plugin pollution (git clone, state dump, repo mirror) — moved to `_quarantine/`
- All 5 remaining plugins pass `node --check`
- 1 remaining issue: 2 hardcoded color classes (`text-red-500`, `bg-green-500`, `bg-gray-500`) violate the "no hardcoded colors — use theme vars" rule

---

## Inventory: Before vs After

### Before (8 entries)

| # | Directory | plugin.js | Type | Status |
|---|-----------|-----------|------|--------|
| 1 | `awesome-hermes-agent/` | ❌ missing | Upstream git clone (docs/LICENSE/media/.git only) | INVALID |
| 2 | `cli-tools-panel/` | ✅ 6091 B | Real plugin | OK |
| 3 | `hermes-achievements/` | ❌ missing | State-file dump (scan_checkpoint.json, scan_snapshot.json, state.json) | INVALID |
| 4 | `hermes-status-monitor/` | ✅ 5479 B | Real plugin | OK |
| 5 | `mindstudio-agent/` | ❌ missing | Full repo clone (src/, dist/, node_modules/, CLAUDE.md, install scripts) | INVALID |
| 6 | `session-manager/` | ✅ 7933 B | Real plugin | DOUBLE IMPORT BUG |
| 7 | `skills-browser/` | ✅ 8165 B | Real plugin | OK |
| 8 | `telegram-quick-actions/` | ✅ 8018 B | Real plugin | DOUBLE IMPORT BUG |

### After (5 valid + 3 quarantined)

```
desktop-plugins/
├── _quarantine/
│   ├── awesome-hermes-agent/   ← moved 2026-09-04
│   ├── hermes-achievements/    ← moved 2026-09-04
│   └── mindstudio-agent/       ← moved 2026-09-04
├── cli-tools-panel/plugin.js
├── hermes-status-monitor/plugin.js
├── session-manager/plugin.js   ← bug fixed 2026-09-04
├── skills-browser/plugin.js
└── telegram-quick-actions/plugin.js  ← bug fixed 2026-09-04
```

`mv` verified via post-move `ls -la` — all 3 dirs present at `_quarantine/<name>/`, none deleted.

---

## Action 1: Quarantine (completed)

Three dirs moved (not deleted) to `desktop-plugins/_quarantine/`:

| Quarantined dir | Reason | Real plugin entry? |
|---|---|---|
| `awesome-hermes-agent/` | Git clone of upstream awesome-list repo (CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE, README.md, media/) — no Hermes plugin code | No |
| `hermes-achievements/` | State-file dump (scan_checkpoint.json, scan_snapshot.json, state.json) — no plugin code | No |
| `mindstudio-agent/` | Full `@mindstudio-ai/agent` repo clone (CLAUDE.md, src/, dist/, node_modules/, tsup.config.ts, install scripts) | **Flag for human review** — see below |

### ⚠ Flag for human review: `mindstudio-agent/dist/index.js`

The quarantined `mindstudio-agent` repo has `dist/index.js` and `src/index.ts` that `export default mindstudio` (an SDK object exposing `auth`, `db`, `RateLimiter`, etc.). It does **not** match the desktop-plugin shape `{ id, name, register(ctx) }` — it's a MindStudio HTTP SDK, not a pane/chip desktop plugin. So nothing in there is a valid desktop plugin entry today.

If a future mindstudio desktop pane is desired, a new `mindstudio-pane/plugin.js` should be authored from scratch (with the proper `register(ctx)` shape) — do NOT symlink or alias to the SDK. **No action taken automatically.**

---

## Action 2: Double-import bug fix (completed)

### Bug

Both `session-manager/plugin.js` and `telegram-quick-actions/plugin.js` had:

```js
import { jsx: jsxRuntime, jsxs: jsxsRuntime } from 'react/jsx-runtime'
```

The aliases `jsxRuntime` / `jsxsRuntime` were imported but never referenced anywhere in either file. All `jsx(...)` / `jsxs(...)` calls in those files already come from the `@hermes/plugin-sdk` import on the line above.

### Verification

Grep against each patched file — `jsxRuntime`/`jsxsRuntime` no longer appear anywhere. Both files now rely solely on the SDK's `jsx`/`jsxs` exports (which is the canonical pattern, also used by `cli-tools-panel` and `skills-browser`).

Note: `hermes-status-monitor/plugin.js` already imports `jsx, jsxs` from `react/jsx-runtime` directly (different but valid pattern) — not changed.

### Files patched

| File | Line removed | Status |
|---|---|---|
| `session-manager/plugin.js` | line 9 (was the spurious import) | ✅ `node --check` passes |
| `telegram-quick-actions/plugin.js` | line 8 (was the spurious import) | ✅ `node --check` passes |

Patches applied via the `patch` tool with auto-lint; both reported `lint: { status: ok }`.

---

## Action 3: Per-plugin audit (5 valid plugins)

For each of the 5 remaining plugins, I checked: SDK imports resolve, `export default` shape, `ctx.register` calls, hardcoded colors.

### 3.1 `cli-tools-panel/plugin.js` (6091 B)

| Check | Result |
|---|---|
| `@hermes/plugin-sdk` imports | `{ cn, haptic, host, Tip, useValue, Button, useMutation, jsx, jsxs }` — all valid SDK names |
| Other imports | `import React from 'react'` — fine |
| `export default` | ✅ `{ id: 'cli-tools-panel', name: 'CLI Tools Panel', register(ctx) { ... } }` |
| `ctx.register` calls | 2 — both pass plain objects with `id`, `area`, `title`, `data`, `render` |
| Hardcoded colors | None — uses `text-(--ui-text-primary)`, `bg-(--chrome-action-hover)`, etc. |
| `node --check` | ✅ SYNTAX_OK |

### 3.2 `hermes-status-monitor/plugin.js` (5479 B)

| Check | Result |
|---|---|
| `@hermes/plugin-sdk` imports | `{ cn, haptic, host, Tip, useValue, StatusDot, Button }` — all valid |
| Other imports | `import { jsx, jsxs } from 'react/jsx-runtime'` — valid direct pattern |
| `export default` | ✅ `{ id: 'hermes-status-monitor', name: 'Hermes Status Monitor', register(ctx) { ... } }` |
| `ctx.register` calls | 2 — `status-pane` + `status-chip` |
| Hardcoded colors | None — all theme vars |
| `node --check` | ✅ SYNTAX_OK |

### 3.3 `session-manager/plugin.js` (7933 B, bug fixed)

| Check | Result |
|---|---|
| `@hermes/plugin-sdk` imports | `{ cn, haptic, host, Tip, useValue, Button, useQuery, useMutation, jsx, jsxs }` — all valid |
| Other imports | `import React from 'react'` — fine; spurious `jsx-runtime` import removed |
| `export default` | ✅ `{ id: 'session-manager', name: 'Session Manager', register(ctx) { ... } }` |
| `ctx.register` calls | 2 — `session-pane` + `session-chip` |
| Hardcoded colors | ⚠ **3 hits** — see Issue #1 below |
| `node --check` | ✅ SYNTAX_OK |

### 3.4 `skills-browser/plugin.js` (8165 B)

| Check | Result |
|---|---|
| `@hermes/plugin-sdk` imports | `{ cn, haptic, host, Tip, useValue, Button, Input, useQuery, useMutation, jsx, jsxs }` — all valid |
| Other imports | `import React from 'react'` — fine |
| `export default` | ✅ `{ id: 'skills-browser', name: 'Skills Browser', register(ctx) { ... } }` |
| `ctx.register` calls | 2 — `skills-pane` + `skills-chip` |
| Hardcoded colors | ⚠ **1 hit** — see Issue #1 below |
| `node --check` | ✅ SYNTAX_OK |

### 3.5 `telegram-quick-actions/plugin.js` (8018 B, bug fixed)

| Check | Result |
|---|---|
| `@hermes/plugin-sdk` imports | `{ cn, haptic, host, Tip, useValue, Button, Input, Dialog, jsx, jsxs }` — all valid; **`Dialog` is imported but never used** — see Issue #2 |
| Other imports | Spurious `jsx-runtime` import removed |
| `export default` | ✅ `{ id: 'telegram-quick-actions', name: 'Telegram Quick Actions', register(ctx) { ... } }` |
| `ctx.register` calls | 2 — `telegram-pane` + `telegram-chip` |
| Hardcoded colors | None — all theme vars |
| `node --check` | ✅ SYNTAX_OK |

---

## Remaining Issues (for human review)

### Issue #1 — Hardcoded color classes (skill-rule violation)

Per the "no hardcoded colors — use theme vars" rule, these should be replaced with theme variables like `text-(--ui-error)`, `text-(--ui-success)`, `bg-(--ui-text-tertiary)`, etc.

| File | Line | Class | Suggested replacement |
|---|---|---|---|
| `session-manager/plugin.js` | 61 | `'p-3 text-red-500'` | `text-(--ui-error)` |
| `session-manager/plugin.js` | 105 | `'bg-green-500'` (active status dot) | `bg-(--ui-success)` |
| `session-manager/plugin.js` | 105 | `'bg-gray-500'` (inactive status dot) | `bg-(--ui-text-tertiary)` |
| `session-manager/plugin.js` | 141 | `'text-red-500 hover:bg-red-500/10'` | `text-(--ui-error) hover:bg-(--ui-error)/10` |
| `skills-browser/plugin.js` | 138 | `'text-red-500 hover:bg-red-500/10'` | `text-(--ui-error) hover:bg-(--ui-error)/10` |

**Why not fixed in this pass:** Theme-variable naming convention (`--ui-error`, `--ui-success`, exact token spelling) should be confirmed against the live `@hermes/plugin-sdk` theme manifest before bulk-substituting. The skill rule was applied via grep but not auto-patched, to avoid silently inventing token names.

### Issue #2 — Unused SDK import

`telegram-quick-actions/plugin.js` line 7 imports `Dialog` from `@hermes/plugin-sdk` but never uses it. Likely leftover from a draft modal that was replaced by inline state. Safe to drop, but no runtime impact — left for human review to confirm intent (might be used in upcoming work).

### Issue #3 — `mindstudio-agent` quarantine (re-flagged)

See "Flag for human review" under Action 1. If a `mindstudio-pane` desktop plugin is desired, author it as a new plugin; do not promote the SDK into the desktop-plugin dir.

---

## Verification log

```
ls -la desktop-plugins/        → 5 plugins + _quarantine
ls -la desktop-plugins/_quarantine/ → awesome-hermes-agent, hermes-achievements, mindstudio-agent
node --check session-manager/plugin.js              → SYNTAX_OK
node --check telegram-quick-actions/plugin.js       → SYNTAX_OK
node --check cli-tools-panel/plugin.js              → SYNTAX_OK
node --check hermes-status-monitor/plugin.js        → SYNTAX_OK
node --check skills-browser/plugin.js               → SYNTAX_OK
grep "jsxRuntime|jsxsRuntime" session-manager/plugin.js         → no matches
grep "jsxRuntime|jsxsRuntime" telegram-quick-actions/plugin.js  → no matches
grep -E "text-red-|text-green-|bg-red-|bg-green-|bg-gray-" → 5 hits (listed above)
```

Nothing deleted — only `mv` operations and line-level edits on two `plugin.js` files.

---

## Files modified

- `C:\Users\Alexa\AppData\Local\hermes\desktop-plugins\session-manager\plugin.js` (removed 1 line)
- `C:\Users\Alexa\AppData\Local\hermes\desktop-plugins\telegram-quick-actions\plugin.js` (removed 1 line)

## Files moved (not deleted)

- `desktop-plugins/awesome-hermes-agent/` → `desktop-plugins/_quarantine/awesome-hermes-agent/`
- `desktop-plugins/hermes-achievements/` → `desktop-plugins/_quarantine/hermes-achievements/`
- `desktop-plugins/mindstudio-agent/` → `desktop-plugins/_quarantine/mindstudio-agent/`

## Files created

- `C:\Users\Alexa\Desktop\SandBox\judge_results\desktop_plugins_audit_2026-09-04.md` (this report)
