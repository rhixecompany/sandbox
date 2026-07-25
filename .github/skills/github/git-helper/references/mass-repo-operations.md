# Mass Repo Operations — Batch Recipes

Recipes for operating on N repos in a workspace (e.g. `projects/*/`).
Each command is safe to re-run — idempotent patterns only.

## Inventory All Repos

```bash
# List remotes and current branches
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  url=$(git -C "$d" remote get-url origin 2>/dev/null | sed 's|https://github.com/||')
  branch=$(git -C "$d" branch --show-current 2>/dev/null || echo "detached")
  printf "%-35s → %-45s [%s]\n" "$(basename $d)" "$url" "$branch"
done

# Full remote inventory (find stale org references)
grep -r "Rhixe-company" projects/*/.git/config && echo "STALE FOUND" || echo "ALL CLEAN"
```

## Migrate Remotes (batch find-and-replace)

```bash
# Replace old org with new user in all repo remotes
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  git -C "$d" remote set-url origin \
    "$(git -C "$d" remote get-url origin | sed 's|Old-Org|New-User|')"
done

# Verify
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  echo "$(basename $d) → $(git -C "$d" remote get-url origin)"
done
```

## Fix Stuck Rebase / Detached HEAD

```bash
# Check which repos are in bad state
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  branch=$(cd "$d" && git branch --show-current 2>/dev/null)
  status=$(cd "$d" && git status --short -b 2>/dev/null | head -1)
  [ -z "$branch" ] && echo "DETACHED: $(basename $d) — $status"
done

# Fix all: stash untracked, checkout development
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  branch=$(cd "$d" && git branch --show-current 2>/dev/null)
  [ -n "$branch" ] && continue  # skip healthy repos
  echo "Fixing: $(basename $d)"
  cd "$d" && git stash --include-untracked 2>/dev/null
  cd "$d" && git rebase --abort 2>/dev/null || true
  cd "$d" && git checkout development 2>/dev/null || git checkout -b development
done
```

## Batch Add-Commit-Push

```bash
# Standardized commit across all repos
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  echo "--- $(basename $d) ---"
  cd "$d"
  git add -A
  git commit -m "chore: sync workspace artifacts for $(basename $d)" 2>/dev/null
  git push origin development 2>/dev/null || echo "Nothing to push"
done
```

## Set Default Branch to `production` Across All Repos

```bash
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  url=$(git -C "$d" remote get-url origin)
  owner_repo=$(echo "$url" | sed 's|https://github.com/||; s|\.git||')
  
  # Must push production branch first or API returns 422
  git -C "$d" push origin production 2>/dev/null
  
  # Set default
  cur=$(gh api repos/$owner_repo --jq '.default_branch' 2>/dev/null)
  if [ "$cur" != "production" ]; then
    result=$(gh api repos/$owner_repo -X PATCH -f default_branch=production --jq '.default_branch' 2>&1)
    echo "$(basename $d): $cur → $result"
  else
    echo "$(basename $d): already production"
  fi
done
```

## Full Repo State Report

```bash
# One-line per repo: name, remote (short), default branch, local/remote count
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  name=$(basename "$d")
  url=$(git -C "$d" remote get-url origin 2>/dev/null | sed 's|https://github.com/||')
  def=$(gh api repos/${url%.git} --jq '.default_branch' 2>/dev/null)
  lb=$(git -C "$d" branch | wc -l)
  rb=$(git -C "$d" branch -r | grep -v HEAD | wc -l)
  printf "%-35s %-45s def=%-12s (l=%d,r=%d)\n" "$name" "$url" "$def" "$lb" "$rb"
done
```
