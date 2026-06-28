# Choco/Winget Migration — Error Patterns & Workarounds

Collected from session 2026-06-25. These are the raw error messages and
solutions discovered in real migration work.

## choco list — Flags Removed in v2.5.0

```
> choco list --local-only
> Invalid argument --local-only. This argument has been removed from the list command and cannot be used.

> choco list -l
> Invalid argument -l. This argument has been removed from the list command and cannot be used.
```

**Fix:** Use bare `choco list`. It now queries local packages by default.

## choco uninstall — Dependency Block

```
> choco uninstall vcredist140 -y
> [NuGet]: Unable to uninstall 'vcredist140.14.51.36247' because
> 'vcredist2015.14.0.24215.20170201' depends on it.
```

**Fix:** Uninstall the dependent first, then the target:
```
choco uninstall vcredist2015 -y   # removes the dependent
choco uninstall vcredist140 -y     # now succeeds
```

Both packages had no registry snapshots, so the uninstall was purely
choco-metadata removal. The actual VC++ runtime DLLs were already shared
with the winget-managed `Microsoft.VCRedist.2015+.x64` install.

## choco uninstall — Broken chocolateyUninstall.ps1 (fzf)

```
> choco uninstall fzf -y
> fzf v0.73.1
> Checking for running 'fzf' processes...
> WARNING: FileType 'EXE_MSI_OR_MSU' is unrecognized, using 'exe' instead.
> WARNING: May not be able to find 'winget uninstall --product-code
>   junegunn.fzf_Microsoft.Winget.Source_8wekyb3d8bbwe'. Please use full
>   path for executables.
> ERROR: Exception calling "Start" with "0" argument(s):
>   "The system cannot find the file specified"
> fzf not uninstalled.
```

**Root cause:** The choco fzf package's uninstall script was a thin shim
around `winget uninstall` that referenced a product code string rather
than the winget CLI binary path. With the winget install already done,
the choco metadata was orphaned.

**Fix:**
```
rm -rf /c/ProgramData/chocolatey/lib/fzf
choco list   # confirms fzf no longer shown
```

## Winget — Large Download Timeout (Gyan.FFmpeg 240 MB)

First attempt: `winget install --id Gyan.FFmpeg -e --accept-source-agreements`
with 60s timeout → killed during download at ~50% (~120 MB).

Second attempt: 180s timeout → killed at ~195 MB (still downloading).

**Root cause:** The Gyan.FFmpeg package is a full ffmpeg build at ~240 MB.
GitHub download speeds from this source were insufficient.

**Workaround:** Switch to `BtbN.FFmpeg.LGPL.7.1` (~131 MB), which also
succeeded more quickly. Run long downloads in background mode.

### Background download pattern (Hermes)
```python
terminal(
    command="winget install --id BtbN.FFmpeg.LGPL.7.1 -e --accept-source-agreements",
    background=True,
    notify_on_complete=True,
    timeout=600
)
```

## Overlap Detection: choco ↔ winget

When cross-referencing, not all names match directly. Known equivalents
discovered this session:

| Choco package | Winget ID | Same? |
|--------------|-----------|-------|
| ripgrep | `BurntSushi.ripgrep.MSVC` | Same tool, diff version |
| python314 | `Python.Python.3.14` | Same major version |
| vcredist140 | `Microsoft.VCRedist.2015+.x64` | Same runtime |
| ffmpeg | `Gyan.FFmpeg` / `BtbN.FFmpeg.LGPL.7.1` | Same tool |
| fzf | `junegunn.fzf` | Same version |
| jq | `jqlang.jq` | Winget is newer (1.8.2 vs 1.8.1) |
| make | `ezwinports.make` | Same version |
| unzip | `GnuWin32.UnZip` | Choco has newer (6.0 vs 5.51) |
| batteryinfoview | `NirSoft.BatteryInfoView` | Winget is newer (1.27 vs 1.26) |
