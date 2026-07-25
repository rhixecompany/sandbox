#!/usr/bin/env python3
"""
Crypto Wallet API Test Script
Quick sandbox test for wallet provider integration.
"""

import asyncio
import os
import sys

# Example for CryptoAPIs
async def test_cryptoapis():
    """Test CryptoAPIs wallet operations."""
    api_key = os.getenv("CRYPTOAPIS_KEY", "your_api_key_here")
    if api_key == "your_api_key_here":
        print("⚠️  Set CRYPTOAPIS_KEY environment variable")
        return
    
    import httpx
    
    base_url = "https://api.cryptoapis.io/v2"
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    
    async with httpx.AsyncClient() as client:
        # Test create wallet
        response = await client.post(
            f"{base_url}/wallet-as-a-service/wallets",
            headers=headers,
            json={"blockchain": "bitcoin", "network": "testnet", "name": "test-wallet"}
        )
        print(f"Create wallet: {response.status_code}")
        if response.status_code == 200:
            wallet = response.json()
            print(f"  Wallet ID: {wallet.get('data', {}).get('item', {}).get('walletId')}")
            return wallet['data']['item']['walletId']
    return None

# Example for Cobo
async def test_cobo():
    """Test Cobo WaaS wallet operations."""
    api_key = os.getenv("COBO_API_KEY", "your_api_key_here")
    if api_key == "your_api_key_here":
        print("⚠️  Set COBO_API_KEY environment variable")
        return
    
    import httpx
    
    base_url = "https://api.cobo.com/v2"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/wallets",
            headers=headers,
            json={"chain": "ETH", "name": "test-wallet"}
        )
        print(f"Create wallet: {response.status_code}")
        if response.status_code == 200:
            wallet = response.json()
            print(f"  Wallet ID: {wallet.get('data', {}).get('wallet_id')}")
            return wallet['data']['wallet_id']
    return None

async def main():
    print("Testing Wallet APIs...")
    print("=" * 40)
    
    # Test available providers
    await test_cryptoapis()
    await test_cobo()
    
    print("=" * 40)
    print("Done! Configure API keys to run actual tests.")

if __name__ == "__main__":
    asyncio.run(main())