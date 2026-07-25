#!/usr/bin/env python3
"""
Binance API Test Script
Tests basic Binance Spot API connectivity.
"""

import asyncio
import httpx
import os

async def test_public_endpoints():
    """Test public market data endpoints."""
    base_url = "https://api.binance.com/api/v3"
    
    async with httpx.AsyncClient() as client:
        # Test ticker
        response = await client.get(f"{base_url}/ticker/24hr?symbol=BTCUSDT")
        print(f"Ticker 24hr: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  BTCUSDT: {data['lastPrice']}")
        
        # Test klines
        response = await client.get(f"{base_url}/klines?symbol=BTCUSDT&interval=1h&limit=5")
        print(f"Klines 1h: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  {len(data)} candles retrieved")
        
        # Test order book
        response = await client.get(f"{base_url}/depth?symbol=BTCUSDT&limit=10")
        print(f"Order book: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  Bids: {len(data['bids'])}, Asks: {len(data['asks'])}")

async def test_signed_endpoints():
    """Test signed endpoints (requires API keys)."""
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        print("⚠️  Set BINANCE_API_KEY and BINANCE_API_SECRET for signed endpoint tests")
        return
    
    import hmac
    import hashlib
    import time
    
    base_url = "https://api.binance.com/api/v3"
    
    def sign(params):
        query = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        return hmac.new(api_secret.encode(), query.encode(), hashlib.sha256).hexdigest()
    
    async with httpx.AsyncClient() as client:
        # Test account info
        params = {"timestamp": int(time.time() * 1000)}
        params["signature"] = sign(params)
        
        response = await client.get(
            f"{base_url}/account",
            params=params,
            headers={"X-MBX-APIKEY": api_key}
        )
        print(f"Account info: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  Balances: {len(data['balances'])} assets")

async def main():
    print("Testing Binance API...")
    print("=" * 40)
    
    await test_public_endpoints()
    await test_signed_endpoints()
    
    print("=" * 40)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())