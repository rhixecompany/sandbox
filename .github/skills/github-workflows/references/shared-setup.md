# Shared Setup — auth detection + repo coordinates

Run this at the start of any GitHub workflow. It detects the auth method
(gh CLI > token env var > Hermes .env > git credential store), exports the
token, and resolves owner/repo from the git remote.

## Quick version (source the helper)

```bash
source "${HERMES_HOME:-$HOME/.hermes}/skills/github/github-workflows/scripts/gh-env.sh"
# Sets: GH_AUTH_METHOD ("gh"|"curl"|"none"), GITHUB_TOKEN, GH_USER, GH_OWNER, GH_REPO, GH_OWNER_REPO
```

## Inline version (no script dependency)

```bash
# Detect auth method: gh CLI > GITHUB_TOKEN env > ~/.hermes/.env > git credential store
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  AUTH="gh"
else
  AUTH="git"
  if [ -z "$GITHUB_TOKEN" ]; then
    if _hermes_env="${HERMES_HOME:-$HOME/.hermes}/.env"; [ -f "$_hermes_env" ] && grep -q "^GITHUB_TOKEN=" "$_hermes_env"; then
      GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" "$_hermes_env" | head -1 | cut -d= -f2 | tr -d '\n\r')
    elif grep -q "github.com" ~/.git-credentials 2>/dev/null; then
      GITHUB_TOKEN=$(uv run python3 "${HERMES_HOME:-$HOME/.hermes}/skills/github/github-workflows/scripts/git-credential-token.py")
    fi
  fi
fi
echo "Using: $AUTH"
```

## Owner/repo from the git remote

Works for both HTTPS and SSH remote URLs:

```bash
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
echo "Owner: $OWNER, Repo: $REPO"
```

If the auth method is `none`, complete `references/auth-setup.md` first.
