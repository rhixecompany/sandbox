---
category: software-development
title: Clonedeps
name: clonedeps
description: "Use when needing to inspect dependency/library source code for debugging implementation details, understanding SDK behavior, or investigating library bugs."
---

## clonedeps

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Clonedeps operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Clone important project dependency source code into an ignored local workspace for inspection. Enables reading library internals, understanding SDK/framework behavior from source, debugging implementation details, and making core dependency repos locally readable.

## When to Use

- Need to inspect dependency/library source code
- Debugging library implementation details
- Understanding SDK/framework behavior from source
- Making core dependency repos locally readable
- Investigating library bugs or edge cases
- Learning how a library works internally

## When NOT to Use

- Simple API/docs questions (use @librarian instead)
- Standard library usage or general programming questions
- Quick reference lookups that don't need source inspection
- Projects where dependencies are stable and well-documented

## Workflow

### Phase 1: Identify Dependencies

- List project dependencies (package.json, requirements.txt, go.mod, etc.)
- Determine which dependencies need source inspection
- Check if source is already available locally

### Phase 2: Clone to Workspace

- Create ignored local workspace directory (.gitignore entry)
- Clone dependency repositories into workspace
- Verify clones are complete and accessible

### Phase 3: Inspect & Understand

- Navigate source code structure
- Read implementation details
- Trace function calls and behavior
- Document findings

### Phase 4: Apply Learnings

- Use insights to fix bugs or optimize code
- Update project code based on understanding
- Clean up workspace when done

## Tools & References

- **Related Skills**: @librarian (docs), systematic-debugging (debugging)
- **Workspace Location**: `.dependencies/` or similar ignored directory
- **Git**: Clone with `git clone` or `git submodule`
- **Version Control**: Track which versions were cloned

## Best Practices

- Keep dependency clones in ignored directories (.gitignore)
- Document why each dependency was cloned
- Use specific versions/tags when cloning
- Clean up clones when investigation is complete
- Don't commit dependency clones to main repo
- Reference source findings in code comments
