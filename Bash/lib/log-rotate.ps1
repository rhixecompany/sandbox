# Log rotation utility
function Rotate-Logs {
    param([string]$LogDir, [int]$MaxLogs = 10)
    if (Test-Path $LogDir) {
        Get-ChildItem -Path $LogDir -Filter '*.log' | Sort-Object LastWriteTime -Descending | Select-Object -Skip $MaxLogs | Remove-Item -Force -ErrorAction SilentlyContinue
    }
}
Set-StrictMode -Version Latest
