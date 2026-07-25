#!/usr/bin/env python3
"""Polymarket CLI — query markets, prices, and orderbooks."""
import json, sys, urllib.request, urllib.error

API = "https://clob.polymarket.com"

def get_markets(tag: str = None, limit: int = 20) -> list:
    url = f"{API}/markets?limit={limit}"
    if tag:
        url += f"&tag={tag}"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

def get_orderbook(condition_id: str) -> dict:
    url = f"{API}/book?condition_id={condition_id}&side=BUY"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "markets"
    if cmd == "markets":
        tag = sys.argv[2] if len(sys.argv) > 2 else None
        data = get_markets(tag)
        for m in data.get("data", [])[:5]:
            print(f"{m['question']} — ${m.get('price', '?')}")
    elif cmd == "orderbook":
        data = get_orderbook(sys.argv[2])
        print(json.dumps(data, indent=2))
