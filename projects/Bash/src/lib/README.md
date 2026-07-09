# Bash/src/lib/ — Shared TypeScript Utilities

This directory contains shared TypeScript modules used by all Bash script implementations.

## Modules

| File | Purpose |
| --- | --- |
| `colors.ts` | Terminal color output (red, green, yellow, blue, cyan, magenta, bold, dim) with auto-detection of TTY and `NO_COLOR` support |
| `logging.ts` | Logging with log levels (debug/info/warn/error), timestamps, and optional file logging via `FileLogger` |
| `errors.ts` | Error types (`ScriptError`, `UsageError`) and `safeExec()` wrapper for consistent exit codes |
| `cli.ts` | CLI argument parsing (`parseArgs`) and `showHelp()` for usage text |

## Usage

```typescript
import { ok, fail, warn, info } from "./lib/colors.js";
import { log } from "./lib/logging.js";
import { safeExec, UsageError } from "./lib/errors.js";
import { parseArgs, showHelp } from "./lib/cli.js";
```
