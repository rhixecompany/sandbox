$ErrorActionPreference = 'Continue'
$root = 'c:\Users\Alexa\Desktop\SandBox\projects'
$projects = @(
  'Banking','comicwise','cookiecutter-django-tailwind','Django-Scrapy-Selenium','ecom','profile',
  'Python-projects','rhixe_scans','selenium_webdriver','university-libary-jsm','xamehi','xamehi.tv','youtube-downloader'
)
$prefix = 'chore/agentsmd-20260529'
$rows = @()

foreach ($name in $projects) {
  $repo = Join-Path $root $name
  $branch = "$prefix-$name"

  if ((git -C $repo rev-parse --is-inside-work-tree 2>$null) -ne 'true') {
    $rows += [PSCustomObject]@{ Repo = $name; Branch = '-'; CommitSHA = '-'; Status = 'skip:not-git-repo' }
    continue
  }

  $sha = (git -C $repo log -1 --pretty='%H' -- AGENTS.md 2>$null | Select-Object -First 1)
  if ([string]::IsNullOrWhiteSpace($sha)) {
    $rows += [PSCustomObject]@{ Repo = $name; Branch = '-'; CommitSHA = '-'; Status = 'skip:no-agents-history' }
    continue
  }

  git -C $repo push origin "${sha}:refs/heads/$branch" 1>$null 2>$null
  if ($LASTEXITCODE -eq 0) {
    $rows += [PSCustomObject]@{ Repo = $name; Branch = $branch; CommitSHA = $sha; Status = 'ok:pushed' }
    continue
  }

  if ($name -eq 'comicwise') {
    $clean = 'c:\Users\Alexa\Desktop\SandBox\projects\comicwise_push_clean'
    if ((git -C $clean rev-parse --is-inside-work-tree 2>$null) -eq 'true') {
      $cleanSha = (git -C $clean log -1 --pretty='%H' -- AGENTS.md 2>$null | Select-Object -First 1)
      if (-not [string]::IsNullOrWhiteSpace($cleanSha)) {
        git -C $clean push origin "${cleanSha}:refs/heads/$branch" 1>$null 2>$null
        if ($LASTEXITCODE -eq 0) {
          $rows += [PSCustomObject]@{ Repo = $name; Branch = $branch; CommitSHA = $cleanSha; Status = 'ok:pushed-via-clean-clone' }
          continue
        }
      }
    }
  }

  $rows += [PSCustomObject]@{ Repo = $name; Branch = $branch; CommitSHA = $sha; Status = 'fail:push-error' }
}

$out = 'c:\Users\Alexa\Desktop\SandBox\artifacts\agents-pr-reconciliation.json'
$rows | ConvertTo-Json -Depth 3 | Set-Content -Path $out -Encoding utf8
$rows | Format-Table -AutoSize
Write-Output "Wrote $out"
