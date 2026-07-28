Get-Process | Where-Object { $_.ProcessName -match 'bash|python|node|hermes' } | Select-Object Id, ProcessName | Format-Table -AutoSize
