---
name: windows-package-management
description: Manage Windows packages via winget and Chocolatey — list, search, install, upgrade, migrate, and troubleshoot. Covers cross-referencing package managers, handling dependency chains, broken uninstallers, and large download workarounds.
---

# Windows Package Management

Manage Windows packages through winget and Chocolatey. Use when the user asks about installed packages, migrating between package managers, troubleshooting package operations, or cleaning up duplicate installations.

## Listing Packages

### Winget
```
winget list
```
Lists all packages tracked by winget — includes winget-managed packages **plus** system-registered/ARP/MSIX packages. Not a pure list of what winget installed.

| Command | Purpose |
|---------|---------|
| `winget list` | All tracked packages (winget + system) |
| `winget list --source winget` | Winget-managed packages only |
| `winget search <name>` | Search available packages |
| `winget show --id <id>` | Package details and versions |
| `winget show --id <id> --versions` | All available versions |

### Chocolatey
```
choco list
```

**Note:** `--local-only` and `-l` flags were **removed in Chocolatey v2.5.0**. Bare `choco list` queries local packages by default.

| Command | Purpose |
|---------|---------|
| `choco list` | Locally installed choco packages |
| `choco list -i` | Include Programs and Features entries (not just choco) |
| `choco list --id-only` | Package names only |
| `choco outdated` | Packages with newer versions available |

## Installing

### Winget
```
winget install --id <id> -e --accept-source-agreements
```
- `-e` / `--exact` — exact ID match
- `--accept-source-agreements` — skip license prompts (non-interactive)

### Chocolatey
```
choco install <package> -y
```

## Upgrading

### Chocolatey
```
choco upgrade all -y --purge
```
The `--purge` flag removes old version files completely instead of leaving remnants.

### Winget
```
winget upgrade --all --accept-source-agreements
```

## Migrating from Chocolatey to Winget

When a package exists in both managers, prefer winget (Microsoft's built-in):

1. **Search winget** for the equivalent: `winget search <name>`
2. **Install the winget version**: `winget install --id <id> -e --accept-source-agreements`
3. **Uninstall the choco version**: `choco uninstall <package> -y`
4. **Verify**: `choco list` confirms removal

## Pitfalls

### Choco Uninstall: Dependency Chains
```
> choco uninstall vcredist140 -y
> Unable to uninstall 'vcredist140' because 'vcredist2015' depends on it.
```
**Fix:** Remove the dependent package first, then the dependency:
```
choco uninstall vcredist2015 -y   # remove dependent first
choco uninstall vcredist140 -y     # now safe to remove
```

### Choco Uninstall: Broken Scripts
Some choco packages (notably `fzf`) have a `chocolateyUninstall.ps1` that crashes because it internally calls `winget uninstall` and fails. The error looks like:
```
ERROR: Exception calling "Start" with "0" argument(s): "The system cannot find the file specified"
```
**Fix (force-remove):** Delete the package folder directly. The software is already gone (or managed by winget now):
```
rm -rf /c/ProgramData/chocolatey/lib/<package-name>
```
Run `choco list` to confirm it's gone.

### Winget: Large Downloads Time Out
Downloads exceeding ~100 MB can time out in foreground mode (the 180s default).

| Package | Approx Size | Alternative |
|---------|------------|-------------|
| `Gyan.FFmpeg` | 240 MB | `BtbN.FFmpeg.LGPL.7.1` (~131 MB) |
| `BtbN.FFmpeg.GPL.8.1` | ~130-240 MB | BtbN LGPL variants are smaller |

**Fix:** Use background mode for large downloads:
```
# Via Hermes terminal
terminal(command="winget install --id <id> -e --accept-source-agreements", background=True, notify_on_complete=True, timeout=600)
```

### Winget list vs choco list Differences
- `winget list` shows **everything** — winget-managed, ARP, MSIX packages, system components. Don't assume winget installed something just because it appears in `winget list`.
- `choco list` shows only packages Chocolatey explicitly installed.

### PATH Conflicts After Migration
When both choco and winget have the same tool, the choco shim directory (`C:\ProgramData\chocolatey\bin`) and winget links dir (`%LOCALAPPDATA%\Microsoft\WinGet\Links`) are both on PATH. After uninstalling the choco version, the winget version takes over automatically. Verify with `where <toolname>`.

## References

- `references/migration-error-patterns.md` — Raw error transcripts, exact workarounds, and known package equivalents discovered during real migration.

## Verification

After migration:
1. `choco list` — confirm package removed from choco
2. `winget list --source winget` — confirm package in winget
3. `where <toolname>` — verify the correct binary is on PATH
