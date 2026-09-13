#!/usr/bin/env python3
"""Test payload script for webhook adapter routes.
Usage: python scripts/webhook_test_payload.py <route> [--payload '{"key":"val"}']
Produces a JSON payload matching the route event type, intended for:
  hermes webhook test <route> --payload '{"issue":{"number":42,"title":"Test"}}'
Verified against docs (dynamic subscriptions / test section).
"""
import argparse, json, sys

def build_payload(route: str) -> dict:
    if route == "github-issues":
        return {"issue": {"number": 42, "title": "Test webhook", "user": {"login": "test-user"}, "body": "Reproduce steps..."}, "action": "opened"}
    elif route == "deploy-notify":
        return {"repository": {"full_name": "rhixecompany/sandbox"}, "ref": "refs/heads/main", "head_commit": {"message": "chore: webhook test"}}
    elif route == "oom-emergency":
        return {"event_type": "monitor", "detail": "memory usage > 92%", "payload": {"service": "gateway"}}
    else:
        return {"message": f"Generic payload for route '{route}'", "route": route}

def main():
    parser = argparse.ArgumentParser(description="Generate webhook test payload")
    parser.add_argument("route", default="github-issues")
    parser.add_argument("--payload", default=None, help="Custom JSON payload (optional)")
    args = parser.parse_args()
    if args.payload:
        payload = json.loads(args.payload)
    else:
        payload = build_payload(args.route)
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
