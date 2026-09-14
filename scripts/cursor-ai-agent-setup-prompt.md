# Cursor AI Agent Setup Prompt

## Task

Set up Cursor AI Agent CLI and verify all features work: version check, agent mode, plan mode, prompt mode.

## Procedure

1. Install Cursor CLI (one of the three methods documented)
2. Add to PATH (shell config)
3. Verify: `cursor --version`, `cursor agent --help`, `cursor plan-mode --help`
4. Test prompt: `cursor agent --task "Explain Cursor setup"`
5. Check keyboard shortcuts reference
6. Report final summary

## Success Criterion

- `cursor --version` exits 0 with version string
- `cursor agent --help` exits 0
- `cursor plan-mode --help` exits 0
- No errors during setup

## Failure Reporting

If any step fails, report:

- Exact command that failed
- stdout/stderr output
- Exit code
- Suggested fix
