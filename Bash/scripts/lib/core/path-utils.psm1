# path-utils.psm1
# PowerShell module for sandbox-aware path resolution

$script:SandboxRoot = $null
$script:ScriptRoot = $null

# Auto-detect sandbox root by finding nearest parent with 'scripts/' directory
function Initialize-SandboxRoot {
    $caller = $PSScriptRoot
    if (-not $caller) {
        $caller = $PSCommandPath ? (Split-Path -Parent $PSCommandPath) : $PWD.Path
    }

    $current = $caller
    while ($current) {
        $scriptsDir = Join-Path $current 'scripts'
        if (Test-Path $scriptsDir -PathType Container) {
            return $current
        }
        $parent = Split-Path -Parent $current
        if ($parent -eq $current) { break }
        $current = $parent
    }

    # Fallback: use caller's parent if no scripts/ found
    return (Split-Path -Parent $caller)
}

$script:SandboxRoot = Initialize-SandboxRoot
$script:ScriptRoot = $PSScriptRoot

function Get-SandboxRoot {
    <#
    .SYNOPSIS
        Returns the detected sandbox root directory.

    .DESCRIPTION
        Traverses upward from the script location to find the nearest parent
        directory containing a 'scripts/' subdirectory. This is the sandbox root.

    .OUTPUTS
        System.String - The sandbox root path.

    .EXAMPLE
        Get-SandboxRoot
        # Returns: C:\Users\Alexa\Desktop\SandBox
    #>
    [CmdletBinding()]
    param()

    return $script:SandboxRoot
}

function Get-ScriptRoot {
    <#
    .SYNOPSIS
        Returns the directory of the importing script or module.

    .DESCRIPTION
        Returns $PSScriptRoot, which is the directory containing the
        script that imported this module.

    .OUTPUTS
        System.String - The script root path.

    .EXAMPLE
        Get-ScriptRoot
        # Returns: C:\Users\Alexa\Desktop\SandBox\scripts\lib\core
    #>
    [CmdletBinding()]
    param()

    return $script:ScriptRoot
}

function Join-SandboxPath {
    <#
    .SYNOPSIS
        Joins path segments relative to the sandbox root.

    .DESCRIPTION
        Combines one or more path segments with the sandbox root directory.
        Use this for paths that should resolve relative to the repo root.

    .PARAMETER ChildPath
        One or more child path segments to join to the sandbox root.

    .OUTPUTS
        System.String - The full resolved path.

    .EXAMPLE
        Join-SandboxPath 'scripts' 'lib' 'core'
        # Returns: C:\Users\Alexa\Desktop\SandBox\scripts\lib\core
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$false, ValueFromPipeline=$true)]
        [string[]]$ChildPath
    )

    process {
        if ($ChildPath) {
            Join-Path $script:SandboxRoot (Join-Path @($ChildPath))
        } else {
            return $script:SandboxRoot
        }
    }
}

function Resolve-RepoPath {
    <#
    .SYNOPSIS
        Joins path segments relative to the script directory.

    .DESCRIPTION
        Combines path segments with $PSScriptRoot for paths relative to the
        importing script. Provides backward compatibility with older scripts.

    .PARAMETER ChildPath
        One or more child path segments to join to the script root.

    .OUTPUTS
        System.String - The full resolved path.

    .EXAMPLE
        Resolve-RepoPath 'config' 'settings.json'
        # Returns: C:\Users\Alexa\Desktop\SandBox\scripts\lib\core\config\settings.json
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$false, ValueFromPipeline=$true)]
        [string[]]$ChildPath
    )

    process {
        if ($ChildPath) {
            Join-Path $script:ScriptRoot (Join-Path @($ChildPath))
        } else {
            return $script:ScriptRoot
        }
    }
}

# Backward-compatibility alias
New-Alias -Name 'Resolve-ScriptPath' -Value 'Resolve-RepoPath' -Scope Global -ErrorAction SilentlyContinue

Export-ModuleMember -Function @(
    'Get-SandboxRoot',
    'Get-ScriptRoot',
    'Join-SandboxPath',
    'Resolve-RepoPath'
)