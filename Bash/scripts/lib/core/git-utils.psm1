#Requires -Version 5.1
<#
.SYNOPSIS
    Git utilities - unified wrapper for git operations
.DESCRIPTION
    Provides a consistent API for git operations across all phase scripts.
    Replaces 20+ duplicate inline git call patterns.
#>

#region Private Helper Functions

function _Test-GitAvailable {
    $null -ne (Get-Command git -ErrorAction SilentlyContinue)
}

function _Invoke-GitInternal {
    param(
        [string]$RepoPath,
        [string[]]$Args,
        [int]$TimeoutSec = 30
    )

    if (-not (_Test-GitAvailable)) {
        throw "Git is not installed or not in PATH"
    }

    $previousLocation = $null
    $originalErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"

    try {
        if ($RepoPath -and (Test-Path $RepoPath)) {
            $previousLocation = Get-Location
            Set-Location $RepoPath
        }

        $output = & git $Args 2>&1 | Out-String
        $exitCode = $LASTEXITCODE

        if ($exitCode -ne 0 -and $exitCode -ne 128) {
            Write-Warning "Git command exited with code ${exitCode}: git $($Args -join ' ')"
        }

        return @{
            output   = $output.Trim()
            exitCode = $exitCode
            success  = $exitCode -eq 0 -or $exitCode -eq 128
        }
    }
    finally {
        if ($previousLocation) {
            Set-Location $previousLocation
        }
        $ErrorActionPreference = $originalErrorAction
    }
}

#endregion

#region Public Functions

function Invoke-Git {
    <#
    .SYNOPSIS
        Run a git command in a repository directory.
    .DESCRIPTION
        Wraps git commands with automatic location handling and error capture.
        Restores the previous location in a finally block.
    .PARAMETER RepoPath
        Path to the repository (optional; if omitted, runs in current directory).
    .PARAMETER Args
        Git command arguments as an array (e.g., @('log', '--oneline', '-5')).
    .PARAMETER TimeoutSec
        Timeout in seconds (default: 30).
    .OUTPUTS
        Hashtable with { output, exitCode, success }.
    .EXAMPLE
        $result = Invoke-Git -RepoPath "C:\repos\myapp" -Args @('status')
        if ($result.success) { Write-Host $result.output }
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $false)]
        [string]$RepoPath,

        [Parameter(Mandatory = $true)]
        [string[]]$Args,

        [Parameter(Mandatory = $false)]
        [int]$TimeoutSec = 30
    )

    if (-not $RepoPath -or $RepoPath -eq "") {
        $RepoPath = $PWD.Path
    }

    if (-not (Test-Path $RepoPath)) {
        throw "Repository path does not exist: ${RepoPath}"
    }

    return _Invoke-GitInternal -RepoPath $RepoPath -Args $Args -TimeoutSec $TimeoutSec
}

function Test-IsGitRepo {
    <#
    .SYNOPSIS
        Test if a directory is a valid git repository.
    .DESCRIPTION
        Checks for the presence of a .git directory.
    .PARAMETER Path
        Path to test.
    .OUTPUTS
        Boolean.
    .EXAMPLE
        if (Test-IsGitRepo "C:\repos\myapp") { "Valid repo" }
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path
    )

    if ([string]::IsNullOrWhiteSpace($Path) -or -not (Test-Path $Path -PathType Container)) {
        return $false
    }

    $gitDir = Join-Path $Path ".git"
    return Test-Path $gitDir -PathType Container
}

function Get-GitInfo {
    <#
    .SYNOPSIS
        Get git repository information.
    .DESCRIPTION
        Returns a hashtable with remote URL, branch, commit count, and last commit date.
    .PARAMETER RepoPath
        Path to the repository.
    .OUTPUTS
        Hashtable with { remote_url, branch, commit_count, last_commit_date, days_since_last_commit }.
    .EXAMPLE
        $info = Get-GitInfo -RepoPath "C:\repos\myapp"
        Write-Host "Last commit: $($info.last_commit_date)"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$RepoPath
    )

    if (-not (Test-Path $RepoPath)) {
        return $null
    }

    $previousLocation = $null
    $originalErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"

    try {
        $previousLocation = Get-Location
        Set-Location $RepoPath

        $remoteUrl = & git config --get remote.origin.url 2>$null
        $branch = & git rev-parse --abbrev-ref HEAD 2>$null
        $commitCountRaw = & git rev-list --count HEAD 2>$null
        $lastCommitDate = & git log -1 --format="%ai" 2>$null

        Set-Location $previousLocation
        $previousLocation = $null

        $commitCount = 0
        if ($commitCountRaw -match '^\d+$') {
            $commitCount = [int]$commitCountRaw
        }

        $daysSinceLastCommit = -1
        if ($lastCommitDate -and $lastCommitDate -ne "") {
            try {
                $commitDateTime = [DateTime]::Parse($lastCommitDate)
                $daysSinceLastCommit = int.TotalDays
                if ($daysSinceLastCommit -lt 0) { $daysSinceLastCommit = -1 }
            }
            catch {
                $daysSinceLastCommit = -1
            }
        }

        return @{
            remote_url             = if ($remoteUrl) { $remoteUrl.Trim() } else { "" }
            branch                 = if ($branch) { $branch.Trim() } else { "unknown" }
            commit_count           = $commitCount
            last_commit_date       = if ($lastCommitDate) { $lastCommitDate.Trim() } else { "" }
            days_since_last_commit = $daysSinceLastCommit
        }
    }
    catch {
        # ignore
    }
    finally {
        if ($previousLocation) {
            Set-Location $previousLocation -ErrorAction SilentlyContinue
        }
        $ErrorActionPreference = $originalErrorAction
    }

    return $null
}

function Get-GitRemoteUrl {
    <#
    .SYNOPSIS
        Get the remote origin URL of a repository.
    .PARAMETER RepoPath
        Path to the repository.
    .OUTPUTS
        String URL or empty string if not available.
    .EXAMPLE
        $url = Get-GitRemoteUrl -RepoPath "C:\repos\myapp"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$RepoPath
    )

    if (-not (Test-Path $RepoPath)) {
        return ""
    }

    $previousLocation = $null
    $originalErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"

    try {
        $previousLocation = Get-Location
        Set-Location $RepoPath
        $url = & git config --get remote.origin.url 2>$null
        Set-Location $previousLocation
        $previousLocation = $null

        if ($url) {
            return $url.Trim()
        }
    }
    catch {
        # ignore
    }
    finally {
        if ($previousLocation) {
            Set-Location $previousLocation -ErrorAction SilentlyContinue
        }
        $ErrorActionPreference = $originalErrorAction
    }

    return ""
}

function Test-GitAccessible {
    <#
    .SYNOPSIS
        Test if a git repository is accessible and valid.
    .PARAMETER RepoPath
        Path to the repository.
    .OUTPUTS
        Hashtable with { valid, reason }.
    .EXAMPLE
        $check = Test-GitAccessible -RepoPath "C:\repos\myapp"
        if (-not $check.valid) { Write-Warning $check.reason }
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$RepoPath
    )

    if (-not (Test-Path $RepoPath)) {
        return @{ valid = $false; reason = "Path does not exist" }
    }

    $gitDir = Join-Path $RepoPath ".git"
    if (-not (Test-Path $gitDir -PathType Container)) {
        return @{ valid = $false; reason = "Not a git repository (.git directory missing)" }
    }

    $hasObjects = Test-Path (Join-Path $gitDir "objects") -PathType Container
    $hasRefs = Test-Path (Join-Path $gitDir "refs") -PathType Container
    $hasConfig = Test-Path (Join-Path $gitDir "config") -PathType Leaf

    if (-not ($hasObjects -and $hasRefs -and $hasConfig)) {
        return @{ valid = $false; reason = "Corrupted git repository (missing essential directories)" }
    }

    return @{ valid = $true; reason = "Repository is valid" }
}

function Get-GitHeadRef {
    <#
    .SYNOPSIS
        Get the current HEAD branch reference.
    .PARAMETER RepoPath
        Path to the repository.
    .OUTPUTS
        String branch name or "unknown".
    .EXAMPLE
        $branch = Get-GitHeadRef -RepoPath "C:\repos\myapp"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$RepoPath
    )

    if (-not (Test-Path $RepoPath)) {
        return "unknown"
    }

    $result = Invoke-Git -RepoPath $RepoPath -Args @('symbolic-ref', '--short', 'HEAD')
    if ($result.success) {
        return $result.output.Trim()
    }

    return "unknown"
}

function Get-GitCommitCount {
    <#
    .SYNOPSIS
        Get the total commit count of a repository.
    .PARAMETER RepoPath
        Path to the repository.
    .OUTPUTS
        Integer commit count or 0.
    .EXAMPLE
        $count = Get-GitCommitCount -RepoPath "C:\repos\myapp"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$RepoPath
    )

    $result = Invoke-Git -RepoPath $RepoPath -Args @('rev-list', '--count', 'HEAD')
    if ($result.success) {
        $count = 0
        if ([int]::TryParse($result.output.Trim(), [ref]$count)) {
            return $count
        }
    }

    return 0
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Invoke-Git'
    'Test-IsGitRepo'
    'Get-GitInfo'
    'Get-GitRemoteUrl'
    'Test-GitAccessible'
    'Get-GitHeadRef'
    'Get-GitCommitCount'
)
#endregion