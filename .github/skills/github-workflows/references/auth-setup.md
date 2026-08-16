# GitHub Authentication Setup (absorbed: github-auth)

Sets up authentication so the agent can work with GitHub repositories, PRs,
issues, and CI. Two paths: `git` (always available — HTTPS PAT or SSH key) and
`gh` CLI (if installed — richer API access with a simpler auth flow).

## Detection Flow

Run this check first:

```bash
git --version
gh --version 2>/dev/null || echo "gh not installed"
gh auth status 2>/dev/null || echo "gh not authenticated"
git config --global credential.helper 2>/dev/null || echo "no git credential helper"
```

**Decision tree:**
1. `gh auth status` shows authenticated → use `gh` for everything
2. `gh` installed but not authenticated → use "gh auth" method below
3. `gh` not installed → use "git-only" method below (no sudo needed)

## Method 1: Git-Only Authentication (No gh, No sudo)

### Option A: HTTPS with Personal Access Token (Recommended)

Most portable — works everywhere, no SSH config.

1. Create a PAT at **https://github.com/settings/tokens** ("Generate new token
   (classic)") with scopes: `repo`, `workflow`, `read:org` (org repos). Set an
   expiration (90 days default). Copy it — shown only once.
2. Store it:
   ```bash
   git config --global credential.helper store        # persists in ~/.git-credentials
   # or: cache in memory:  git config --global credential.helper 'cache --timeout=28800'
   # or per-repo:          git remote set-url origin https://<user>:<token>@github.com/<owner>/<repo>.git
   # First auth:           git ls-remote https://github.com/<user>/<repo>.git  (username + PAT as password)
   ```
3. Set identity: `git config --global user.name "Name"` and
   `git config --global user.email "email@example.com"`.
4. Verify: `git ls-remote https://github.com/<user>/<repo>.git` works without prompts.

### Option B: SSH Key Authentication

1. Check existing keys: `ls -la ~/.ssh/id_*.pub`
2. Generate: `ssh-keygen -t ed25519 -C "email@example.com" -f ~/.ssh/id_ed25519 -N ""`
3. Add the `.pub` content at **https://github.com/settings/keys**.
4. Test: `ssh -T git@github.com` → "Hi <username>! You've successfully authenticated..."
5. Rewrite HTTPS→SSH: `git config --global url."git@github.com:".insteadOf "https://github.com/"`
6. Set git identity as above.

## Method 2: gh CLI Authentication

```bash
gh auth login                    # interactive: GitHub.com → HTTPS → browser
echo "<TOKEN>" | gh auth login --with-token   # headless / token-based
gh auth setup-git                # wire git credentials through gh
gh auth status                   # verify
```

## Using the GitHub API Without gh

```bash
export GITHUB_TOKEN="<token>"    # then send: -H "Authorization: token $GITHUB_TOKEN"
```

Or extract the token from git credentials:
`uv run python3 "${HERMES_HOME:-$HOME/.hermes}/skills/github/github-workflows/scripts/git-credential-token.py"`

Full environment detection (auth method + user + repo) in one shot:
`source "${HERMES_HOME:-$HOME/.hermes}/skills/github/github-workflows/scripts/gh-env.sh"`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git push` asks for password | GitHub disabled password auth. Use a PAT as the password, or switch to SSH |
| `remote: Permission to X denied` | Token may lack `repo` scope — regenerate with correct scopes |
| `fatal: Authentication failed` | Cached credentials stale — run `git credential reject`, re-authenticate |
| SSH port 22 blocked | Add `Host github.com` with `Port 443` + `Hostname ssh.github.com` to `~/.ssh/config` |
| Credentials not persisting | `git config --global credential.helper` must be `store` or `cache` |
| Multiple GitHub accounts | SSH with different keys per host alias in `~/.ssh/config`, or per-repo credential URLs |
| `gh: command not found` + no sudo | Use git-only Method 1 — no installation needed |

## Verification Checklist

- [ ] Chosen auth method verified with a live `git`/`gh` command
- [ ] Credentials persist across sessions (credential helper configured)
- [ ] SSH host alias/port overrides match the setup instructions
- [ ] Fallback method documented when primary install is blocked
