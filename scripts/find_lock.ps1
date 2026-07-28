$path = "C:\Users\Alexa\AppData\Local\hermes\profiles\alexa\logs\mcp-stderr.log"
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class RM {
    [DllImport("rstrtmgr.dll", CharSet=CharSet.Unicode)]
    public static extern int RmStartSession(out uint pSessionHandle, int dwSessionFlags, string strSessionKey);
    
    [DllImport("rstrtmgr.dll", CharSet=CharSet.Unicode)]
    public static extern int RmRegisterResources(uint pSessionHandle, uint nFiles, string[] rgsFilenames, uint nApplications, uint rgsApplications, uint nServices, string[] rgsServiceNames);
    
    [DllImport("rstrtmgr.dll")]
    public static extern int RmGetList(uint dwSessionHandle, out uint pnProcInfoNeeded, ref uint pnProcInfo, IntPtr rgAffectedApps, ref uint lpdwRebootReasons);
    
    [DllImport("rstrtmgr.dll")]
    public static extern int RmEndSession(uint pSessionHandle);
}
"@

$sessionHandle = 0
$result = [RM]::RmStartSession([ref]$sessionHandle, 0, [Guid]::NewGuid().ToString())
Write-Host "Session: $sessionHandle Result: $result"

$resources = @($path)
$result = [RM]::RmRegisterResources($sessionHandle, 1, $resources, 0, $null, 0, $null)
Write-Host "Register result: $result"

$procInfoNeeded = 0
$procInfo = 10
$rebootReasons = 0

$size = [System.Runtime.InteropServices.Marshal]::SizeOf([type]::GetType("System.Int32")) * 2 + 260 * 2
Write-Host "Trying to find lock..."

# Simpler: just use tasklist /m to find what's using the file
$result = [RM]::RmEndSession($sessionHandle)

# Alternative approach - use handle from Sysinternals if available
$handlePath = Get-Command handle64.exe -ErrorAction SilentlyContinue
if (-not $handlePath) { $handlePath = Get-Command handle.exe -ErrorAction SilentlyContinue }

if ($handlePath) {
    & $handlePath.Path -a "$path" 2>&1 | Select-Object -First 5
} else {
    Write-Host "handle.exe not found, trying alternate method..."
    # Use netstat or check open files
    & "C:\Windows\System32\openfiles.exe" /Query /v 2>&1 | Select-Object -First 5
}
