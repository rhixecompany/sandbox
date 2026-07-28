$ErrorActionPreference='SilentlyContinue'
$root='C:\Users\Alexa\Desktop\SandBox'
$files=Get-ChildItem -Path $root -Recurse -Filter 'AGENTS.md' | Select-Object -ExpandProperty FullName
$items=foreach($f in $files){ $h=(Get-FileHash $f -Algorithm SHA256).Hash; [pscustomobject]@{File=$f;Hash=$h;Len=(Get-Item $f).Length} }
$items | Format-Table File,Hash,Len | Out-String -Width 200 | Write-Output | Out-File -FilePath 'C:\Users\Alexa\Desktop\SandBox\_tmp_agents_inventory.txt' -Encoding utf8
