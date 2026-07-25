---
author: Hermes Agent
description: Use when needing to inspect dependency/library source code for debugging
  implementation details, understanding SDK behavior, or investigating library bugs.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: clonedeps
tags:
- debugging
- dependencies
- source-inspection
- libraries
title: Clone Dependencies
version: 1.0.0

---
# Clone Dependencies

## Overview

Clone project dependency source code into an ignored local workspace for inspection. This enables reading library internals, understanding SDK/framework behavior from source, debugging implementation details, and investigating library bugs.

## When to Use

- A library behaves unexpectedly and you need to read its source
- Debugging a bug that may be in a dependency
- Understanding how an SDK's internal methods work
- Investigating a library's edge cases not documented in API docs
- Learning how a framework works internally
- Verifying a dependency's security or behavior

## When NOT to Use

- Simple API/docs questions — check context7 or official docs first
- Standard library usage — read docs instead of source
- Quick reference lookups — use grep/search on npm/GitHub
- When the dependency is well-documented and behavior matches docs

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Trace bugs through dependency source |
| `context7` | Look up library API docs before cloning |

## Workflow

### Phase 1: Identify Dependencies to Inspect

1. List project dependencies:
   ```bash
   # Node.js
   cat package.json | grep -A 50 '"dependencies"'
   # Also check devDependencies
   cat package.json | grep -A 50 '"devDependencies"'

   # Python
   cat requirements.txt
   # or
   pip freeze

   # Go
   cat go.mod

   # Rust
   cat Cargo.toml
   ```

2. Identify which dependency needs source inspection
3. Find the library's source repository URL (usually on GitHub)
4. Determine the specific version/tag to clone:
   ```bash
   # Node.js - check installed version
   cat node_modules/<pkg>/package.json | grep version

   # Python - check installed version
   pip show <pkg>
   ```

### Phase 2: Clone to Workspace

1. Create an ignored workspace directory:
   ```bash
   mkdir -p .deps-source
   # Ensure it's in .gitignore
   grep -q ".deps-source" .gitignore || echo ".deps-source/" >> .gitignore
   ```

2. Clone the dependency repository:
   ```bash
   cd .deps-source
   git clone https://github.com/<owner>/<repo>.git

   # Clone specific version tag
   git clone --branch v2.1.0 https://github.com/<owner>/<repo>.git

   # Or clone specific commit
   git clone https://github.com/<owner>/<repo>.git
   cd <repo>
   git checkout <commit-sha>
   ```

3. Verify the clone matches the installed version:
   ```bash
   cat <repo>/package.json | grep version  # Node.js
   cat <repo>/setup.py | grep version      # Python
   ```

### Phase 3: Inspect & Understand

1. Navigate the source structure:
   ```bash
   # Understand the project layout
   ls -la <repo>/
   # Find the main source directory
   find <repo>/src -name "*.ts" -o -name "*.js" | head -20
   ```

2. Read the specific code causing issues:
   ```bash
   # Search for the function/method in question
   grep -r "functionName" <repo>/src/

   # Read the implementation
   read_file <repo>/src/path/to/file.js
   ```

3. Trace function calls and behavior:
   ```bash
   # Find all callers of a function
   grep -r "functionName(" <repo>/src/

   # Find all references to a class
   grep -r "ClassName" <repo>/src/ | head -20
   ```

4. Document findings in the actual project:
   ```markdown
   # Debugging notes
   - Library: <name> v<version>
   - File inspected: `.deps-source/<repo>/src/path/file.js:42`
   - Finding: The function does X when Y is null, causing Z
   - Fix: Add null check in our code at `src/our-file.js:15`
   ```

### Phase 4: Apply Learnings & Clean Up

1. Apply the fix to your actual project (not the cloned source)
2. Add a code comment referencing the source finding:
   ```javascript
   // See: .deps-source/lib-name/src/file.js:42
   // The library doesn't handle null input, so we guard here
   const result = input != null ? lib.process(input) : defaultValue;
   ```
3. Clean up when done:
   ```bash
   # Remove clone after investigation
   rm -rf .deps-source/<repo>
   ```

## Verification Checklist

- [ ] Dependency version matches what's installed in the project
- [ ] Source cloned to ignored directory (not committed)
- [ ] Investigation documented with specific file:line references
- [ ] Fix applied to the actual project (not the clone)
- [ ] Code comments reference source findings
- [ ] Clone cleaned up after investigation

## Pitfalls

- **Version mismatch:** Always clone the exact version installed, not latest main
- **Large repos:** Some dependencies are monorepos — clone only the relevant package
- **Build artifacts:** Source may need building to understand compiled output — check dist/ too
- **License compliance:** Reading source for debugging is fine, but don't copy code without checking license
- **Forgetting to clean up:** Cloned deps can be large — remove when investigation is complete
- **Editing the clone:** Never edit the cloned source to "fix" bugs — fix your own code or file an upstream issue
