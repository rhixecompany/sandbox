# Windows Cache Types & Cleanup Targets

Reference of all cache types that can be safely cleaned on a Windows dev machine.

## System Caches (Regenerate Automatically)

| Cache Type | Location | Size (Typical) | Tool | Reversible | Notes |
|-----------|----------|----------------|------|-----------|-------|
| NPM cache | `%APPDATA%/npm-cache` | 50-200 MB | `npm cache clean --force` | Yes | Regenerates on next install |
| Bun cache | `%USERPROFILE%/.bun/cache` | 20-100 MB | `bun pm cache rm` | Yes | Regenerates on next bun command |
| PNPM cache | `%LOCALAPPDATA%/pnpm-store` | 50-150 MB | `pnpm store prune` | Yes | Regenerates on next install |
| Docker buildkit | `%USERPROFILE%/.docker` | 20-100 MB | `docker system prune -a` | Yes | Regenerates on next build |
| Docker images | (same) | 100-500 MB | (same) | Yes | Keep only active images |
| Temp folder | `C:\Temp`, `%TEMP%` | 100-1000 MB | Manual or script | Yes | Windows regenerates |
| Windows Update cache | `C:\Windows\SoftwareDistribution\Download` | 50-500 MB | `Disk Cleanup` | Yes | Safe to delete after update |
| VS Code cache | `%APPDATA%/Code/Cache` | 100-500 MB | Manual delete | Yes | Rebuilds on restart |
| Git LFS cache | `%USERPROFILE%/.cache/git-lfs` | 10-100 MB | `git lfs prune` | Yes | Re-downloads as needed |
| Java Maven cache | `%USERPROFILE%/.m2/repository` | 100-1000 MB | `mvn dependency:purge-local-repository` | Yes | Re-downloads on build |
| Gradle cache | `%USERPROFILE%/.gradle` | 100-500 MB | `gradle cleanBuildCache` | Yes | Re-downloads on build |
| DNS cache | System | <1 MB | `ipconfig /flushdns` | Yes | Regenerates immediately |
| Thumbnails | `C:\Users\<user>\AppData\Local\Microsoft\Windows\Explorer` | 10-50 MB | Manual delete | Yes | Windows regenerates |
| WER reports | `C:\ProgramData\Microsoft\Windows\WER` | 5-50 MB | Manual delete | Yes | New errors regenerate |

**Total typical system cache:** 300-1000 MB across all types.

---

## Dependency Caches (May Require Rebuild)

| Dependency Type | Location | Size (Typical) | Restore Command | Reversible | Notes |
|----------------|----------|----------------|-----------------|-----------|-------|
| node_modules | `project-root/node_modules` | 100-500 MB | `npm install` | No (but recoverable) | Lost until npm install |
| Python venv | `project-root/venv` | 50-200 MB | `python -m venv venv` | No (but recoverable) | Lost until venv recreated |
| .NET bin/obj | `project-root/bin`, `/obj` | 50-200 MB | `dotnet build` | No (but recoverable) | Rebuilt on compile |
| Java target | `project-root/target` | 50-500 MB | `mvn clean install` | No (but recoverable) | Rebuilt on compile |
| Go pkg | `%USERPROFILE%/go/pkg` | 20-100 MB | `go build ./...` | No (but recoverable) | Re-downloaded on build |
| Ruby gems | `%USERPROFILE%/.gems` | 50-200 MB | `bundle install` | No (but recoverable) | Reinstalled from Gemfile |

**Total typical project dependencies:** 100-500 MB per active project.

---

## Session Example: Sandbox/Bash Cleanup (2026-05-27)

**Before:**
```
C: drive free space: 0 bytes (100% FULL — CRITICAL)
Dependencies found: 394.43 MB
  • Bash/node_modules: 301.1 MB ← PRIMARY TARGET
  • Resume_maker/node_modules: 93.29 MB (kept — active project)
Caches found: ~418 MB (14 types)
```

**Operations:**
1. Delete Bash node_modules: `clean_dependency_folders.sh --max-depth 2 --auto`
   - Result: 301.1 MB freed
2. Clean all caches: `cache-clean.sh --all --auto`
   - Result: ~418 MB freed (14 cache types)

**After:**
```
C: drive free space: 718.75 MB (operational)
Dependencies remaining: 93.29 MB (Resume_maker only)
Caches: Cleaned, regenerating on next use
Total reclaimed: ~719 MB
```

**Recovery:**
- Restore Bash dependencies: `cd Bash && npm install`
- Caches: Regenerate automatically on next tool use

---

## Cleanup Order (Recommended)

**For critical disk situations (0-100 MB free):**

1. **Delete dependencies first** (highest gain, fastest)
   - `clean_dependency_folders.sh --max-depth 2 --auto`
   - Typical gain: 100-500 MB in seconds

2. **Clean caches next** (moderate gain, continues freeing space)
   - `cache-clean.sh --all --auto`
   - Typical gain: 50-500 MB over 30 seconds

3. **Monitor results**
   - Check: `Get-Volume C | Select-Object SizeRemaining, Size`
   - If still critical, may need to delete other project dependencies

**For routine cleanup (>500 MB free):**
- Just run `cache-clean.sh --all --auto` weekly
- Defer dependency cleanup until next major version bump
