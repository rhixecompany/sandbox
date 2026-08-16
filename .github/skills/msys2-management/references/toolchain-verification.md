# MSYS2 Toolchain Verification

Companion to `msys2-management` SKILL.md. Run these inside the target MSYS2
environment to prove the toolchain works. **Pre-flight first**: standalone MSYS2
must be installed (see SKILL.md) — Git Bash's MSYS runtime alone has no gcc/ld.

## 1. Pre-flight detection

```bash
if [ -d /c/msys64 ] && [ -x /c/msys64/usr/bin/pacman ]; then
  MSYS2_ROOT=/c/msys64
elif command -v pacman >/dev/null 2>&1; then
  MSYS2_ROOT="$(cygpath -w "$(command -v pacman)" 2>/dev/null | sed 's|/usr/bin/pacman||;s|\\|/|g')"
else
  echo "Standalone MSYS2 NOT installed (Git Bash MSYS runtime only). Install: https://www.msys2.org/" >&2
  exit 1
fi
```

## 2. Compiler/package presence

```bash
# From any bash:
CHERE_INVOKING=1 MSYSTEM=UCRT64 "$MSYS2_ROOT/usr/bin/bash" -l -c '
  pacman -Q mingw-w64-ucrt-x86_64-gcc || echo "MISSING: gcc"
  gcc --version
  g++ --version
  ld --version
  ar --version
'
```

Expected: each `--version` prints; the `pacman -Q` line confirms the UCRT64 gcc
package is installed under the UCRT64 environment (MINGW64 package ≠ UCRT64 gcc).

## 3. Runtime DLLs

```bash
ls "$MSYS2_ROOT"/ucrt64/bin/libgcc_s_seh-1.dll    # SEH runtime (UCRT64)
ls "$MSYS2_ROOT"/ucrt64/bin/libstdc++-6.dll       # C++ stdlib
ls "$MSYS2_ROOT"/ucrt64/bin/libwinpthread-1.dll   # Windows threading
```

## 4. Build + run smoke test

```bash
CHERE_INVOKING=1 MSYSTEM=UCRT64 "$MSYS2_ROOT/usr/bin/bash" -l -c '
  printf "#include <stdio.h>\nint main() { printf(\"Hello from UCRT64!\\n\"); return 0; }\n" > /tmp/test.c &&
  gcc /tmp/test.c -o /tmp/test.exe &&
  /tmp/test.exe
'
```

Expected output: `Hello from UCRT64!` and exit 0.

## 5. `$MSYSTEM` check

```bash
CHERE_INVOKING=1 MSYSTEM=UCRT64 "$MSYS2_ROOT/usr/bin/bash" -l -c 'echo "MSYSTEM=$MSYSTEM"'
# Expected: MSYSTEM=UCRT64  (uname says MINGW64_NT-... for every variant — trust $MSYSTEM)
```

## Failure triage

| Symptom | Cause | Fix |
|---------|-------|-----|
| `No such file or directory` for `/c/msys64/usr/bin/bash` | MSYS2 not installed | Install MSYS2 (see SKILL.md) |
| `gcc: command not found` inside env | Package installed for wrong env | `pacman -S mingw-w64-ucrt-x86_64-gcc` |
| `pacman: command not found` | Inside Git Bash, not MSYS2 | Use `"$MSYS2_ROOT/usr/bin/bash" -l` |
| Stale package DB | Long-idle MSYS2 | `pacman -Sy` once, then retry |
