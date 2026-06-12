# Cleanup Plan: SandBox + Hermes (Skills/Hooks/Archives)

Generated: 2026-06-11

## Objective
- Prune loose docs/archives in SandBox
- Remove broken Hermes snapshot
- Non-aggressive prune of local skills (disabled/empty only)
- Remove both hook trees (`~/.hermes/hooks` + `.github/hooks`)

## Scope constraints (from user)
- Keep all 337 skills by default; prune only disabled/empty/duplicate local skill dirs
- `./sample.prompt.txt` in SandBox root is exempt from deletion
- Delete: `backup.hermes/`, `backups/`, `Prompts/_archive/`
- Delete: `~/.hermes/hermes-agent.broken-20260611-155754/`
- Delete both hook trees

## Steps

### 1. Baseline
- Export Hermes skills manifest
- Snapshot SandBox text/markdown counts
- Snapshot Hermes file counts

### 2. SandBox root text/markdown cleanup
- Delete `.txt`/`.md`/`.markdown` in SandBox root, except `sample.prompt.txt`

### 3. SandBox archive removal
- Delete `backup.hermes/`, `backups/`, `Prompts/_archive/`

### 4. Hermes broken snapshot removal
- Delete `hermes-agent.broken-20260611-155754/`

### 5. Hermes skills non-aggressive prune
- Detect disabled/empty skill dirs under `~/.hermes/skills`
- Halt for review before removing any enabled skill dir

### 6. Hermes + GitHub hooks removal
- Delete `~/.hermes/hooks/` and `.github/hooks/`

### 7. Verification
- Re-run counts
- Confirm `hermes skills list` still succeeds
- Report freed paths + totals

## Verification gates
- Step 2: root `find` excludes only `./sample.prompt.txt`
- Step 3: targeted paths are gone; dependent paths rechecked
- Step 5: enabled skills untouched; disabled/empty only
- Step 6: both hook dirs removed; no hook references in use
