$ErrorActionPreference = 'SilentlyContinue'  
$root = 'C:\Users\Alexa\Desktop\SandBox'  
$hashes   = @{}  
$dupes    = @{}  

Get-ChildItem -Path $root -Recurse -Filter 'AGENTS.md' | ForEach-Object {  
  $path = $_.FullName  
  $hash = (Get-FileHash -Path $path -Algorithm SHA256).Hash  
  $size = (Get-Item $path).Length  
  if ($hashes.ContainsKey($hash)) {  
    $dupes[$hash] += ,$path  
  } else {  
    $hashes[$hash] = $path  
    $dupes[$hash]  = ,@($path)  
  }  
}  
if ($dupes.Count -eq 0) { 'NO_DUPES'; exit 0 }  
$dupes.Values | Where-Object Length -gt 1 | ForEach-Object { 'DUP_GROUP=' + ($_ -join '|') }  
exit 0  
