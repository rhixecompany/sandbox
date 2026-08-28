#!/usr/bin/env powershell
<#
.SYNOPSIS
  Add recommended MCP servers to opencode.json and sync with Copilot/Codex configs

.DESCRIPTION
  Adds Stripe, Plaid, and other recommended MCP servers to opencode.json
  Then syncs the configuration to .copilot/mcp.json and .codex/mcp.json
#>

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

# Configuration
$workspaceRoot = "C:\Users\Alexa\Desktop\SandBox"
$opencodeJson = Join-Path $workspaceRoot "opencode.json"
$copilotMcp = Join-Path $workspaceRoot ".copilot\mcp.json"
$codexMcp = Join-Path $workspaceRoot ".codex\mcp.json"

# New MCP servers to add
$newServers = @{
    "stripe" = @{
        "enabled" = $true
        "type" = "remote"
        "url" = "https://mcp.stripe.com/mcp"
    }
    "plaid" = @{
        "enabled" = $true
        "type" = "remote"
        "url" = "https://mcp.plaid.com/mcp"
    }
    "anthropic-resources" = @{
        "enabled" = $true
        "type" = "remote"
        "url" = "https://resources.anthropic.com/mcp"
    }
    "evals" = @{
        "command" = @("bunx", "-y", "@modelcontextprotocol/server-evals")
        "enabled" = $true
        "type" = "local"
    }
    "time" = @{
        "command" = @("bunx", "-y", "@modelcontextprotocol/server-time")
        "enabled" = $true
        "type" = "local"
    }
    "everart" = @{
        "enabled" = $true
        "type" = "remote"
        "url" = "https://mcp.everart.ai/mcp"
    }
}

function Merge-McpServers {
    param(
        [PSCustomObject]$Base,
        [hashtable]$New
    )
    
    foreach ($serverName in $New.Keys) {
        if ($null -eq $Base.PSObject.Properties[$serverName]) {
            $Base | Add-Member -NotePropertyName $serverName -NotePropertyValue $New[$serverName]
            Write-Host "[+] Added: $serverName"
        } else {
            Write-Host "[-] Skipped: $serverName (already exists)"
        }
    }
    
    return $Base
}

function Sync-McpConfig {
    param(
        [string]$SourcePath,
        [string]$TargetPath,
        [string]$TargetName
    )
    
    # Read source (opencode.json)
    $sourceJson = Get-Content $SourcePath -Raw | ConvertFrom-Json
    
    # Read target
    $targetJson = Get-Content $TargetPath -Raw | ConvertFrom-Json
    
    # Sync mcp servers (convert opencode format to Copilot/Codex format)
    $sourceMcp = $sourceJson.mcp
    $targetMcpServers = $targetJson.mcpServers
    
    $syncCount = 0
    foreach ($serverName in $sourceMcp.PSObject.Properties.Name) {
        $sourceServer = $sourceMcp.$serverName
        $targetServer = $targetMcpServers.PSObject.Properties[$serverName]
        
        # Skip if target already exists (prefer manual customization)
        if ($null -ne $targetServer) {
            continue
        }
        
        # Convert opencode format to Copilot format
        $convertedServer = @{}
        
        if ($sourceServer.type -eq "remote") {
            $convertedServer["type"] = "http"
            $convertedServer["url"] = $sourceServer.url
        } elseif ($sourceServer.type -eq "local") {
            $convertedServer["type"] = "stdio"
            if ($null -ne $sourceServer.command) {
                if ($sourceServer.command -is [array]) {
                    $convertedServer["command"] = $sourceServer.command[0]
                    $convertedServer["args"] = $sourceServer.command[1..($sourceServer.command.Length-1)]
                } else {
                    $convertedServer["command"] = $sourceServer.command
                }
            }
            if ($null -ne $sourceServer.env) {
                $convertedServer["env"] = $sourceServer.env
            }
        }
        
        $targetJson.mcpServers | Add-Member -NotePropertyName $serverName -NotePropertyValue $convertedServer
        $syncCount++
    }
    
    if ($syncCount -gt 0) {
        if (-not $DryRun) {
            $targetJson | ConvertTo-Json -Depth 10 | Set-Content $TargetPath -Encoding UTF8
            Write-Host "[SYNC] ${TargetName}: Synced $syncCount servers"
        } else {
            Write-Host "[DRY-RUN] ${TargetName}: Would sync $syncCount servers"
        }
    } else {
        Write-Host "[OK] ${TargetName}: Already in sync"
    }
}

# Main
Write-Host "=========================================="
Write-Host "MCP Server Sync Script"
Write-Host "=========================================="
Write-Host ""

# Step 1: Add new servers to opencode.json
Write-Host "[1/3] Adding recommended servers to opencode.json..."
$opencodeContent = Get-Content $opencodeJson -Raw
$opencodeJson_obj = $opencodeContent | ConvertFrom-Json

$opencodeJson_obj.mcp = Merge-McpServers -Base $opencodeJson_obj.mcp -New $newServers

if (-not $DryRun) {
    $opencodeJson_obj | ConvertTo-Json -Depth 10 | Set-Content $opencodeJson -Encoding UTF8
    Write-Host "[+] Saved opencode.json"
} else {
    Write-Host "[DRY-RUN] Would save opencode.json"
}

Write-Host ""

# Step 2: Sync to .copilot/mcp.json
Write-Host "[2/3] Syncing to .copilot/mcp.json..."
Sync-McpConfig -SourcePath $opencodeJson -TargetPath $copilotMcp -TargetName ".copilot/mcp.json"

# Step 3: Sync to .codex/mcp.json
Write-Host "[3/3] Syncing to .codex/mcp.json..."
Sync-McpConfig -SourcePath $opencodeJson -TargetPath $codexMcp -TargetName ".codex/mcp.json"

Write-Host ""
Write-Host "=========================================="
Write-Host "Sync complete!"
Write-Host "=========================================="
Write-Host ""
Write-Host "Summary:"
Write-Host "  - opencode.json: canonical source"
Write-Host "  - .copilot/mcp.json: synced"
Write-Host "  - .codex/mcp.json: synced"
Write-Host ""
Write-Host "New servers added:"
$newServers.Keys | ForEach-Object { Write-Host "  + $_" }
