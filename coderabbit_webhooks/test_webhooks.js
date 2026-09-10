import http from "node:http";

const BASE = "http://localhost:3456";

function post(path, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = http.request(`${BASE}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Content-Length": data.length,
        "x-coderabbit-signature": "test-signature"
      }
    }, (res) => {
      let resp = "";
      res.on("data", (chunk) => (resp += chunk));
      res.on("end", () => resolve({ status: res.statusCode, body: resp }));
    });
    req.on("error", reject);
    req.write(data);
    req.end();
  });
}

async function runTests() {
  console.log("=== CodeRabbit Webhook Tests ===\n");

  // Test 1: Auth status
  console.log("1. GET /webhooks/coderabbit/auth/status");
  try {
    const req = http.request(`${BASE}/webhooks/coderabbit/auth/status`, (res) => {
      let d = "";
      res.on("data", (c) => (d += c));
      res.on("end", () => console.log(`   Status: ${res.statusCode}, Body: ${d.substring(0, 200)}`));
    });
    req.end();
  } catch (e) {
    console.log(`   ERROR: ${e.message}`);
  }

  // Test 2: Review webhook
  console.log("\n2. POST /webhooks/coderabbit/review");
  try {
    const result = await post("/webhooks/coderabbit/review", {
      repository: "test/repo",
      ref: "main",
      after: "abc123"
    });
    console.log(`   Status: ${result.status}, Body: ${result.body.substring(0, 200)}`);
  } catch (e) {
    console.log(`   ERROR: ${e.message}`);
  }

  // Test 3: PR webhook
  console.log("\n3. POST /webhooks/coderabbit/pr");
  try {
    const result = await post("/webhooks/coderabbit/pr", {
      action: "opened",
      repository: { full_name: "test/repo" },
      pull_request: { number: 1, base: { ref: "main" } }
    });
    console.log(`   Status: ${result.status}, Body: ${result.body.substring(0, 200)}`);
  } catch (e) {
    console.log(`   ERROR: ${e.message}`);
  }

  // Test 4: Bootstrap
  console.log("\n4. POST /webhooks/coderabbit/bootstrap");
  try {
    const result = await post("/webhooks/coderabbit/bootstrap", {});
    console.log(`   Status: ${result.status}, Body: ${result.body.substring(0, 200)}`);
  } catch (e) {
    console.log(`   ERROR: ${e.message}`);
  }

  console.log("\n=== Tests Complete ===");
}

runTests();
