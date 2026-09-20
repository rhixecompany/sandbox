# SPEC — yt-dl-agent-docs-20260920-142744

## Goal

Update, enhance, and verify project agent/user context files for `projects/youtube-downloader`. Create any that are missing.

## Targets

| Path | Rule |
| --- | --- |
| `.cursorrules` | if exists → update/enhance/verify; else create |
| `AGENTS.md` | if exists → update/enhance/verify; else create |
| `CLAUDE.md` | if exists → update/enhance/verify; else create |
| `.hermes.md` | if exists → update/enhance/verify; else create |
| `README.md` | if exists → update/enhance/verify; else create |

## Constraints

- DRY: no duplication of root `AGENTS.md` / `.hermes.md` policy
- Verified commands only (manifests + CI + live tree)
- No secrets; no commit/push in this run

## Acceptance

- All five paths exist
- Commands match `package.json`, `pyproject.toml`, `requirements/local.txt`, CI
- Relative pointers resolve to SandBox root adapters / `SOUL.md`
