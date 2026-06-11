#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

/**
 * Repo Scanner: Auto-detect stack and run diagnostics
 */

class RepoScanner {
  constructor(repoPath, diagnosticsConfig) {
    this.repoPath = repoPath;
    this.diagnosticsConfig = diagnosticsConfig;
    this.stack = null;
    this.findings = [];
  }

  /**
   * Detect stack type based on presence of key files
   */
  detectStack() {
    const stacks = this.diagnosticsConfig.stacks;

    for (const [stackName, stackConfig] of Object.entries(stacks)) {
      if (stackName === "unknown") continue;

      const allFilesPresent = stackConfig.detectionFiles.every((file) => {
        return fs.existsSync(path.join(this.repoPath, file));
      });

      if (allFilesPresent) {
        this.stack = stackName;
        return stackName;
      }
    }

    this.stack = "unknown";
    return "unknown";
  }

  /**
   * Run diagnostics for detected stack
   */
  runDiagnostics() {
    const stackConfig = this.diagnosticsConfig.stacks[this.stack];
    const results = {
      stack: this.stack,
      diagnostics: {},
    };

    for (const diagnostic of stackConfig.diagnostics) {
      try {
        const output = execSync(diagnostic.command, {
          cwd: this.repoPath,
          encoding: "utf-8",
          stdio: ["pipe", "pipe", "pipe"],
        });

        if (diagnostic.parseJson) {
          try {
            results.diagnostics[diagnostic.name] = JSON.parse(output);
          } catch (e) {
            results.diagnostics[diagnostic.name] = {
              raw: output,
              parseError: true,
            };
          }
        } else {
          results.diagnostics[diagnostic.name] = { raw: output };
        }
      } catch (error) {
        results.diagnostics[diagnostic.name] = {
          error: error.message,
          exitCode: error.status,
        };
      }
    }

    return results;
  }

  /**
   * Scan repo: detect stack and run diagnostics
   */
  scan() {
    this.detectStack();
    const diagnostics = this.runDiagnostics();
    return {
      repoPath: this.repoPath,
      stack: this.stack,
      diagnostics: diagnostics.diagnostics,
    };
  }
}

module.exports = RepoScanner;
