# Subagent Path Resolution Pitfall

## Observed (2026-07-24 — agents-system-prompt-context-fix run)

When dispatching 3+ subagents to generate blueprint docs for project subdirectories,
subagents wrote files to `projects/<name>/docs/Project_Architecture/` instead of
`docs/Project_Architecture/`. The context said:

```
Write to: docs/Project_Architecture/<project>_architecture.md
```

But subagents ran from `projects/<name>/`, so the relative path resolved to
`projects/<name>/docs/Project_Architecture/` on disk.

## Root Cause

`delegate_task` subagents inherit their working directory from the dispatch
context. When dispatching a task for `projects/Bash/`, the CWD is `projects/Bash/`,
not the workspace root `~/Desktop/SandBox/`.

## Fix

Always pass fully-qualified absolute paths in the `context` string:

```
Context should say:
    TARGET_DIR: /c/Users/Alexa/Desktop/SandBox/docs/Project_Architecture/

NOT:
    TARGET_DIR: docs/Project_Architecture/
```

## Detection

A subagent self-report that says "wrote to docs/Project_Architecture/file.md"
with file sizes in the 7-18 KB range may still be at the wrong path. Always
verify with:

```bash
ls -la /c/Users/Alexa/Desktop/SandBox/docs/Project_Architecture/<project>_architecture.md
```

If the file doesn't exist there, search:

```bash
find /c/Users/Alexa/Desktop/SandBox/projects -name "*<project>*" -path "*/Project_Architecture/*"
```

## Recovery

```bash
# Find misplaced files
find /c/Users/Alexa/Desktop/SandBox/projects -name "*_architecture.md" -path "*/Project_Architecture/*"

# Copy to correct location
cp <wrong_path> /c/Users/Alexa/Desktop/SandBox/docs/Project_Architecture/

# Mirror to projects/ subdirectory
cp /c/Users/Alexa/Desktop/SandBox/docs/Project_Architecture/<file>.md \
   /c/Users/Alexa/Desktop/SandBox/docs/Project_Architecture/projects/<project>/
```
