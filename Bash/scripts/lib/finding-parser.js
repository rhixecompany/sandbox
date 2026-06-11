#!/usr/bin/env node

/**
 * Finding Parser: Convert diagnostic output into Finding objects
 */

class FindingParser {
  constructor() {
    this.findings = [];
    this.findingId = 0;
  }

  /**
   * Parse npm audit JSON output
   */
  parseNpmAudit(auditJson, repoId) {
    if (!auditJson || !auditJson.vulnerabilities) {
      return [];
    }

    const findings = [];
    for (const [pkgName, vulnData] of Object.entries(
      auditJson.vulnerabilities,
    )) {
      if (vulnData.via && Array.isArray(vulnData.via)) {
        for (const vuln of vulnData.via) {
          if (typeof vuln === "object") {
            findings.push({
              id: `${repoId}-npm-audit-${++this.findingId}`,
              repoId,
              type: "security",
              severity: vuln.severity || "unknown",
              package: pkgName,
              vulnerability: vuln.title || vuln.cve || "Unknown vulnerability",
              currentVersion: vulnData.installed,
              fixedVersion: vulnData.fixed,
              rootCause: `Vulnerable dependency: ${pkgName}@${vulnData.installed}`,
              proposedFix: `Update ${pkgName} to version ${vulnData.fixed || "latest"}`,
              complexity: "low",
              risk: "medium",
              userImpact: "Security vulnerability in production",
            });
          }
        }
      }
    }
    return findings;
  }

  /**
   * Parse npm outdated output
   */
  parseNpmOutdated(outdatedRaw, repoId) {
    if (!outdatedRaw) return [];

    const findings = [];
    const lines = outdatedRaw.split("\n").slice(1); // Skip header

    for (const line of lines) {
      if (!line.trim()) continue;

      const parts = line.split(/\s+/);
      if (parts.length >= 4) {
        const [pkg, current, wanted, latest] = parts;
        findings.push({
          id: `${repoId}-outdated-${++this.findingId}`,
          repoId,
          type: "dependency",
          severity: "low",
          package: pkg,
          currentVersion: current,
          wantedVersion: wanted,
          latestVersion: latest,
          rootCause: `Package ${pkg} is outdated`,
          proposedFix: `Update ${pkg} from ${current} to ${latest}`,
          complexity: "low",
          risk: "low",
          userImpact: "Potential compatibility issues, missing features",
        });
      }
    }
    return findings;
  }

  /**
   * Parse linter output (generic)
   */
  parseLinterOutput(linterRaw, repoId, linterType = "eslint") {
    if (!linterRaw) return [];

    const findings = [];
    const lines = linterRaw.split("\n");
    let currentFile = null;

    for (const line of lines) {
      if (line.includes("error") || line.includes("warning")) {
        findings.push({
          id: `${repoId}-${linterType}-${++this.findingId}`,
          repoId,
          type: "code-quality",
          severity: line.includes("error") ? "high" : "medium",
          file: currentFile || "unknown",
          issue: line.trim(),
          rootCause: `Code style/quality violation`,
          proposedFix: `Fix ${linterType} violations`,
          complexity: "medium",
          risk: "low",
          userImpact: "Code maintainability",
        });
      } else if (line.includes(".js") || line.includes(".ts")) {
        currentFile = line.split(":")[0];
      }
    }
    return findings;
  }

  /**
   * Parse test failures
   */
  parseTestOutput(testRaw, repoId) {
    if (!testRaw || testRaw.includes("PASS")) return [];

    const findings = [];
    const failureMatch = testRaw.match(/(\d+) failed/);

    if (failureMatch) {
      findings.push({
        id: `${repoId}-test-${++this.findingId}`,
        repoId,
        type: "test",
        severity: "high",
        failureCount: parseInt(failureMatch[1]),
        rootCause: `${failureMatch[1]} test(s) failing`,
        proposedFix: `Fix failing tests`,
        complexity: "high",
        risk: "high",
        userImpact: "Code reliability compromised",
      });
    }
    return findings;
  }

  /**
   * Parse build errors
   */
  parseBuildOutput(buildRaw, repoId) {
    if (!buildRaw || buildRaw.includes("successfully")) return [];

    const findings = [];
    if (buildRaw.includes("error") || buildRaw.includes("Error")) {
      findings.push({
        id: `${repoId}-build-${++this.findingId}`,
        repoId,
        type: "build",
        severity: "critical",
        rootCause: `Build process failing`,
        proposedFix: `Fix build errors`,
        complexity: "high",
        risk: "critical",
        userImpact: "Cannot deploy or release",
      });
    }
    return findings;
  }

  /**
   * Parse all diagnostics from a scan result
   */
  parseAllDiagnostics(scanResult, repoId) {
    const allFindings = [];
    const diagnostics = scanResult.diagnostics || {};

    // Parse npm audit
    if (diagnostics["npm-audit"] && diagnostics["npm-audit"].vulnerabilities) {
      allFindings.push(...this.parseNpmAudit(diagnostics["npm-audit"], repoId));
    }

    // Parse npm outdated
    if (diagnostics["npm-outdated"] && diagnostics["npm-outdated"].raw) {
      allFindings.push(
        ...this.parseNpmOutdated(diagnostics["npm-outdated"].raw, repoId),
      );
    }

    // Parse linter
    if (diagnostics["npm-lint"] && diagnostics["npm-lint"].raw) {
      allFindings.push(
        ...this.parseLinterOutput(
          diagnostics["npm-lint"].raw,
          repoId,
          "eslint",
        ),
      );
    }

    // Parse tests
    if (diagnostics["npm-test"] && diagnostics["npm-test"].raw) {
      allFindings.push(
        ...this.parseTestOutput(diagnostics["npm-test"].raw, repoId),
      );
    }

    // Parse build
    if (diagnostics["npm-build"] && diagnostics["npm-build"].raw) {
      allFindings.push(
        ...this.parseBuildOutput(diagnostics["npm-build"].raw, repoId),
      );
    }

    return allFindings;
  }
}

module.exports = FindingParser;
