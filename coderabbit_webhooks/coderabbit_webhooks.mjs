/**
 * CodeRabbit Webhook Endpoints
 * Express server wrapping CodeRabbit CLI functionality via HTTP webhooks
 */

import { exec } from "node:child_process";
import express from "express";
import cors from "cors";

const app = express();
app.use(express.json());
app.use(cors());

const PORT = process.env.CODERRABBIT_WEBHOOK_PORT || 3456;
const CR_BIN = process.env.CODERRABBIT_BIN || "C:/Users/Alexa/.local/bin/coderabbit";

// Middleware to validate webhook signatures
function validateWebhook(req, res, next) {
  const signature = req.headers["x-coderabbit-signature"];
  if (!signature) {
    return res.status(401).json({ error: "Missing webhook signature" });
  }
  next();
}

// Webhook: Trigger a CodeRabbit review on a push event
app.post("/webhooks/coderabbit/review", validateWebhook, (req, res) => {
  const { repository, ref, pull_request } = req.body;

  if (!repository) {
    return res.status(400).json({ error: "Missing repository field" });
  }

  const cwd = pull_request?.base?.repo?.clone_url
    ? `/tmp/${pull_request.base.repo.name}`
    : process.cwd();

  const mode = pull_request ? "interactive" : "plain";
  const type = pull_request ? "all" : "uncommitted";

  exec(
    `"${CR_BIN}" review --mode ${mode} --type ${type} --cwd "${cwd}"`,
    { cwd },
    (error, stdout, stderr) => {
      if (error) {
        return res.status(500).json({
          error: "Review failed",
          details: stderr || error.message
        });
      }
      res.json({
        status: "review_complete",
        repository,
        ref: ref || "HEAD",
        output: stdout,
        review_type: type
      });
    }
  );
});

// Webhook: Trigger a CodeRabbit review on a PR event
app.post("/webhooks/coderabbit/pr", validateWebhook, (req, res) => {
  const { action, pull_request, repository } = req.body;

  if (action !== "opened" && action !== "synchronize") {
    return res.json({ status: "skipped", reason: `Action ${action} not reviewed` });
  }

  const prNumber = pull_request?.number;
  const repo = repository?.full_name;

  exec(
    `"${CR_BIN}" review --mode interactive --type all --base ${pull_request.base.ref}`,
    { cwd: process.cwd() },
    (error, stdout, stderr) => {
      if (error) {
        return res.status(500).json({
          error: `PR review failed for #${prNumber}`,
          details: stderr || error.message
        });
      }
      res.json({
        status: "pr_review_complete",
        repository: repo,
        pull_request_number: prNumber,
        output: stdout
      });
    }
  );
});

// Webhook: Check CodeRabbit auth status
app.get("/webhooks/coderabbit/auth/status", (req, res) => {
  exec(`"${CR_BIN}" doctor`, (error, stdout, stderr) => {
    if (error) {
      return res.json({ authenticated: false, details: stderr || error.message });
    }
    res.json({ authenticated: true, details: stdout });
  });
});

// Webhook: Bootstrap CodeRabbit CLI if missing
app.post("/webhooks/coderabbit/bootstrap", (req, res) => {
  exec(`"${CR_BIN}" --version`, (error, stdout) => {
    if (error) {
      return res.status(500).json({ error: "CodeRabbit CLI not found", details: error.message });
    }
    res.json({ status: "installed", version: stdout.trim(), path: CR_BIN });
  });
});

app.listen(PORT, () => {
  console.log(`CodeRabbit webhook server running on port ${PORT}`);
  console.log(`Using binary: ${CR_BIN}`);
});

export default app;
