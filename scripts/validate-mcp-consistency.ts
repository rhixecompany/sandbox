#!/usr/bin/env bun
/**
 * Validate MCP Configuration Consistency
 *
 * CI check: Ensures no project has duplicate/outdated .vscode/mcp.json files
 * Projects should inherit from root .vscode/mcp.json
 * Only exceptions: projects with unique minimal configs (e.g., Banking/.cursor/mcp.json)
 */

import { readFileSync, readdirSync, statSync } from "fs";
import { resolve, join, sep } from "path";

const ROOT = resolve(import.meta.dirname, "..");
const CANONICAL_MCP = resolve(ROOT, ".vscode", "mcp.json");

// Normalize path for comparison (handle Windows backslashes)
function normPath(p: string): string {
	return p.split(sep).join("/");
}

// Files that are allowed to exist (non-.vscode/mcp.json or tool-specific)
const ALLOWED_MCP_FILES = new Set([".codex/mcp.json", ".copilot/mcp.json", "projects/Banking/.cursor/mcp.json"]);

// Projects allowed to have their own .vscode/mcp.json
const ALLOWED_PROJECT_EXCEPTIONS = new Set<string>();

function getAllMCPFiles(): string[] {
	const results: string[] = [];

	function scan(dir: string, base = "") {
		const entries = readdirSync(dir);
		for (const entry of entries) {
			const fullPath = join(dir, entry);
			const relPath = base ? join(base, entry) : entry;
			const stat = statSync(fullPath);

			if (stat.isDirectory()) {
				if (![".git", "node_modules", "dist", "build", ".next", "target", ".turbo"].includes(entry)) {
					scan(fullPath, relPath);
				}
			} else if (entry === "mcp.json") {
				results.push(normPath(relPath));
			}
		}
	}

	scan(ROOT);
	return results;
}

function compareConfigs(file1: string, file2: string): boolean {
	try {
		const content1 = readFileSync(file1, "utf-8");
		const content2 = readFileSync(file2, "utf-8");
		const norm1 = JSON.stringify(JSON.parse(content1), null, 0);
		const norm2 = JSON.stringify(JSON.parse(content2), null, 0);
		return norm1 === norm2;
	} catch {
		return false;
	}
}

function main() {
	console.log("🔍 Validating MCP configuration consistency...\n");

	const allMCPFiles = getAllMCPFiles();

	let violations = 0;
	let checked = 0;
	let allowed = 0;

	for (const relPath of allMCPFiles) {
		const fullPath = resolve(ROOT, relPath);

		// Skip canonical source
		if (relPath === ".vscode/mcp.json") continue;

		// Skip allowed exceptions
		if (ALLOWED_MCP_FILES.has(relPath)) {
			console.log(`✅ Allowed exception: ${relPath}`);
			allowed++;
			continue;
		}

		// Check if it's a project .vscode/mcp.json
		const projectMatch = relPath.match(/^projects\/([^/]+)\/.vscode\/mcp\.json$/);
		if (projectMatch) {
			const projectName = projectMatch[1];

			if (ALLOWED_PROJECT_EXCEPTIONS.has(projectName)) {
				console.log(`✅ Allowed project exception: ${relPath}`);
				allowed++;
				continue;
			}

			// Check if identical to canonical
			if (compareConfigs(fullPath, CANONICAL_MCP)) {
				console.log(`❌ VIOLATION: ${relPath} duplicates root .vscode/mcp.json`);
				console.log(`   → Delete this file; project should inherit from root`);
				violations++;
			} else {
				console.log(`⚠️  DIFFERS: ${relPath} differs from canonical`);
				console.log(`   → Review: is this intentional? If so, add to ALLOWED_PROJECT_EXCEPTIONS`);
				violations++;
			}
			checked++;
		} else {
			console.log(`⚠️  UNKNOWN: ${relPath} - not in allowed list, not project .vscode/mcp.json`);
			violations++;
		}
	}

	console.log(`\n📊 Summary: ${checked} project configs checked, ${allowed} allowed, ${violations} violations`);

	if (violations > 0) {
		console.log("\n💡 Fix: Delete duplicate files or add to allowed lists in this script");
		process.exit(1);
	} else {
		console.log("\n✅ All MCP configurations are consistent!");
		process.exit(0);
	}
}

main();
