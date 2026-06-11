#Requires -Version 5.1
<#
.SYNOPSIS
    Batch service module for grouping and managing fix batches

.DESCRIPTION
    Provides functions to group findings into batches, apply fixes,
    track batch status, and generate batch reports. Uses dir-manager
    for directory operations and logger for output.
#>

#region Module Dependencies
Import-Module (Join-Path $PSScriptRoot '../core/path-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/dir-manager.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/logger.psm1') -Force
#endregion

#region Module Variables
$script:DefaultMaxBatchSize = 7
#endregion

#region Public Functions

function New-BatchGroup {
    <#
    .SYNOPSIS
        Groups findings into batches of max specified size

    .DESCRIPTION
        Takes an array of findings and groups them into batches of
        max $MaxBatchSize (default 7). Groups by complexity/severity
        to ensure related fixes stay together.

    .PARAMETER Findings
        Array of finding hashtables to group

    .PARAMETER MaxBatchSize
        Maximum number of findings per batch (default: 7)

    .OUTPUTS
        Array of batch hashtables

    .EXAMPLE
        $batches = New-BatchGroup -Findings $allFindings
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Findings,

        [Parameter(Mandatory=$false)]
        [int]$MaxBatchSize = $script:DefaultMaxBatchSize
    )

    if ($Findings.Count -eq 0) {
        return @()
    }

    # Sort findings by severity (critical first)
    $severityOrder = @{
        "critical" = 0
        "high" = 1
        "medium" = 2
        "low" = 3
        "info" = 4
    }

    $sortedFindings = $Findings | Sort-Object {
        $severity = if ($_.severity) { $_.severity.ToLower() } else { "info" }
        $order = if ($severityOrder.ContainsKey($severity)) { $severityOrder[$severity] } else { 4 }
        $order
    }

    $batches = @()
    $currentBatch = @{
        id = 1
        findings = @()
        complexity = 0
    }

    foreach ($finding in $sortedFindings) {
        # Calculate complexity (simple heuristic)
        $complexity = 1
        if ($finding.files_modified) {
            $complexity = $finding.files_modified.Count
        }

        # Check if adding this finding would exceed max size or complexity
        $wouldExceedSize = ($currentBatch.findings.Count + 1) -gt $MaxBatchSize
        $wouldExceedComplexity = ($currentBatch.complexity + $complexity) -gt ($MaxBatchSize * 2)

        if ($wouldExceedSize -or $wouldExceedComplexity) {
            # Save current batch and start new one
            if ($currentBatch.findings.Count -gt 0) {
                $batches += $currentBatch
            }

            $currentBatch = @{
                id = $batches.Count + 1
                findings = @()
                complexity = 0
            }
        }

        $currentBatch.findings += $finding
        $currentBatch.complexity += $complexity
    }

    # Add final batch if not empty
    if ($currentBatch.findings.Count -gt 0) {
        $batches += $currentBatch
    }

    # Add metadata to each batch
    foreach ($batch in $batches) {
        $batch | Add-Member -NotePropertyName "total_findings" -NotePropertyValue $batch.findings.Count -PassThru | Out-Null
        $batch | Add-Member -NotePropertyName "max_size" -NotePropertyValue $MaxBatchSize -PassThru | Out-Null
    }

    return $batches
}

function Apply-BatchFix {
    <#
    .SYNOPSIS
        Applies fixes for a batch (placeholder)

    .DESCRIPTION
        Placeholder function that records the intent to apply fixes
        for a batch. In a real implementation, this would execute
        the actual fix commands.

    .PARAMETER Batch
        Batch hashtable with findings to apply

    .PARAMETER DryRun
        If $true, only simulates the fix without applying

    .OUTPUTS
        Hashtable with fix application results

    .EXAMPLE
        $result = Apply-BatchFix -Batch $batch -DryRun $true
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Batch,

        [Parameter(Mandatory=$false)]
        [switch]$DryRun
    )

    $result = @{
        batch_id = $Batch.id
        status = "pending"
        applied = @()
        failed = @()
        dry_run = $DryRun.IsPresent
    }

    if ($DryRun.IsPresent) {
        $result.status = "dry_run"
        $result.message = "Dry run mode - no fixes applied"
        Write-Info "Dry run: Would apply $($Batch.findings.Count) fixes for batch $($Batch.id)"
        return $result
    }

    # Placeholder: In real implementation, iterate through findings and apply fixes
    $result.status = "not_implemented"
    $result.message = "Batch fix application not implemented - placeholder"

    Write-Warn "Batch fix application is a placeholder - not actually applying fixes"

    return $result
}

function Get-BatchStatus {
    <#
    .SYNOPSIS
        Returns status of a batch

    .DESCRIPTION
        Returns the current status of a batch: pending, in-progress,
        complete, or failed.

    .PARAMETER Batch
        Batch hashtable to check status

    .OUTPUTS
        String status value

    .EXAMPLE
        $status = Get-BatchStatus -Batch $batch
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Batch
    )

    if ($Batch.status) {
        return $Batch.status
    }

    return "pending"
}

function New-BatchLog {
    <#
    .SYNOPSIS
        Creates a batch log entry

    .DESCRIPTION
        Creates a structured log entry for batch execution including
        timestamp, batch ID, status, and results.

    .PARAMETER Batch
        Batch hashtable being executed

    .PARAMETER Status
        Execution status (started, completed, failed)

    .PARAMETER Results
        Optional results hashtable from execution

    .OUTPUTS
        Hashtable representing the log entry

    .EXAMPLE
        $log = New-BatchLog -Batch $batch -Status "started"
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Batch,

        [Parameter(Mandatory=$true)]
        [ValidateSet("started", "completed", "failed")]
        [string]$Status,

        [Parameter(Mandatory=$false)]
        [hashtable]$Results = @{}
    )

    $log = @{
        timestamp = (Get-Date -Format "o")
        batch_id = $Batch.id
        status = $Status
        findings_count = $Batch.findings.Count
    }

    if ($Results) {
        $log.results = $Results
    }

    return $log
}

function Format-BatchReport {
    <#
    .SYNOPSIS
        Formats batch execution as markdown

    .DESCRIPTION
        Creates a formatted markdown report from batch execution
        results, suitable for documentation or reporting.

    .PARAMETER Batches
        Array of batch hashtables with execution results

    .PARAMETER Title
        Optional title for the report

    .OUTPUTS
        String containing markdown formatted report

    .EXAMPLE
        $report = Format-BatchReport -Batches $executedBatches
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Batches,

        [Parameter(Mandatory=$false)]
        [string]$Title = "Batch Execution Report"
    )

    $sb = [System.Text.StringBuilder]::new()

    [void]$sb.AppendLine("# $Title")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
    [void]$sb.AppendLine("")

    # Summary
    $totalBatches = $Batches.Count
    $totalFindings = ($Batches | Measure-Object -Property findings_count -Sum).Sum

    [void]$sb.AppendLine("## Summary")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("| Metric | Value |")
    [void]$sb.AppendLine("|--------|-------|")
    [void]$sb.AppendLine("| Total Batches | $totalBatches |")
    [void]$sb.AppendLine("| Total Findings | $totalFindings |")
    [void]$sb.AppendLine("")

    # Batch details
    [void]$sb.AppendLine("## Batch Details")
    [void]$sb.AppendLine("")

    foreach ($batch in $Batches) {
        $status = if ($batch.status) { $batch.status } else { "pending" }

        [void]$sb.AppendLine("### Batch $($batch.id)")
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine("- **Status:** $status")
        [void]$sb.AppendLine("- **Findings:** $($batch.findings.Count)")

        if ($batch.complexity) {
            [void]$sb.AppendLine("- **Complexity:** $($batch.complexity)")
        }

        if ($batch.findings -and $batch.findings.Count -gt 0) {
            [void]$sb.AppendLine("")
            [void]$sb.AppendLine("**Findings:**")

            foreach ($finding in $batch.findings) {
                $findingId = if ($finding.id) { $finding.id } else { "unknown" }
                $severity = if ($finding.severity) { $finding.severity } else { "unknown" }
                $description = if ($finding.description) { $finding.description } else { "No description" }

                [void]$sb.AppendLine("- `$findingId` ($severity): $description")
            }
        }

        [void]$sb.AppendLine("")
    }

    return $sb.ToString()
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'New-BatchGroup'
    'Apply-BatchFix'
    'Get-BatchStatus'
    'New-BatchLog'
    'Format-BatchReport'
)
#endregion