# Phase 0: Generate Reports

> Extracted from `quality-gate-debugger.prompt.md`.

## Phase 0: Generate Reports

**Before anything else**, run the quality-gate script to produce fresh report files.

Detect the shell and run the appropriate script from the project root:

```powershell
# Windows / PowerShell
pwsh -NoProfile -File ./quality-gate.ps1 -ContinueOnError -Json
```

```bash
# macOS / Linux
bash quality-gate.sh --continue-on-error --json
```

Wait for the script to complete. This produces:

| File                | Source Command     |
| ------------------- | ------------------ |
| `type-check.txt`    | `pnpm type-check`  |
| `lint-fixed.txt`    | `pnpm lint:fix`    |
| `test-report.txt`   | `pnpm test --run`  |
| `build-report.txt`  | `pnpm build:debug` |
| `quality-gate.json` | Summary (JSON)     |

If the script is missing or fails to run, fall back to running each command manually and capturing output to the corresponding `.txt` file. Proceed with whatever report files exist.

### Important: Fail-Fast Behavior

As of v2.1, the quality-gate scripts employ **fail-fast logic**:

- ✅ **Phase 0** runs and completes normally (all 4 gates)
- ⚠️ **Subsequent runs** will STOP immediately after the first gate failure

This means:

- If `type-check` fails, `lint`, `test`, and `build` won't run
- If `lint` fails, `test` and `build` won't run
- Etc.

**You will need to re-run the script after each fix cluster** to see the next gate's status.

This is intentional: it prevents cascading errors and focuses your attention on fixing one thing at a time.
