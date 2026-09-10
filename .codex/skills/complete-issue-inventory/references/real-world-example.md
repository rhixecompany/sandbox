# Real-World Example: markdownlint-cli2 "Non-Blocking" Trap

## The Situation

Task: "Debug/fix all issues, errors, warnings" across a workspace.

Investigation found: `markdownlint-cli2` is configured but `bunx` download timed out on first run.

## The Wrong Summary

Writing "Remaining observations (non-blocking): X can't be installed" without attempting to fix it triggers a user correction.

## The Right Fix

1. **Re-try** — `bunx` caches after first download; a timeout is often transient
2. **Check config** — `globs: ["**/*.md"]` forced full-tree scans of 3399 files; removing it fixed performance
3. **Use `--no-globs`** — prevents config's `globs` from overruling CLI arguments
4. **Adjust thresholds** — MD025/MD028 disabled for template files where structure is intentional
5. **Fix actual issues** — add language specifiers to bare fenced code blocks

## Lesson

When the task is "fix ALL issues":
- A tool network timeout on first invocation is fixable by retrying
- Always look for config issues that compound the problem
- The user's expectation is zero issues = zero dismissals
