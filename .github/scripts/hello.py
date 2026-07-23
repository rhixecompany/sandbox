import asyncio
import sys
import datetime


async def main():
    print("Hello, Python!")
    print("Python version:", sys.version.split()[0])
    print("Time:", datetime.datetime.now().isoformat())


if __name__ == "__main__":
    asyncio.run(main())
