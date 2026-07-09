<#
.SYNOPSIS
    Ensures a directory exists, creating it if necessary.

.DESCRIPTION
    Tests if the specified path exists and is a directory. Creates the
    directory (and any parent directories) if missing. Returns the path.
    Replaces duplicate `if (-not (Test-Path $p)) { New-Item ... }` patterns.

.PARAMETER Path
    The directory path to ensure exists.

.EXAMPLE
    $auditDir = Ensure-Directory -Path "C:\Logs\Audit"

.EXAMPLE
    Ensure-Directory -Path "C:\Output\Results" | Out-Null
#>
function Ensure-Directory {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
    elseif (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "Path exists but is not a directory: $Path"
    }

    return $Path
}

<#
.SYNOPSIS
    Clears all contents from a directory.

.DESCRIPTION
    Removes all files and subdirectories from the specified directory
    while keeping the directory itself intact.

.PARAMETER Path
    The directory path to clear.

.EXAMPLE
    Clear-Directory -Path "C:\Temp\Cache"
#>
function Clear-Directory {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        Write-Verbose "Directory does not exist, nothing to clear: $Path"
        return
    }

    Get-ChildItem -LiteralPath $Path -Force | Remove-Item -Recurse -Force
}

<#
.SYNOPSIS
    Returns the REPO_AUDIT directory path and ensures it exists.

.DESCRIPTION
    Gets the path to the repository audit directory (REPO_AUDIT)
    and ensures the directory structure exists.

.EXAMPLE
    $auditDir = Get-AuditDir
#>
function Get-AuditDir {
    [CmdletBinding()]
    [OutputType([string])]
    param()

    $parentDir = Split-Path $PSScriptRoot -Parent
    $auditDir = Join-Path $parentDir '../REPO_AUDIT'
    return Ensure-Directory -Path $auditDir
}

<#
.SYNOPSIS
    Returns the BATCH_LOGS directory path and ensures it exists.

.DESCRIPTION
    Gets the path to the batch logs directory and ensures
    the directory structure exists.

.EXAMPLE
    $logsDir = Get-BatchLogsDir
#>
function Get-BatchLogsDir {
    [CmdletBinding()]
    [OutputType([string])]
    param()

    $parentDir = Split-Path $PSScriptRoot -Parent
    $logsDir = Join-Path $parentDir '../BATCH_LOGS'
    return Ensure-Directory -Path $logsDir
}

<#
.SYNOPSIS
    Returns the docs/audits directory path and ensures it exists.

.DESCRIPTION
    Gets the path to the documentation audits directory and ensures
    the directory structure exists.

.EXAMPLE
    $auditsDir = Get-AuditsDir
#>
function Get-AuditsDir {
    [CmdletBinding()]
    [OutputType([string])]
    param()

    $parentDir = Split-Path $PSScriptRoot -Parent
    $parentParentDir = Split-Path $parentDir -Parent
    $auditsDir = Join-Path $parentParentDir 'docs/audits'
    return Ensure-Directory -Path $auditsDir
}

<#
.SYNOPSIS
    Removes a directory safely with optional confirmation.

.DESCRIPTION
    Removes the specified directory and all its contents. If -Confirm
    is specified, prompts for confirmation before deletion.

.PARAMETER Path
    The directory path to remove.

.PARAMETER Confirm
    If specified, prompts for confirmation before removing.

.EXAMPLE
    Remove-DirectorySafely -Path "C:\Temp\OldData" -Confirm

.EXAMPLE
    Remove-DirectorySafely -Path "C:\Temp\OldData"
#>
function Remove-DirectorySafely {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path,
        [Parameter()]
        [switch]$Confirm
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        Write-Verbose "Directory does not exist: $Path"
        return
    }

    if ($Confirm -and -not $PSCmdlet.ShouldContinue("Remove directory?", "$Path")) {
        Write-Verbose "Deletion cancelled by user: $Path"
        return
    }

    Remove-Item -LiteralPath $Path -Recurse -Force
}

Export-ModuleMember -Function @(
    'Ensure-Directory',
    'Clear-Directory',
    'Get-AuditDir',
    'Get-BatchLogsDir',
    'Get-AuditsDir',
    'Remove-DirectorySafely'
)