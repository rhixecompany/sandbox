#!/usr/bin/env bun
/**
 * Sync MCP Configuration
 *
 * Keeps opencode.json MCP section in sync with .vscode/mcp.json (canonical source)
 * Run this after any changes to .vscode/mcp.json
 */

import { readFileSync, writeFileSync } from "fs";
import { resolve } from "path";

const ROOT = resolve(import.meta.dirname, "..");
const VSCODE_MCP = resolve(ROOT, ".vscode", "mcp.json");
const OPENCODE_CONFIG = resolve(ROOT, "opencode.json");

interface MCPServer {
	command?: string[];
	args?: string[];
	type?: string;
	url?: string;
	enabled?: boolean;
	env?: Record<string, string>;
}

function main() {
	console.log("🔄 Syncing MCP configuration...");

	// Read canonical source
	const vscodeContent = readFileSync(VSCODE_MCP, "utf-8");
	const vscodeConfig = JSON.parse(vscodeContent);

	// Read target
	const opencodeContent = readFileSync(OPENCODE_CONFIG, "utf-8");
	const opencodeConfig = JSON.parse(opencodeContent);

	// Extract servers from vscode config (handles both 'servers' and 'mcpServers' keys)
	const vscodeServers = vscodeConfig.servers ?? vscodeConfig.mcpServers ?? {};
	const serverEntries = Object.entries(vscodeServers) as [string, MCPServer][];

	// Build new MCP section with lowercase keys
	const newMCPServers: Record<string, MCPServer> = {};
	for (const [key, server] of serverEntries) {
		const lowerKey = key.toLowerCase();
		newMCPServers[lowerKey] = server;
	}

	// Preserve OpenCode-specific config
	const newConfig = {
		...opencodeConfig,
		mcp: newMCPServers,
	};

	// Write back
	writeFileSync(OPENCODE_CONFIG, JSON.stringify(newConfig, null, "\t") + "\n");

	console.log(`✅ Synced ${Object.keys(newMCPServers).length} MCP servers from .vscode/mcp.json → opencode.json`);
	console.log(`   Servers: ${Object.keys(newMCPServers).join(", ")}`);
}

main();
