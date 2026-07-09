#Requires -Version 5.1
<#
.SYNOPSIS
    Logger module for standardized colored console output with timestamps
.DESCRIPTION
    Provides consistent, styled output functions for all phase scripts.
    Replaces duplicate inline Write-Host patterns across all scripts.
#>

#region Module Variables
$script:LoggerIndentLevel = 0
$script:LoggerIndentSize = 2
#endregion

#region Private Helper Functions

function _Get-Timestamp {
    return Get-Date -Format "HH:mm:ss"
}

function _Get-Indent {
    if ($script:LoggerIndentLevel -le 0) { return "" }
    return " " * ($script:LoggerIndentLevel * $script:LoggerIndentSize)
}

function _Write-ColorOutput {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message,

        [Parameter(Mandatory = $false)]
        [ConsoleColor]$Color = [ConsoleColor]::White
    )
    $indent = _Get-Indent
    $originalColor = $Host.UI.RawUI.ForegroundColor
    try {
        $Host.UI.RawUI.ForegroundColor = $Color
        Write-Host "${indent}${Message}"
    }
    finally {
        $Host.UI.RawUI.ForegroundColor = $originalColor
    }
}

#endregion

#region Public Functions

function Write-Phase {
    <#
    .SYNOPSIS
        Write a phase header with timestamp.
    .DESCRIPTION
        Displays a message with the >>> prefix, timestamp, and cyan color.
        Used to mark the start of a major operation or phase.
    .PARAMETER Message
        The message to display.
    .EXAMPLE
        Write-Phase "Phase 1: Discovery"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        $timestamp = _Get-Timestamp
        _Write-ColorOutput ">>> [${timestamp}] ${Message}" -Color Cyan
    }
}

function Write-Success {
    <#
    .SYNOPSIS
        Write a success message.
    .DESCRIPTION
        Displays a message with the ✓ prefix in green.
        Used for completed operations and positive outcomes.
    .PARAMETER Message
        The success message to display.
    .EXAMPLE
        Write-Success "Phase 1 completed"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        _Write-ColorOutput "✓ ${Message}" -Color Green
    }
}

function Write-Warn {
    <#
    .SYNOPSIS
        Write a warning message.
    .DESCRIPTION
        Displays a message with the ⚠ prefix in yellow.
        Used for non-fatal issues, skipped items, and caution notices.
    .PARAMETER Message
        The warning message to display.
    .EXAMPLE
        Write-Warn "Skipping invalid repo"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        _Write-ColorOutput "⚠ ${Message}" -Color Yellow
    }
}

function Write-Err {
    <#
    .SYNOPSIS
        Write an error message.
    .DESCRIPTION
        Displays a message with the ✗ prefix in red.
        Used for failures, exceptions, and critical issues.
    .PARAMETER Message
        The error message to display.
    .EXAMPLE
        Write-Err "Config file not found"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        _Write-ColorOutput "✗ ${Message}" -Color Red
    }
}

function Write-Info {
    <#
    .SYNOPSIS
        Write an informational message.
    .DESCRIPTION
        Displays a message in white with no prefix.
        Used for general progress and status information.
    .PARAMETER Message
        The message to display.
    .EXAMPLE
        Write-Info "Processing 5 repositories..."
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        _Write-ColorOutput "${Message}" -Color White
    }
}

function Write-Debug-Message {
    <#
    .SYNOPSIS
        Write a debug message (only if Verbose is enabled).
    .DESCRIPTION
        Displays a message in gray only when -Verbose switch is used.
        Used for detailed diagnostic information.
    .PARAMETER Message
        The debug message to display.
    .EXAMPLE
        Write-Debug-Message "Entering function X"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Message
    )
    process {
        if ($VerbosePreference -eq 'Continue') {
            $timestamp = _Get-Timestamp
            _Write-ColorOutput "[DEBUG][${timestamp}] ${Message}" -Color Gray
        }
    }
}

function Write-Header {
    <#
    .SYNOPSIS
        Write a section header banner.
    .DESCRIPTION
        Displays a double-line cyan banner with centered text.
        Used to mark the beginning of major sections.
    .PARAMETER Text
        The header text to display.
    .EXAMPLE
        Write-Header "Repository Audit Report"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Text
    )
    process {
        $width = 48
        $padding = [Math]::Max(0, [Math]::Floor(($width - $Text.Length) / 2))
        $paddedText = (" " * $padding) + $Text
        _Write-ColorOutput "" -Color Cyan
        _Write-ColorOutput ("=" * $width) -Color Cyan
        _Write-ColorOutput $paddedText -Color Cyan
        _Write-ColorOutput ("=" * $width) -Color Cyan
        _Write-ColorOutput "" -Color Cyan
    }
}

function Write-SubHeader {
    <#
    .SYNOPSIS
        Write a sub-section header (underline style).
    .DESCRIPTION
        Displays the text with a cyan underline.
        Used for sub-sections within a major section.
    .PARAMETER Text
        The sub-header text.
    .EXAMPLE
        Write-SubHeader "Clone Results"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [AllowEmptyString()]
        [string]$Text
    )
    process {
        _Write-ColorOutput "" -Color Cyan
        _Write-ColorOutput $Text -Color Cyan
        _Write-ColorOutput ("=" * $Text.Length) -Color Cyan
    }
}

function Write-Table-Output {
    <#
    .SYNOPSIS
        Write data as a formatted table.
    .DESCRIPTION
        Displays key-value pairs or array items as an aligned table.
        Works with arrays of hashtables or simple value arrays.
    .PARAMETER Data
        A hashtable or array of hashtables to display as a table.
    .PARAMETER Columns
        Optional column names to display (for hashtable arrays).
    .EXAMPLE
        Write-Table-Output @{ Name = "repo1"; Status = "OK" }
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [object]$Data,

        [Parameter(Mandatory = $false)]
        [string[]]$Columns
    )

    if ($null -eq $Data) {
        _Write-ColorOutput "  (empty)" -Color Gray
        return
    }

    if ($Data -is [hashtable]) {
        $maxKey = 0
        foreach ($key in $Data.Keys) {
            if ($key.Length -gt $maxKey) { $maxKey = $key.Length }
        }
        foreach ($key in $Data.Keys) {
            $value = if ($null -ne $Data[$key]) { $Data[$key].ToString() } else { "(null)" }
            $line = "  {0,-$maxKey} : {1}" -f $key, $value
            _Write-ColorOutput $line -Color White
        }
    }
    elseif ($Data -is [array] -or $Data -is [System.Collections.IEnumerable]) {
        $arr = @($Data)
        if ($arr.Count -eq 0) {
            _Write-ColorOutput "  (empty)" -Color Gray
            return
        }
        foreach ($item in $arr) {
            if ($item -is [hashtable]) {
                foreach ($key in $item.Keys) {
                    $value = if ($null -ne $item[$key]) { $item[$key].ToString() } else { "(null)" }
                    _Write-ColorOutput "  ${key}: ${value}" -Color White
                }
                _Write-ColorOutput "" -Color White
            }
            else {
                _Write-ColorOutput "  ${item}" -Color White
            }
        }
    }
    else {
        _Write-ColorOutput "  ${Data}" -Color White
    }
}

function Write-Progress-Custom {
    <#
    .SYNOPSIS
        Write inline progress with index and total.
    .DESCRIPTION
        Displays [current/total] prefix for batch operations.
    .PARAMETER Current
        Current item index.
    .PARAMETER Total
        Total item count.
    .PARAMETER Message
        Optional message to display after the counter.
    .EXAMPLE
        Write-Progress-Custom -Current 3 -Total 10 -Message "Cloning repo"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [int]$Current,

        [Parameter(Mandatory = $true)]
        [int]$Total,

        [Parameter(Mandatory = $false)]
        [string]$Message = ""
    )
    $msg = if ($Message) { " ${Message}" } else { "" }
    _Write-ColorOutput "[${Current}/${Total}]${msg}" -Color Yellow
}

function Push-Indent {
    <#
    .SYNOPSIS
        Increase indentation level for subsequent log messages.
    .EXAMPLE
        Push-Indent
        Write-Info "Inside section"
        Pop-Indent
    #>
    [CmdletBinding()]
    param()
    $script:LoggerIndentLevel++
}

function Pop-Indent {
    <#
    .SYNOPSIS
        Decrease indentation level.
    .EXAMPLE
        Push-Indent
        Write-Info "Inside section"
        Pop-Indent
    #>
    [CmdletBinding()]
    param()
    if ($script:LoggerIndentLevel -gt 0) {
        $script:LoggerIndentLevel--
    }
}

function Reset-Indent {
    <#
    .SYNOPSIS
        Reset indentation to zero.
    #>
    [CmdletBinding()]
    param()
    $script:LoggerIndentLevel = 0
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Write-Phase'
    'Write-Success'
    'Write-Warn'
    'Write-Err'
    'Write-Info'
    'Write-Debug-Message'
    'Write-Header'
    'Write-SubHeader'
    'Write-Table-Output'
    'Write-Progress-Custom'
    'Push-Indent'
    'Pop-Indent'
    'Reset-Indent'
)
#endregion