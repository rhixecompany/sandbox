---
author: Alexa
description: Use when working with Gh Cli.
license: MIT
metadata:
  hermes:
    tags:
    - tools
name: gh-cli
tags:
- tools
title: Gh Cli
version: 1.0.0

---

# Gh Cli

## Goal
Provide comprehensive guidance for Gh Cli workflows including authentication, repository transfer/migration, and multi-account management on Windows.

## Subgoals
1. **Preparation** — Verify auth, check scopes, identify accounts
2. **Execution** — Inventory repos, transfer between owners, handle name conflicts
3. **Verification** — Confirm transfers, clean up duplicates
4. **Scope Management** — Handle `delete_repo` scope gaps

## When to Use
- Managing GitHub repos, especially across org/user boundaries
- Transferring repos between accounts (user ↔ org, org → user)
- Cleaning up duplicate repos after migration
- Handling `.tv` or similarly-patterned duplicate repo names
- **Triggers**: "migrate repo", "transfer repo", "move repo", "consolidate accounts", "gh auth", "multi-account"

## When NOT to Use
- Simple clone/fork/create operations (use `github` or `github-repo-management` umbrella)
- Basic PR/issues workflow (use `github` skill)

## Account & Token Management

### List Authenticated Accounts

```bash
gh auth status
# Shows all logged-in accounts with their scopes
```

### Scope Detection

```bash
gh auth status 2>&1 | grep "scopes"
# Typical: 'gist', 'read:org', 'repo', 'workflow'
# Missing: 'delete_repo' — needed for repo deletion but NOT for transfer

# To add delete_repo scope (interactive browser flow required):
#   gh auth refresh -h github.com -s delete_repo
```

### Switch Active Account

The active account is the one marked "Active account: true" in `gh auth status`.
Transfers and API calls use the active account.

### MSYS/Windows Path Note

On Git Bash (MSYS), API endpoints starting with `/` can be rewritten as Windows filesystem paths:
```bash
# WRONG — MSYS rewrites /repos/... to C:/Program Files/Git/repos/...
gh api /repos/owner/repo

# RIGHT — quoting prevents MSYS path rewriting
gh api "repos/owner/repo"
gh api "user/memberships/orgs/OrgName"
```

## Workflow: Repo Transfer & Migration

### Phase 1: Inventory

List all repos from source and destination with full metadata:

```bash
# Source (org or user)
gh repo list <source> --limit 50 \
  --json name,description,owner,isFork,isArchived,visibility,url,languages,updatedAt

# Destination
gh repo list <destination> --limit 50 \
  --json name,description,owner,isFork,isArchived,visibility,url,languages,updatedAt
```

Cross-reference by name to identify:
- **Unique repos** — exist at source only → can transfer directly
- **Name conflicts** — same name at both → must resolve before transfer
- **Content duplicates** — different names, same purpose → flag for deletion

### Phase 2: Transfer Unique Repos

```bash
# Single repo
gh api --method POST "repos/<source>/<repo>/transfer" \
  --raw-field "new_owner=<destination>"

# Bulk — loop over unique repos
for repo in repo1 repo2 repo3; do
  echo "--- Transferring $repo ---"
  gh api --method POST "repos/<source>/$repo/transfer" \
    --raw-field "new_owner=<destination>"
done
```

The API returns the full repo object on success. The repo is moved immediately.

### Phase 3: Resolve Name Conflicts

If the destination already has a repo with the same name, the transfer is rejected (HTTP 422). Check which version is newer:

```bash
gh repo view <source>/<repo> --json updatedAt
gh repo view <destination>/<repo> --json updatedAt
```

**Strategy A: Keep destination (it's newer)** — skip transfer, delete source's copy.

**Strategy B: Keep source (it's newer)** — rename destination to free the name:
```bash
gh repo edit <destination>/<repo> --new-name "<repo>-old"
# Then transfer source into the vacant name
gh api --method POST "repos/<source>/<repo>/transfer" \
  --raw-field "new_owner=<destination>"
```

### Phase 4: Delete Redundant Copies

After all transfers complete, delete duplicate/superfluous repos:

```bash
# Requires delete_repo scope
gh repo delete <owner>/<repo> --yes
```

If `delete_repo` is missing, report the list of repos to delete and ask the user to run `gh auth refresh -h github.com -s delete_repo`.

### Phase 5: Verify

```bash
# Confirm all expected repos at destination
gh repo list <destination> --limit 50 --json name,url

# Confirm source is clean
gh repo list <source> --limit 10 2>&1 || echo "Source empty"
```

## Auth Detection — Run Once Per Session

```bash
# For scripts and curl fallbacks
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  AUTH="gh"
  GH_USER=$(gh api user --jq '.login')
else
  AUTH="git"
  # Extract from git config
  if [ -z "$GITHUB_TOKEN" ]; then
    [ -f $LOCALAPPDATA/hermes/.env ] && GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" $LOCALAPPDATA/hermes/.env | head -1 | cut -d= -f2 | tr -d '\n\r')
    grep -q "github.com" ~/.git-credentials 2>/dev/null && GITHUB_TOKEN=$(grep "github.com" ~/.git-credentials | head -1 | sed 's|https://[^:]*:\([^@]*\)@.*|\1|')
  fi
fi
```

## Personas
| Persona | When to Use |
|---------|-------------|
| **Developer** | Technical implementation and coding tasks |
| **Admin** | System operations and maintenance, repo migration, org cleanup |
| **User** | Day-to-day operations and usage |

## Personality & Tone
- **Tone**: Professional, concise
- **Style**: Step-by-step instructions with examples
- **Avoid**: Unclear prerequisites, missing error handling
- **Encourage**: Verification checkpoints, resumability

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| General purpose | `default` |
| Code changes | `code-architect` |
| System operations | `adminbot` |

## Skills Required
| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Workflow (General)

### Phase 1: Preparation
- Understand the context and requirements
- Verify prerequisites are met
- Check authentication and available scopes

### Phase 2: Execution
- Follow step-by-step instructions
- Handle errors gracefully
- Document intermediate results

### Phase 3: Verification
- Confirm output meets requirements
- Document results

## Pitfalls
- **`delete_repo` scope missing**: `repo` scope allows transfers but NOT deletions. Interactive browser flow needed to add it.
- **MSYS path rewriting**: On Windows Git Bash, always double-quote API endpoint URLs.
- **Name conflicts block transfer**: Check destination for same-name repos before attempting transfer.
- **Transfer is immediate with no undo**: Verify destination capabilities before starting large migrations.
- **Org admin required**: Transferring from an org requires admin role in that org.
- **This skill was a thin stub**: Added repo migration content. May still lack edge-case coverage for very large org migrations.

## Local Git Cleanup (Post-Migration)

After migrating repos on GitHub, local clones need remote URL updates and
may be in broken git states. See the dedicated reference:

> [`references/repo-migration-local-fix.md`](references/repo-migration-local-fix.md)
>
> Covers: inventory stale remotes, update remote URLs, abort stuck rebases,
> fix detached HEAD, stash untracked files blocking checkout, push/pull
> syncing, final verification.

### Quick Summary

```bash
# 1. Update remote
git remote set-url origin https://github.com/new-owner/repo.git

# 2. Fix stuck state
git rebase --abort
git stash --include-untracked
git checkout development
git stash pop

# 3. Sync
git pull origin development --ff-only
git push origin development

# 4. Verify
grep -r "old-owner" projects/*/.git/config && echo "STALE" || echo "CLEAN"
```

## Verification Checklist
- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

