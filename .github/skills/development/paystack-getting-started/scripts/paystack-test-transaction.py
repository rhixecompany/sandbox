#!/usr/bin/env python3
"""
Paystack Sandbox Test Script
Tests basic integration flow in sandbox environment.
"""

import asyncio
import httpx
import os

# Load from environment or config
SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "sk_test_your_key_here")
BASE_URL = "https://api.paystack.co"

async def test_initialize_transaction():
    """Test transaction initialization."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/transaction/initialize",
            headers={
                "Authorization": f"Bearer {SECRET_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "email": "test@example.com",
                "amount": 10000,  # 100 NGN in kobo
                "reference": "test-ref-123"
            }
        )
        print(f"Initialize: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Authorization URL: {data['data']['authorization_url']}")
            return data['data']['reference']
        return None

async def test_verify_transaction(reference):
    """Test transaction verification."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/transaction/verify/{reference}",
            headers={"Authorization": f"Bearer {SECRET_KEY}"}
        )
        print(f"Verify: {response.status_code}")
        if response.status_code == 200:
            print(f"Status: {response.json()['data']['status']}")

async def main():
    print("Testing Paystack Sandbox...")
    ref = await test_initialize_transaction()
    if ref:
        await test_verify_transaction(ref)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())