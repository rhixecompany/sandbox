$repo = 'c:\Users\Alexa\Desktop\SandBox\projects\comicwise_push_clean'
$branch = 'chore/agentsmd-20260529-comicwise'

git -C $repo checkout -B $branch | Out-Null
git -C $repo push -u origin $branch
$line = git -C $repo ls-remote --heads origin $branch | Select-Object -First 1
if ([string]::IsNullOrWhiteSpace($line)) {
  Write-Output 'VERIFY_FAIL'
  exit 1
}
$sha = ($line -split "`t")[0]
Write-Output "VERIFY_OK|$sha"
