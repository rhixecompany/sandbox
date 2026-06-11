# Sandbox migration helper commands
# Run from: C:\Users\Alexa\Desktop\SandBox

Write-Host "== Runtime Inventory =="
Get-ChildItem "C:\Users\Alexa\Desktop\SandBox\projects" -Directory |
  Select-Object Name, FullName |
  Format-Table -AutoSize

Write-Host "`n== Patch Discovery =="
Get-ChildItem "C:\Users\Alexa\Desktop\SandBox" -Recurse -Filter *.patch |
  Select-Object Name, FullName |
  Sort-Object FullName |
  Format-Table -AutoSize

Write-Host "`n== Git Repos in Projects Root =="
Get-ChildItem "C:\Users\Alexa\Desktop\SandBox\projects" -Directory |
  ForEach-Object {
    $gitDir = Join-Path $_.FullName ".git"
    [PSCustomObject]@{
      Project = $_.Name
      Path = $_.FullName
      HasGitRepo = Test-Path $gitDir
    }
  } |
  Format-Table -AutoSize

Write-Host "`nTemplate patch dry-run: git apply --check \"PATCH_FILE\""
Write-Host "Template patch apply:   git apply --index --3way \"PATCH_FILE\""
