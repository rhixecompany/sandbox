#!/usr/bin/env bun
/**
 * Sync MCP Configuration
 */
import { readFileSync, writeFileSync } from "fs";
import { resolve } from "path";

function main(): void {
	const args = process.argv.slice(2);
	if (args.includes("--help") || args.length === 0) {
		console.log("Usage: sync-mcp-config.ts [--sync] [--check]");
		process.exit(0);
	}
	if (args.includes("--check")) {
		const vscode = JSON.parse(readFileSync(resolve(import.meta.dirname, "..", ".vscode", "mcp.json"), "utf-8"));
		const opencode = JSON.parse(readFileSync(resolve(import.meta.dirname, "..", "opencode.json"), "utf-8"));
		console.log(JSON.stringify(vscode) === JSON.stringify(opencode.mcp || {}) ? "In sync" : "Differ");
	}
	if (args.includes("--sync")) {
		const vscode = JSON.parse(readFileSync(resolve(import.meta.dirname, "..", ".vscode", "mcp.json"), "utf-8"));
		const opencode = JSON.parse(readFileSync(resolve(import.meta.dirname, "..", "opencode.json"), "utf-8"));
		opencode.mcp = vscode;
		writeFileSync(resolve(import.meta.dirname, "..", "opencode.json"), JSON.stringify(opencode, null, 2));
		console.log("Synced");
	}
}

main();
