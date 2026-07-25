#!/usr/bin/env python3
"""
Flutterwave Test Transfers Script
Tests transfer API in sandbox mode.
"""

import asyncio
import httpx
import os
import uuid
from datetime import datetime

SECRET_KEY = os.getenv("FLW_SECRET_KEY", "FLWSECK_TEST-your_key")
BASE_URL = "https://api.flutterwave.com/v3"

async def test_validate_account():
    """Test account validation."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/accounts/validate",
            headers={
                "Authorization": f"Bearer {SECRET_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "account_number": "0690000031",
                "account_bank": "044"  # Access Bank
            }
        )
        print(f"Validate account: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: {data.get('status')}")
            print(f"  Account name: {data.get('data', {}).get('account_name')}")
            return True
    return False

async def test_initiate_transfer():
    """Test transfer initiation."""
    idempotency_key = str(uuid.uuid4())
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/transfers",
            headers={
                "Authorization": f"Bearer {SECRET_KEY}",
                "Content-Type": "application/json",
                "Idempotency-Key": idempotency_key
            },
            json={
                "account_bank": "044",
                "account_number": "0690000031",
                "amount": 100,
                "currency": "NGN",
                "reference": f"tx_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "narration": "Test transfer"
            }
        )
        print(f"Initiate transfer: {response.status_code}")
        if response.status_code in (200, 201, 202):
            data = response.json()
            print(f"  Status: {data.get('status')}")
            print(f"  ID: {data.get('data', {}).get('id')}")

async def main():
    print("Testing Flutterwave Transfers API...")
    print("=" * 40)
    await test_validate_account()
    await test_initiate_transfer()
    print("=" * 40)
    print("Done! Set FLW_SECRET_KEY env var for real testing.")

if __name__ == "__main__":
    asyncio.run(main())