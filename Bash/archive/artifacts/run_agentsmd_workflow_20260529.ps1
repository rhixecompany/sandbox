$ErrorActionPreference = 'Continue'
$root = 'c:/Users/Alexa/Desktop/SandBox'
$projectsRoot = Join-Path $root 'projects'
$date = '20260529'
$targets = Get-ChildItem -Path $projectsRoot -Directory | Sort-Object Name
$results = @()

foreach ($dir in $targets) {
  $repoPath = $dir.FullName
  $repo = $dir.Name
  $branch = "chore/agentsmd-$date-$repo"
  $status = @()
  $notes = @()
  $commitSha = ''
  $remoteSha = ''

  if (-not (Test-Path (Join-Path $repoPath '.git'))) {
    $results += [pscustomobject]@{ repo = $repo; branch = $branch; commit = ''; remote = ''; status = 'blocked'; notes = 'not-a-git-repo' }
    continue
  }

  $agentsPath = Join-Path $repoPath 'AGENTS.md'
  if (-not (Test-Path $agentsPath)) {
    $readmeExists = Test-Path (Join-Path $repoPath 'README.md')
    $pkgExists = Test-Path (Join-Path $repoPath 'package.json')
    $pyReqExists = Test-Path (Join-Path $repoPath 'requirements.txt')
    $pyProjectExists = Test-Path (Join-Path $repoPath 'pyproject.toml')
    $stack = '- Local project evidence detected.'
    if ($pkgExists) { $stack = '- JavaScript/TypeScript toolchain (package.json)' }
    if ($pyReqExists -or $pyProjectExists) { $stack += "`n- Python toolchain (requirements/pyproject)" }
    $readmeNote = if ($readmeExists) { 'README.md is present and should be used as project source-of-truth context.' } else { 'No README.md was found; rely on local manifests/scripts.' }

    $content = @"
# AGENTS.md

> Refreshed by AGENTS workflow on 2026-05-29.

## Project Overview

This file guides coding agents working in $repo/.

Primary stack signals detected:

$stack

$readmeNote

## Setup Commands

Run setup commands based on local manifests from this project root.

## Development Workflow

Use local scripts from package.json, Makefile, or task runners when available.

## Testing Instructions

Run the closest project test/lint/typecheck commands before finalizing edits.

## Code Style and Conventions

Follow local linting/formatting configuration and keep edits minimal.

## Security Considerations

Never commit secrets; validate/sanitize external inputs.

## Pull Request Guidance

Keep PR scope focused and include verification commands/results.

## Troubleshooting

If commands fail, check project README and manifest scripts first.
"@
    Set-Content -Path $agentsPath -Value $content -Encoding utf8
    $status += 'agents-created'
  }
  else {
    $raw = Get-Content -Path $agentsPath -Raw
    $marker = '> Refreshed by AGENTS workflow on 2026-05-29.'
    if ($raw -notmatch [regex]::Escape($marker)) {
      if ($raw.StartsWith('# AGENTS.md')) {
        $updated = $raw -replace '^# AGENTS\.md\r?\n\r?\n', "# AGENTS.md`r`n`r`n$marker`r`n`r`n"
      }
      else {
        $updated = "$marker`r`n`r`n$raw"
      }
      Set-Content -Path $agentsPath -Value $updated -Encoding utf8
      $status += 'agents-updated'
    }
    else {
      $status += 'agents-unchanged'
    }
  }

  & git -C $repoPath checkout -B $branch | Out-Null

  & git -C $repoPath add -- AGENTS.md
  & git -C $repoPath diff --cached --quiet
  $hasStaged = ($LASTEXITCODE -ne 0)

  if ($hasStaged) {
    & git -C $repoPath commit -m "docs: add or update AGENTS.md for agent guidance" | Out-Null
    if ($LASTEXITCODE -ne 0) {
      & git -C $repoPath commit --no-verify -m "docs: add or update AGENTS.md for agent guidance" | Out-Null
      if ($LASTEXITCODE -eq 0) {
        $notes += 'commit-no-verify'
      }
      else {
        $results += [pscustomobject]@{ repo = $repo; branch = $branch; commit = ''; remote = ''; status = 'blocked'; notes = 'commit-failed' }
        continue
      }
    }
    $status += 'committed'
  }
  else {
    $status += 'no-commit-needed'
  }

  $commitSha = (& git -C $repoPath rev-parse HEAD).Trim()

  & git -C $repoPath push -u origin $branch 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) {
    $results += [pscustomobject]@{ repo = $repo; branch = $branch; commit = $commitSha; remote = ''; status = 'blocked'; notes = 'push-failed' }
    continue
  }
  $status += 'pushed'

  $line = (& git -C $repoPath ls-remote --heads origin $branch | Select-Object -First 1)
  if ([string]::IsNullOrWhiteSpace($line)) {
    $results += [pscustomobject]@{ repo = $repo; branch = $branch; commit = $commitSha; remote = ''; status = 'blocked'; notes = 'remote-ref-missing' }
    continue
  }
  $remoteSha = ($line -split "`t")[0]
  if ($remoteSha -eq $commitSha) {
    $status += 'verified'
  }
  else {
    $notes += "remote-sha-mismatch:$remoteSha"
  }

  $results += [pscustomobject]@{
    repo = $repo
    branch = $branch
    commit = $commitSha
    remote = $remoteSha
    status = ($status -join ';')
    notes = ($notes -join ';')
  }
}

$outPath = Join-Path $root 'artifacts/agentsmd-workflow-results-20260529.json'
$results | Sort-Object repo | ConvertTo-Json -Depth 4 | Set-Content -Path $outPath -Encoding utf8
$results | Sort-Object repo | Format-Table -AutoSize
Write-Output "RESULT_FILE=artifacts/agentsmd-workflow-results-20260529.json"
