#!/usr/bin/env python3
"""
PayPal Webhook Test Script
Tests webhook verification and handling.
"""

import json
import hmac
import hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import threading
import time
import os

# Webhook verification
def verify_webhook(payload: bytes, signature: str, webhook_id: str) -> bool:
    """Verify PayPal webhook signature."""
    expected = hmac.new(
        webhook_id.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(content_length)
        
        signature = self.headers.get('PayPal-Transmission-Sig', '')
        webhook_id = os.getenv('PAYPAL_WEBHOOK_ID', 'test_webhook_id')
        
        if verify_webhook(payload, signature, webhook_id):
            print("✅ Webhook signature verified")
            event = json.loads(payload)
            print(f"   Event: {event.get('event_type')}")
            print(f"   Resource: {event.get('resource', {}).get('id')}")
            self.send_response(200)
            self.end_headers()
        else:
            print("❌ Webhook signature verification failed")
            self.send_response(400)
            self.end_headers()

def run_test_server():
    """Run a simple test webhook server."""
    server = HTTPServer(('localhost', 8080), WebhookHandler)
    print("🌐 Webhook server running on http://localhost:8080")
    print("   Configure PayPal webhook URL to: http://localhost:8080")
    print("   Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        server.shutdown()

def test_webhook_verification():
    """Test webhook verification logic."""
    print("🧪 Testing webhook verification...")
    
    # Test payload
    payload = json.dumps({
        "id": "WH-123456789",
        "event_type": "CHECKOUT.ORDER.APPROVED",
        "resource": {
            "id": "5O190127TN364715T",
            "status": "APPROVED"
        }
    }).encode()
    
    webhook_id = "test_webhook_id"
    signature = hmac.new(
        webhook_id.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    if verify_webhook(payload, signature, webhook_id):
        print("✅ Verification test passed")
    else:
        print("❌ Verification test failed")

if __name__ == "__main__":
    test_webhook_verification()
    print("\n" + "=" * 50)
    print("To test with real PayPal webhooks:")
    print("1. Set PAYPAL_WEBHOOK_ID environment variable")
    print("2. Run: python paypal-test-webhook.py server")
    print("3. Use ngrok to expose localhost:8080")
    print("4. Configure PayPal webhook to ngrok URL")
    
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        run_test_server()