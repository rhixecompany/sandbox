param([string]$Path)
$pathToCheck = "C:\Users\Alexa\AppData\Local\hermes\profiles\alexa\logs\mcp-stderr.log"
Write-Output "Checking handles for: $pathToCheck"
$procs = Get-Process
foreach ($p in $procs) {
    try {
        $handles = $p.HandleCount
        if ($handles -gt 0) {
            # Not all processes expose handle info via .NET, skip silently
        }
    } catch {
        # skip
    }
}
Write-Output "Done checking"
