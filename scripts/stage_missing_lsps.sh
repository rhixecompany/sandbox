#!/usr/bin/env bash
# Stage missing LSP server binaries into Hermes' lsp/bin dir.
# Hermes probes <HERMES_HOME>/lsp/bin/ before PATH (agent/lsp/install.py),
# so staging there registers servers as installed.
set -uo pipefail
BIN_DIR="$LOCALAPPDATA/hermes/lsp/bin"
TMP_DIR="$LOCALAPPDATA/Temp/lsp_stage_$$"
mkdir -p "$BIN_DIR" "$TMP_DIR"
cd "$TMP_DIR" || exit 1
fail=0

stage_zip() { # $1=name  $2=url  $3=exe_pattern
  local name="$1" url="$2" pat="$3"
  echo "== $name =="
  if ! curl -fsSL --retry 2 -o "$name.zip" "$url"; then echo "   download FAILED"; fail=1; return; fi
  if ! unzip -oq "$name.zip"; then echo "   unzip FAILED"; fail=1; return; fi
  local exe; exe=$(find . -iname "$pat" -type f | head -1)
  if [ -z "$exe" ]; then echo "   binary not found (pattern $pat)"; fail=1; return; fi
  chmod +x "$exe"
  cp -f "$exe" "$BIN_DIR/$(basename "$exe")"
  echo "   OK -> $BIN_DIR/$(basename "$exe")"
}

# zls (zig)
stage_zip zls "https://github.com/zigtools/zls/releases/download/0.16.0/zls-x86_64-windows.zip" "zls.exe"

# clojure-lsp
stage_zip clojure-lsp "https://github.com/clojure-lsp/clojure-lsp/releases/download/2026.07.06-14.34.19/clojure-lsp-native-windows-amd64.zip" "clojure-lsp.exe"

# gleam
stage_zip gleam "https://github.com/gleam-lang/gleam/releases/download/v1.18.0/gleam-v1.18.0-x86_64-pc-windows-msvc.zip" "gleam.exe"

# terraform-ls (resolve latest asset name dynamically)
echo "== terraform-ls =="
TL_VER=$(gh api repos/hashicorp/terraform-ls/releases/latest --jq '.tag_name' 2>/dev/null | tr -d '\r')
TL_ASSET=$(gh api "repos/hashicorp/terraform-ls/releases/latest" --jq '.assets[].name' 2>/dev/null | grep -i "windows_amd64.zip" | head -1 | tr -d '\r')
if [ -n "$TL_VER" ] && [ -n "$TL_ASSET" ]; then
  stage_zip terraform-ls "https://github.com/hashicorp/terraform-ls/releases/download/$TL_VER/$TL_ASSET" "terraform-ls.exe"
else
  echo "   no windows asset found"; fail=1
fi

# prisma via npm (fits the user's stack)
echo "== prisma =="
if bun install --prefix "$LOCALAPPDATA/hermes/lsp" --silent --no-fund --no-audit @prisma/language-server >/dev/null 2>&1; then
  PRISMA_BIN="$LOCALAPPDATA/hermes/lsp/node_modules/.bin/prisma-language-server"
  if [ -f "$PRISMA_BIN" ] || [ -f "$PRISMA_BIN.cmd" ]; then
    cp -f "$PRISMA_BIN" "$BIN_DIR/prisma-language-server" 2>/dev/null || true
    echo "   OK -> $BIN_DIR/prisma-language-server"
  else
    echo "   installed but bin not found"; fail=1
  fi
else
  echo "   bun install FAILED"; fail=1
fi

rm -rf "$TMP_DIR"
echo "DONE fail=$fail"
exit $fail
