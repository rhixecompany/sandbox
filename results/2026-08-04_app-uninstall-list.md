# App Uninstall — Inventory & Deletion List (PENDING APPROVAL)

**Date:** 2026-08-04 | **Source:** `winget list` (161 entries)
**Status:** READY FOR REVIEW — nothing uninstalled yet.

## Environment stack (from USER.md) — KEEP

Bun, Python 3.11/3.13, uv, Node/TypeScript, ruff/pyright/eslint/prettier,
Git, Git Bash (MSYS2), Docker Desktop, VS Code, Tailscale, WezTerm, ripgrep.

## Candidate removal list (review each; delete only checked)

| #   | App (Id)                                                    | Version    | Why candidate                                                             |
| --- | ----------------------------------------------------------- | ---------- | ------------------------------------------------------------------------- |
| 1   | **BleachBit** (BleachBit.BleachBit)                         | 6.0.2.3702 | Dedicated cleanup tool; overlaps this workflow; likely unused manual tool |
| 2   | **BatteryInfoView** (NirSoft.BatteryInfoView)               | 1.27       | One-off diagnostic util                                                   |
| 3   | **FFmpeg (LGPL static)** (BtbN.FFmpeg.LGPL.7.1)             | 7.1.5      | **Duplicate** — Gyan.FFmpeg 9.0 also installed; keep one                  |
| 4   | **Eclipse Temurin JDK 21** (EclipseAdoptium.Temurin.21.JDK) | 21.0.12.8  | Dev runtime; not in active stack (MCP servers are Node/TS)                |
| 5   | **Erlang OTP** (Erlang.ErlangOTP)                           | 29.0.5     | Large runtime; nothing in stack depends on it                             |
| 6   | **Julia** (Julialang.Julia)                                 | 1.12.6     | Large runtime; not in active stack                                        |
| 7   | **Dart SDK** (Google.DartSDK)                               | 3.12.2     | Flutter/desktop runtime; not in active stack                              |
| 8   | **Go** (GoLang.Go)                                          | 1.26.5     | Runtime; verify nothing needs it before removing                          |
| 9   | **GnuWin32 UnZip** (GnuWin32.UnZip)                         | 5.51       | Legacy, superseded by modern unzip                                        |
| 10  | **Copilot CLI** (GitHub.Copilot)                            | v1.0.78    | Copilot removed per prior session (2026-08-04); verify stale entry        |

## Duplicate VS Code / Edge (review before removing store/MSIX variants)

- VS Code installed under BOTH winget (Microsoft.VisualStudioCode) and MSIX variant. Keep one, remove the other's MSIX.
- Microsoft Edge has two entries (Microsoft.Edge + MSIX stable). Keep winget, note MSIX.

## KEEP (do not flag without explicit request)

- All `Microsoft.*`/`MSIX\Microsoft.*` system + store apps, VCRedist, .NET runtimes, MSVC, Python, NVM, IntelliJ-style tooling, Docker, Tailscale, Git, dev CLIs actually used.

## Next step

Confirm which numbered apps to uninstall. Command per item:
`winget uninstall --id <Id> --silent`
Deletion is destructive; I will NOT run it without your explicit go-ahead.
