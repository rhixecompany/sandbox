<#
.SYNOPSIS
    Imports and validates a JSON configuration file.

.DESCRIPTION
    Loads a JSON configuration file from scripts/config/{Name}-config.json,
    validates it's valid JSON, and returns a PowerShell object.
    Throws an error if the file is missing or contains invalid JSON.

.PARAMETER Name
    The base name of the config file (without the -config.json suffix).

.EXAMPLE
    Import-Config -Name "repo-inventory"

.EXAMPLE
    $config = Import-Config "discovery"
#>
function Import-Config {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]$Name
    )

    $configPath = Get-ConfigPath -Name $Name

    if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) {
        throw "Configuration file not found: $configPath"
    }

    try {
        $jsonContent = Get-Content -LiteralPath $configPath -Raw -Encoding UTF8
        $config = $jsonContent | ConvertFrom-Json
        return $config
    }
    catch {
        throw "Failed to parse config file '$configPath': $($_.Exception.Message)"
    }
}

<#
.SYNOPSIS
    Returns the resolved path to a configuration file.

.DESCRIPTION
    Constructs the full path to a config file in scripts/config/ directory.
    Does not verify the file exists.

.PARAMETER Name
    The base name of the config file (without the -config.json suffix).

.EXAMPLE
    $path = Get-ConfigPath -Name "clone-config"
#>
function Get-ConfigPath {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]$Name
    )

    $configDir = Join-Path $PSScriptRoot '../../config'
    $configPath = Join-Path $configDir "$Name-config.json"
    return $configPath
}

<#
.SYNOPSIS
    Loads the repository inventory configuration.

.DESCRIPTION
    Returns the parsed repo-inventory.json configuration containing
    the list of repositories to process.

.EXAMPLE
    $repos = Get-RepoInventory
    $repos | ForEach-Object { $_.name }
#>
function Get-RepoInventory {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()

    return Import-Config -Name "repo-inventory"
}

<#
.SYNOPSIS
    Loads the discovery configuration.

.DESCRIPTION
    Returns the parsed discovery-config.json configuration containing
    settings for the discovery phase.

.EXAMPLE
    $discoveryConfig = Get-DiscoveryConfig
#>
function Get-DiscoveryConfig {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()

    return Import-Config -Name "discovery-config"
}

<#
.SYNOPSIS
    Loads the clone configuration.

.DESCRIPTION
    Returns the parsed clone-config.json configuration containing
    settings for the cloning phase.

.EXAMPLE
    $cloneConfig = Get-CloneConfig
#>
function Get-CloneConfig {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()

    return Import-Config -Name "clone-config"
}

<#
.SYNOPSIS
    Loads the triage configuration.

.DESCRIPTION
    Returns the parsed triage-config.json configuration containing
    settings for the triage phase.

.EXAMPLE
    $triageConfig = Get-TriageConfig
#>
function Get-TriageConfig {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()

    return Import-Config -Name "triage-config"
}

<#
.SYNOPSIS
    Loads the diagnostics configuration if it exists.

.DESCRIPTION
    Returns the parsed diagnostics-config.json configuration containing
    settings for diagnostics. Returns $null if the file doesn't exist.

.EXAMPLE
    $diagConfig = Get-DiagnosticsConfig
    if ($null -ne $diagConfig) { ... }
#>
function Get-DiagnosticsConfig {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()

    $configPath = Get-ConfigPath -Name "diagnostics-config"

    if (Test-Path -LiteralPath $configPath -PathType Leaf) {
        return Import-Config -Name "diagnostics-config"
    }

    return $null
}

Export-ModuleMember -Function @(
    'Import-Config',
    'Get-ConfigPath',
    'Get-RepoInventory',
    'Get-DiscoveryConfig',
    'Get-CloneConfig',
    'Get-TriageConfig',
    'Get-DiagnosticsConfig'
)