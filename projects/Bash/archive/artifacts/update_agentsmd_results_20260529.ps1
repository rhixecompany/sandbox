$p = 'c:\Users\Alexa\Desktop\SandBox\artifacts\agentsmd-workflow-results-20260529.json'
$data = Get-Content $p -Raw | ConvertFrom-Json
foreach ($r in $data) {
  if ($r.repo -eq 'comicwise') {
    $r.commit = '4e6d7e04352fd7e075370ff479e773b615298345'
    $r.remote = '4e6d7e04352fd7e075370ff479e773b615298345'
    $r.status = 'agents-unchanged;no-commit-needed;pushed;verified'
    $r.notes = 'fallback-published-from-comicwise_push_clean'
  }
}
$data | ConvertTo-Json -Depth 5 | Set-Content $p -Encoding utf8
Write-Output 'UPDATED_RESULTS'
