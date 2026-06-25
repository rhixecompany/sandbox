# CLI Tools on PATH

> Generated 2026-06-25

---

## WinGet (WinGet Links)
`%LOCALAPPDATA%\Microsoft\WinGet\Links`

| Tool | Notes |
|------|-------|
| BatteryInfoView | NirSoft utility |
| copilot | GitHub Copilot CLI |
| direnv | env var loader |
| ffmpeg | multimedia framework |
| ffplay | FFmpeg player |
| ffprobe | FFmpeg stream probe |
| fzf | fuzzy finder |
| git-wt | git worktree helper |
| jq | JSON processor |
| make | build tool |
| nano | text editor |
| pmux | terminal multiplexer |
| pnpm | fast Node package manager |
| psmux | process multiplexer |
| rg (ripgrep) | recursive grep |
| tmux | terminal multiplexer |
| uv | Python package/version mgr |
| uvw | uv wrapper |
| uvx | uv tool runner |
| winstow | symlink manager |
| wt | Windows Terminal launcher |

## Bun
`%USERPROFILE%\.bun\bin`

| Tool | Notes |
|------|-------|
| bun | JS/TS runtime & bundler |
| bunx | bun package runner |
| agent-browser | browser automation CLI |
| btca | Bun toolchain helper |
| mcp-server-filesystem | MCP filesystem server |
| mcp-server-sequential-thinking | MCP thinking server |
| playwright-mcp | MCP Playwright server |

## Hermes / Local
`%USERPROFILE%\.local\bin`

| Tool | Notes |
|------|-------|
| uv | Python package/version mgr |
| uvw | uv wrapper |
| uvx | uv tool runner |
| python | Python (Hermes venv) |
| python3 | Python 3 alias |
| python3.11 | Python 3.11 |
| python3.13 | Python 3.13 |
| parallel-cli | parallel task runner |
| nano-pdf | PDF tool |
| alexa.bat | Hermes profile switch |
| code-architect.bat | Hermes profile switch |
| creative-director.bat | Hermes profile switch |
| exec-assistant.bat | Hermes profile switch |
| patient-tutor.bat | Hermes profile switch |
| research-analyst.bat | Hermes profile switch |

## Chocolatey
`C:\ProgramData\chocolatey\bin`

| Tool | Notes |
|------|-------|
| choco | Chocolatey package manager |
| choco-cleaner.bat | Choco cache cleaner |

## Git for Windows (MSYS2)
`C:\Program Files\Git\bin`

Standard GNU toolchain — bash, git, sh plus:

`awk` `basename` `bunzip2` `bzcat` `bzip2` `bzip2recover` `cat` `chattr` `chcon` `chgrp` `chmod` `chown` `chroot` `cksum` `clear` `cmp` `col` `comm` `cp` `csplit` `cut` `date` `dd` `df` `diff` `diff3` `dircolors` `dirname` `dos2unix` `du` `echo` `env` `envsubst` `expr` `factor` `false` `fdisk` `fgrep` `find` `fmt` `fold` `gawk` `getfacl` `grep` `groups` `gunzip` `gzip` `head` `hostid` `hostname` `id` `info` `infocmp` `install` `join` `kill` `less` `lessecho` `lesskey` `ln` `locate` `logname` `ls` `m4` `md5sum` `mkdir` `mkfifo` `mknod` `mktemp` `more` `mount` `msgunfmt` `mv` `nano` `nc` `nice` `nl` `nohup` `nproc` `numfmt` `od` `openssl` `paste` `patch` `pathchk` `pinky` `pr` `printenv` `printf` `ps` `ptx` `pwd` `readlink` `realpath` `rm` `rmdir` `runcon` `scp` `sed` `seq` `sha1sum` `sha224sum` `sha256sum` `sha384sum` `sha512sum` `shred` `shuf` `sleep` `sort` `split` `ssh` `stat` `stdbuf` `stty` `sum` `sync` `tac` `tail` `tar` `tee` `test` `time` `timeout` `touch` `tr` `true` `truncate` `tsort` `tty` `type` `ulimit` `umask` `uname` `unexpand` `uniq` `unlink` `uname` `unset` `unxz` `unzip` `uptime` `users` `uuencode` `uudecode` `wc` `wget` `whatis` `whereis` `who` `whoami` `xargs` `xxd` `xz` `xzcat` `yes` `zcat` `zcmp` `zdiff` `zegrep` `zfgrep` `zgrep` `zip` `zless` `zmore` `zstd` `zstdcat` `zstdgrep` `zstdless` `zstdmt` `unzstd`

## Other Notable Tools on PATH

| Tool | Likely Source |
|------|---------------|
| docker / docker-compose | Docker Desktop |
| gh | GitHub CLI (winget) |
| node / npm / npx | fnm-managed Node |
| pwsh / powershell | Microsoft.PowerShell (winget) |
| dotnet | .NET SDK |
| codex | Codex CLI |
| psql / pg_dump / createdb / dropdb | PostgreSQL (winget) |
| wsl | Windows Subsystem for Linux |

---

## Package Manager Summary

| Manager | Count | Managed Tools |
|---------|-------|---------------|
| **Winget** | 541 packages (incl. system) | Chrome, Edge, Brave, VLC, Docker, Git, VS Code, Python, Terminal, PowerToys, etc. |
| **Chocolatey** | 9 packages (infra only) | choco-cleaner, choco extensions, KB patches |
| **Bun** | 8 binaries | bun, bunx, agent-browser, MCP servers |
| **Hermes local** | ~15 scripts | python, uv, profile switchers |
| **fnm (Node)** | node, npm, npx | Node.js version manager |
