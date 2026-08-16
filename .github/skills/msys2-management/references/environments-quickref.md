# MSYS2 Environment Quick Reference

Companion to `msys2-management` SKILL.md. All paths assume the standard MSYS2
root `/c/msys64` (detect it first — see the SKILL.md pre-flight gate; Git Bash's
MSYS runtime is NOT standalone MSYS2).

## Environment launchers / prefixes

| Environment | `MSYSTEM` value | Prefix dir | Default C runtime | Use for |
|-------------|-----------------|------------|-------------------|---------|
| UCRT64 | `UCRT64` | `/ucrt64/bin/` | UCRT (modern) | **New builds (recommended)** |
| MINGW64 | `MINGW64` | `/mingw64/bin/` | msvcrt (legacy) | Legacy mingw-w64 |
| MINGW32 | `MINGW32` | `/mingw32/bin/` | msvcrt (legacy) | 32-bit mingw-w64 |
| CLANG64 | `CLANG64` | `/clang64/bin/` | UCRT | LLVM/Clang-based toolchain |
| CLANGARM64 | `CLANGARM64` | `/clangarm64/bin/` | UCRT | ARM64 cross-compilation |

## Package naming by environment

- `mingw-w64-ucrt-x86_64-<pkg>` — UCRT64
- `mingw-w64-x86_64-<pkg>` — MINGW64
- `mingw-w64-clang-x86_64-<pkg>` — CLANG64

Packages are environment-specific: installing the MINGW64 gcc does NOT make
`gcc` available under UCRT64.

## Key paths

| Path | Purpose |
|------|---------|
| `/c/msys64/` | Root install directory |
| `/c/msys64/usr/bin/bash.exe` | Shared bash binary (all environments) |
| `/c/msys64/usr/bin/pacman` | Package manager |
| `/c/msys64/usr/bin/msys-2.0.dll` | MSYS2 runtime DLL |
| `/c/msys64/ucrt64/bin/` | UCRT64 binaries |
| `/c/msys64/mingw64/bin/` | MINGW64 binaries |

## Invoking a subshell (captures stdout)

GUI launchers (`ucrt64.exe`, `mingw64.exe`, `msys2.exe`) are Windows GUI apps —
they spawn a window and produce **zero stdout** when run programmatically.
Always use the bash binary directly:

```bash
MSYS2_ROOT="${MSYS2_ROOT:-/c/msys64}"
CHERE_INVOKING=1 MSYSTEM=UCRT64 "$MSYS2_ROOT/usr/bin/bash" -l -c 'command here'
```

## Environment detection pitfalls

- `uname -a` reports the same kernel (`MINGW64_NT-...`) for all variants — check
  `$MSYSTEM` to distinguish environments.
- Inside Git Bash (`MSYSTEM=MSYS`), a full MSYS2 install may or may not be
  present — run the pre-flight gate before assuming `/c/msys64` exists.
