/**
 * Quality Gate Triage Script
 *
 * Parses quality gate report files (type-check.txt, lint-strict.txt,
 * test-report.txt, build-report.txt) and produces a triaged JSON summary
 * with severity categories, affected files, and fix suggestions.
 *
 * Usage: tsx --env-file=.env.local src/scripts/triage-quality-gate.ts
 * Output: quality-gate-triage.json + colored console summary
 * Exit: 0 if no CRITICAL/HIGH, 1 otherwise
 */

import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

// ── ANSI Colors ────────────────────────────────────────────────────────────
const C = {
  RESET: "\x1b[0m",
  BOLD: "\x1b[1m",
  RED: "\x1b[31m",
  GREEN: "\x1b[32m",
  YELLOW: "\x1b[33m",
  CYAN: "\x1b[36m",
  GRAY: "\x1b[90m",
  MAGENTA: "\x1b[35m",
} as const;

// ── Types ──────────────────────────────────────────────────────────────────
type Severity = "CRITICAL" | "HIGH" | "LOW" | "MEDIUM";
type Category = "build" | "eslint" | "test" | "typescript";

interface TriageIssue {
  autoFix: null | string;
  category: Category;
  code: null | string;
  column: null | number;
  file: string;
  line: null | number;
  message: string;
  severity: Severity;
}

interface TriageSuggestion {
  action: string;
  count: number;
}

interface TriageReport {
  issues: TriageIssue[];
  suggestions: TriageSuggestion[];
  summary: {
    autoFixable: number;
    critical: number;
    high: number;
    low: number;
    medium: number;
    topFiles: string[];
    total: number;
  };
  timestamp: string;
}

// ── Helpers ────────────────────────────────────────────────────────────────
function readReport(filename: string): null | string {
  const filepath = resolve(process.cwd(), filename);
  if (!existsSync(filepath)) return null;
  return readFileSync(filepath, "utf-8");
}

// ── Parsers ────────────────────────────────────────────────────────────────

/**
 * Parse TypeScript errors from type-check.txt
 * Format: src/file.ts(12,5): error TS2322: Type 'string' is not assignable to type 'number'
 */
function parseTypeScriptErrors(content: string): TriageIssue[] {
  const issues: TriageIssue[] = [];
  const regex = /^(.+)\((\d+),(\d+)\):\s+error\s+(TS\d+):\s+(.+)$/gm;
  let match;
  while ((match = regex.exec(content)) !== null) {
    issues.push({
      severity: "CRITICAL",
      category: "typescript",
      file: match[1].trim(),
      line: parseInt(match[2], 10),
      column: parseInt(match[3], 10),
      code: match[4],
      message: match[5].trim(),
      autoFix: null,
    });
  }
  return issues;
}

/**
 * Parse ESLint errors/warnings from lint-fixed.txt
 * Format:
 *   /path/to/file.ts
 *     12:5  error  Some message  rule-name
 *     15:1  warning  Another msg  other-rule
 */
function parseEslintIssues(content: string): TriageIssue[] {
  const issues: TriageIssue[] = [];
  let currentFile = "";

  const lines = content.split("\n");
  for (const line of lines) {
    // Detect file header lines (absolute or relative paths, no leading whitespace)
    const fileMatch = line.match(/^([A-Za-z]:\\[^\s].*|\/[^\s].*|\S+\.\w+)$/);
    if (fileMatch) {
      currentFile = fileMatch[1];
      continue;
    }

    // Detect ESLint issue lines
    const issueMatch = line.match(/^\s+(\d+):(\d+)\s+(error|warning)\s+(.+?)\s{2,}(\S+)\s*$/);
    if (issueMatch && currentFile) {
      const eslintSeverity = issueMatch[3];
      const rule = issueMatch[5];
      const isAutoFixable =
        rule.includes("/") ||
        ["semi", "quotes", "indent", "comma-dangle", "no-trailing-spaces", "eol-last", "prettier/prettier"].includes(
          rule
        );

      issues.push({
        severity: eslintSeverity === "error" ? "HIGH" : "MEDIUM",
        category: "eslint",
        file: currentFile,
        line: parseInt(issueMatch[1], 10),
        column: parseInt(issueMatch[2], 10),
        code: rule,
        message: issueMatch[4].trim(),
        autoFix: isAutoFixable ? "pnpm lint:fix" : null,
      });
    }
  }
  return issues;
}

/**
 * Parse Vitest test failures from test-report.txt
 * Looks for FAIL markers and extracts test file + error info
 */
function parseTestFailures(content: string): TriageIssue[] {
  const issues: TriageIssue[] = [];

  // Match FAIL lines: ❌ FAIL  src/tests/file.test.ts > suite > test name
  const failRegex = /FAIL\s+(.+?\.(?:test|spec)\.\w+)\s*(?:>\s*(.+))?$/gm;
  let match;
  while ((match = failRegex.exec(content)) !== null) {
    issues.push({
      severity: "HIGH",
      category: "test",
      file: match[1].trim(),
      line: null,
      column: null,
      code: null,
      message: match[2]?.trim() || "Test failed",
      autoFix: null,
    });
  }

  // Match AssertionError blocks for more detail
  const assertRegex = /AssertionError:\s+(.+?)(?:\n\s+Expected:\s+(.+?))?(?:\n\s+Received:\s+(.+?))?$/gm;
  while ((match = assertRegex.exec(content)) !== null) {
    // Avoid duplicating — only add if we don't already have an issue for this
    const msg = match[1].trim();
    if (!issues.some((i) => i.message.includes(msg))) {
      issues.push({
        severity: "HIGH",
        category: "test",
        file: "unknown",
        line: null,
        column: null,
        code: null,
        message: msg,
        autoFix: null,
      });
    }
  }

  return issues;
}

/**
 * Parse Next.js build errors from build-report.txt
 * Looks for Error:, Module not found, Type error: patterns
 */
function parseBuildErrors(content: string): TriageIssue[] {
  const issues: TriageIssue[] = [];

  // Match "Type error:" lines
  const typeErrRegex = /Type error:\s+(.+?)(?:\n|$)/gm;
  let match;
  while ((match = typeErrRegex.exec(content)) !== null) {
    issues.push({
      severity: "CRITICAL",
      category: "build",
      file: "build",
      line: null,
      column: null,
      code: "BUILD_TYPE_ERROR",
      message: match[1].trim(),
      autoFix: null,
    });
  }

  // Match "Module not found:" lines
  const moduleRegex = /Module not found:\s+(.+?)(?:\n|$)/gm;
  while ((match = moduleRegex.exec(content)) !== null) {
    issues.push({
      severity: "CRITICAL",
      category: "build",
      file: "build",
      line: null,
      column: null,
      code: "MODULE_NOT_FOUND",
      message: match[1].trim(),
      autoFix: null,
    });
  }

  // Match generic "Error:" lines (not already captured above)
  const errorRegex = /^Error:\s+(.+?)$/gm;
  while ((match = errorRegex.exec(content)) !== null) {
    const msg = match[1].trim();
    if (!msg.startsWith("Type error") && !msg.startsWith("Module not found")) {
      issues.push({
        severity: "CRITICAL",
        category: "build",
        file: "build",
        line: null,
        column: null,
        code: "BUILD_ERROR",
        message: msg,
        autoFix: null,
      });
    }
  }

  return issues;
}

// ── Suggestion Generator ───────────────────────────────────────────────────
function generateSuggestions(issues: TriageIssue[]): TriageSuggestion[] {
  const suggestions: TriageSuggestion[] = [];

  const autoFixable = issues.filter((i) => i.autoFix !== null);
  if (autoFixable.length > 0) {
    suggestions.push({
      action: `Run pnpm lint:fix to auto-fix ${autoFixable.length} ESLint issue(s)`,
      count: autoFixable.length,
    });
  }

  const tsErrors = issues.filter((i) => i.category === "typescript");
  if (tsErrors.length > 0) {
    // Group by file
    const fileMap = new Map<string, number>();
    for (const issue of tsErrors) {
      fileMap.set(issue.file, (fileMap.get(issue.file) || 0) + 1);
    }
    for (const [file, count] of fileMap) {
      suggestions.push({
        action: `Fix ${count} TypeScript error(s) in ${file}`,
        count,
      });
    }
  }

  const testFailures = issues.filter((i) => i.category === "test");
  if (testFailures.length > 0) {
    suggestions.push({
      action: `Fix ${testFailures.length} failing test(s) — run pnpm test to reproduce`,
      count: testFailures.length,
    });
  }

  const buildErrors = issues.filter((i) => i.category === "build");
  if (buildErrors.length > 0) {
    suggestions.push({
      action: `Fix ${buildErrors.length} build error(s) — run pnpm build to reproduce`,
      count: buildErrors.length,
    });
  }

  return suggestions;
}

// ── Main ───────────────────────────────────────────────────────────────────
function main(): void {
  console.log(`\n${C.BOLD}${C.CYAN}Quality Gate Triage${C.RESET}`);
  console.log(`${C.GRAY}${"─".repeat(50)}${C.RESET}\n`);

  const allIssues: TriageIssue[] = [];
  const reportFiles = [
    { file: "type-check.txt", parser: parseTypeScriptErrors, label: "TypeScript" },
    { file: "lint-strict.txt", parser: parseEslintIssues, label: "ESLint" },
    { file: "test-report.txt", parser: parseTestFailures, label: "Tests" },
    { file: "build-report.txt", parser: parseBuildErrors, label: "Build" },
  ];

  for (const { file, parser, label } of reportFiles) {
    const content = readReport(file);
    if (content === null) {
      console.log(`  ${C.GRAY}⊘ ${label}: ${file} not found (skipped)${C.RESET}`);
      continue;
    }
    const issues = parser(content);
    allIssues.push(...issues);
    if (issues.length > 0) {
      console.log(`  ${C.YELLOW}▸ ${label}: ${issues.length} issue(s) found${C.RESET}`);
    } else {
      console.log(`  ${C.GREEN}✓ ${label}: clean${C.RESET}`);
    }
  }

  // Compute summary
  const critical = allIssues.filter((i) => i.severity === "CRITICAL").length;
  const high = allIssues.filter((i) => i.severity === "HIGH").length;
  const medium = allIssues.filter((i) => i.severity === "MEDIUM").length;
  const low = allIssues.filter((i) => i.severity === "LOW").length;
  const autoFixable = allIssues.filter((i) => i.autoFix !== null).length;

  // Top affected files
  const fileCount = new Map<string, number>();
  for (const issue of allIssues) {
    fileCount.set(issue.file, (fileCount.get(issue.file) || 0) + 1);
  }
  const topFiles = [...fileCount.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([f]) => f);

  const suggestions = generateSuggestions(allIssues);

  const report: TriageReport = {
    timestamp: new Date().toISOString(),
    summary: {
      critical,
      high,
      medium,
      low,
      total: allIssues.length,
      topFiles,
      autoFixable,
    },
    issues: allIssues,
    suggestions,
  };

  // Write JSON
  const outPath = resolve(process.cwd(), "quality-gate-triage.json");
  writeFileSync(outPath, JSON.stringify(report, null, 2), "utf-8");

  // Console summary
  console.log(`\n${C.BOLD}Severity Breakdown${C.RESET}`);
  console.log(`${C.GRAY}${"─".repeat(35)}${C.RESET}`);
  if (critical > 0) console.log(`  ${C.RED}${C.BOLD}CRITICAL${C.RESET}  ${critical}`);
  if (high > 0) console.log(`  ${C.YELLOW}${C.BOLD}HIGH${C.RESET}      ${high}`);
  if (medium > 0) console.log(`  ${C.CYAN}MEDIUM${C.RESET}    ${medium}`);
  if (low > 0) console.log(`  ${C.GRAY}LOW${C.RESET}       ${low}`);
  console.log(`  ${C.BOLD}Total${C.RESET}     ${allIssues.length}`);
  if (autoFixable > 0) console.log(`  ${C.GREEN}Auto-fixable${C.RESET}  ${autoFixable}`);

  if (topFiles.length > 0) {
    console.log(`\n${C.BOLD}Top Affected Files${C.RESET}`);
    console.log(`${C.GRAY}${"─".repeat(35)}${C.RESET}`);
    for (const file of topFiles) {
      const count = fileCount.get(file) || 0;
      console.log(`  ${C.GRAY}${count}×${C.RESET} ${file}`);
    }
  }

  if (suggestions.length > 0) {
    console.log(`\n${C.BOLD}Suggestions${C.RESET}`);
    console.log(`${C.GRAY}${"─".repeat(35)}${C.RESET}`);
    for (const s of suggestions) {
      console.log(`  ${C.MAGENTA}→${C.RESET} ${s.action}`);
    }
  }

  console.log(`\n${C.GRAY}→ Triage written to quality-gate-triage.json${C.RESET}\n`);

  // Exit code: 1 if any CRITICAL or HIGH
  if (critical > 0 || high > 0) {
    console.log(`${C.RED}${C.BOLD}✗ ${critical + high} blocking issue(s) found${C.RESET}\n`);
    process.exit(1);
  } else {
    console.log(`${C.GREEN}${C.BOLD}✓ No blocking issues${C.RESET}\n`);
    process.exit(0);
  }
}

main();
