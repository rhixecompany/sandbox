---
name: msys2-management
version: 1.0.0
description: Manage MSYS2 environments on Windows — install, update, invoke subshells, manage packages via pacman, and verify toolchains. Covers UCRT64, MINGW64, MINGW32, CLANG64, and CLANGARM64.
title: "MSYS2 Management"
author: Hermes Agent
license: MIT
tags: [windows, msys2, toolchain, ucrt64, mingw64, pacman]
---
# MSYS2 Management

Manage MSYS2 installation on Windows — invoking subshells, package management, and toolchain verification. Use when the user asks about MSYS2, UCRT64, MINGW64, pacman on Windows, or compiling C/C++ on Windows.

## Pre-flight: is standalone MSYS2 actually installed?

**Git Bash (MSYS runtime) ≠ standalone MSYS2.** Git for Windows bundles a minimal
MSYS runtime (`/usr/bin/bash`, `cygpath`, `MSYSTEM=MSYS`) but does **not** include
the full MSYS2 distribution — no `/c/msys64`, no `pacman`, no UCRT64/MINGW64
toolchains. A host can have Git Bash without having MSYS2.

**Always detect before invoking `/c/msys64/...` or `pacman`:**

```bash
if [ -d /c/msys64 ] && [ -x /c/msys64/usr/bin/pacman ]; then
  MSYS2_ROOT=/c/msys64
elif command -v pacman >/dev/null 2>&1; then
  MSYS2_ROOT="$(cygpath -w "$(command -v pacman)" 2>/dev/null | sed 's|/usr/bin/pacman||;s|\\|/|g')"
else
  echo "Standalone MSYS2 is NOT installed on this host (only Git Bash MSYS runtime)." >&2
  echo "Install it first: https://www.msys2.org/  (winget install MSYS2.MSYS2)" >&2
  exit 1
fi
```

If the host has no `/c/msys64` and no `pacman`, every command in this skill that
touches `pacman` or `/c/msys64/usr/bin/bash` will fail — the detection gate above
is mandatory, not optional. Prefer `"$MSYS2_ROOT/usr/bin/bash"` over the
hardcoded `/c/msys64/usr/bin/bash` in scripts so non-default install roots work.


## When to Use

- When you need to automate or structure workflows for `msys2-management`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `msys2-management`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## MSYS2 Subshell Invocation

MSYS2 ships multiple environment launchers (UCRT64, MINGW64, MINGW32, CLANG64, CLANGARM64). The `.exe` launchers are **Windows GUI apps** — they spawn a window and DON'T capture stdout when run programmatically. Use the MSYS2 bash binary directly with the correct `MSYSTEM` env var.

### Correct pattern (from any bash environment)

```bash
MSYS2_ROOT="${MSYS2_ROOT:-/c/msys64}"   # set by the pre-flight gate above
CHERE_INVOKING=1 MSYSTEM=UCRT64 "$MSYS2_ROOT/usr/bin/bash" -l -c 'your command here'
```

| Flag | Purpose |
|------|---------|
| `CHERE_INVOKING=1` | Prevents `cd ~` — stays in current working directory |
| `MSYSTEM=UCRT64` | Selects the environment (UCRT64, MINGW64, MINGW32, CLANG64, CLANGARM64) |
| `"$MSYS2_ROOT/usr/bin/bash" -l` | MSYS2 bash with login profile (detected root, not hardcoded) |
| `-c 'command'` | Run command inline |

### Environment prefix mapping

| `MSYSTEM` value | Prefix directory | Purpose |
|-----------------|-----------------|---------|
| `UCRT64` | `/ucrt64/bin/` | UCRT (modern) CRT — recommended for new builds |
| `MINGW64` | `/mingw64/bin/` | Legacy mingw-w64 |
| `MINGW32` | `/mingw32/bin/` | 32-bit mingw-w64 |
| `CLANG64` | `/clang64/bin/` | LLVM/Clang-based toolchain |
| `CLANGARM64` | `/clangarm64/bin/` | ARM64 cross-compilation |

## Package Management (pacman)

MSYS2 uses Arch Linux's pacman. Packages follow the naming convention:
- `mingw-w64-ucrt-x86_64-<package>` — UCRT64 environment
- `mingw-w64-x86_64-<package>` — MINGW64 environment
- `mingw-w64-clang-x86_64-<package>` — CLANG64 environment

### Common commands

```bash
pacman -Syu                          # Full system update
pacman -S mingw-w64-ucrt-x86_64-gcc  # Install UCRT64 GCC
pacman -S mingw-w64-ucrt-x86_64-<pkg> # Install any UCRT64 package
pacman -Q mingw-w64-ucrt-x86_64-gcc  # Check if installed
pacman -Q | grep -i <keyword>        # Search installed packages
```

### Common UCRT64 development packages

| Package | Purpose |
|---------|---------|
| `mingw-w64-ucrt-x86_64-gcc` | GCC compiler suite (C, C++) |
| `mingw-w64-ucrt-x86_64-make` | GNU make |
| `mingw-w64-ucrt-x86_64-cmake` | CMake build system |
| `mingw-w64-ucrt-x86_64-gdb` | GDB debugger |
| `mingw-w64-ucrt-x86_64-git` | Git |
| `mingw-w64-ucrt-x86_64-python` | Python |
| `mingw-w64-ucrt-x86_64-boost` | Boost C++ libraries |
| `mingw-w64-ucrt-x86_64-ninja` | Ninja build system |

## Toolchain Verification

Run from within the target environment:

```bash
gcc --version    # C compiler
g++ --version    # C++ compiler
ld --version     # Linker
ar --version     # Archiver

# Verify runtime DLLs
ls /ucrt64/bin/libgcc_s_seh-1.dll   # SEH runtime (UCRT64)
ls /ucrt64/bin/libstdc++-6.dll       # C++ stdlib
ls /ucrt64/bin/libwinpthread-1.dll   # Windows threading

# Build + run test
echo '#include <stdio.h>
int main() { printf("Hello from UCRT64!\\n"); return 0; }' > /tmp/test.c &&
gcc /tmp/test.c -o /tmp/test.exe && /tmp/test.exe
```

## Common MSYS2 Paths

| Path | Description |
|------|-------------|
| `C:\msys64\` or `/c/msys64/` | Root install directory |
| `/c/msys64/usr/bin/bash.exe` | Shared bash binary (all environments) |
| `/c/msys64/ucrt64/bin/` | UCRT64 binaries |
| `/c/msys64/mingw64/bin/` | MINGW64 binaries |
| `/c/msys64/usr/bin/pacman` | Package manager |

## Pitfalls

### GUI launchers don't capture stdout
`ucrt64.exe`, `mingw64.exe`, `msys2.exe` are Windows GUI apps. Running them from a background terminal produces zero stdout. Always use `MSYSTEM=... /c/msys64/usr/bin/bash -l` instead.

### `uname` reports the same kernel for all variants
MSYS2 uses a shared kernel layer. `uname -a` will show `MINGW64_NT-...` regardless of which environment you're in. Check `$MSYSTEM` to distinguish environments.

### Package names differ by environment
Packages are environment-specific. Installing `mingw-w64-x86_64-gcc` won't make `gcc` available under UCRT64 — you need `mingw-w64-ucrt-x86_64-gcc`.

### First pacman run may need `pacman -Sy`
A fresh install or long-idle MSYS2 may have stale package DBs. Run `pacman -Sy` first if package lookups fail.

## References

- `references/environments-quickref.md` — Quick reference table for all MSYS2 environments and their characteristics.
- `references/toolchain-verification.md` — Detailed toolchain verification scripts and expected output.

## Verification Checklist

- [ ] **Pre-flight passed**: `/c/msys64` exists (or `pacman` on PATH); otherwise standalone MSYS2 is not installed — install it first
- [ ] MSYS2 root detected and exported as `$MSYS2_ROOT` (not hardcoded `/c/msys64`)
- [ ] Target environment tools installed (gcc, ld, etc.)
- [ ] Test compile + run succeeds
- [ ] `$MSYSTEM` correctly identifies the active environment

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "MSYS2 Management".

### Phase 2: Execution

Run the primary "MSYS2 Management" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
