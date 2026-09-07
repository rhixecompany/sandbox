#!/usr/bin/env bash
# CodeRabbit Webhook Handler
# Processes incoming webhooks from GitHub and triggers CodeRabbit reviews
# 
# Endpoints:
#   POST /webhooks/code-rabbit/review   - Trigger review
#   POST /webhooks/code-rabbit/sync     - Re-review on commit
#   POST /webhooks/code-rabbit/opened   - Initial review on PR open
#
# Requires: GITHUB_PAT, CODE_RABBIT_WEBHOOK_SECRET

set -euo pipefail

WEBHOOK_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$WEBHOOK_DIR/webhook.log"

# Configuration
GITHUB_PAT="${GITHUB_PAT:-}"
WEBHOOK_SECRET="${CODE_RABBIT_WEBHOOK_SECRET:-}"
CODERABBIT_BIN="${CODERABBIT_BIN:-coderabbit}"
PORT="${PORT:-8080}"

# Ensure GITHUB_PAT is set
if [ -z "$GITHUB_PAT" ]; then
    echo "ERROR: GITHUB_PAT environment variable is required" | tee -a "$LOG_FILE"
    exit 1
fi

log() {
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] $*" | tee -a "$LOG_FILE"
}

verify_signature() {
    local payload="$1"
    local signature="$2"
    # Verify webhook signature using HMAC-SHA256
    # This is a placeholder - implement actual signature verification
    if [ -z "$WEBHOOK_SECRET" ]; then
        log "WARNING: No webhook secret configured, skipping verification"
        return 0
    fi
    log "Verifying webhook signature..."
    return 0
}

handle_review() {
    local payload="$1"
    log "Handling review webhook: $payload"
    
    # Extract PR info from payload
    local pr_number
    pr_number=$(echo "$payload" | grep -oP '"number":\s*\K\d+' || echo "unknown")
    local repo_name
    repo_name=$(echo "$payload" | grep -oP '"name":\s*"\K[^"]+' || echo "unknown")
    
    log "Running CodeRabbit review for PR #$pr_number in $repo_name"
    
    # Trigger CodeRabbit review
    if [ "$CODERABBIT_BIN" = "coderabbit" ]; then
        coderabbit review --agent 2>&1 | tee -a "$LOG_FILE"
    else
        "$CODERABBIT_BIN" review --agent 2>&1 | tee -a "$LOG_FILE"
    fi
    
    log "Review completed for PR #$pr_number"
}

handle_sync() {
    local payload="$1"
    log "Handling sync webhook: $payload"
    
    # Re-run review for new commits
    handle_review "$payload"
}

handle_opened() {
    local payload="$1"
    log "Handling opened webhook: $payload"
    
    # Initial review
    handle_review "$payload"
}

# Simple HTTP server using Python
python3 -c "
import http.server
import json
import subprocess
import os
import hmac
import hashlib

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        # Verify signature
        signature = self.headers.get('X-Hub-Signature-256', '')
        secret = os.environ.get('CODE_RABBIT_WEBHOOK_SECRET', '')
        
        if secret and signature:
            expected = hmac.new(secret.encode(), post_data, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(f'sha256={expected}', signature):
                self.send_response(401)
                self.end_headers()
                return
        
        payload = json.loads(post_data)
        path = self.path
        
        if '/review' in path:
            self.handle_review(payload)
        elif '/sync' in path:
            self.handle_sync(payload)
        elif '/opened' in path:
            self.handle_opened(payload)
        else:
            self.send_response(404)
            self.end_headers()
            return
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'ok'}).encode())
    
    def handle_review(self, payload):
        pr = payload.get('pull_request', {})
        number = pr.get('number', 'unknown')
        repo = payload.get('repository', {}).get('full_name', 'unknown')
        print(f'[WEBHOOK] Running review for PR #{number} in {repo}')
        os.system('coderabbit review --agent')
    
    def handle_sync(self, payload):
        self.handle_review(payload)
    
    def handle_opened(self, payload):
        self.handle_review(payload)
    
    def log_message(self, format, *args):
        pass  # Suppress default logging

server = http.server.HTTPServer(('localhost', int(os.environ.get('PORT', 8080))), WebhookHandler)
print(f'[WEBHOOK] CodeRabbit webhook server running on port {os.environ.get(\"PORT\", 8080)}')
server.serve_forever()
" &

log "CodeRabbit webhook handler started on port $PORT"
