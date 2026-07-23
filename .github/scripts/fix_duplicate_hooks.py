#!/usr/bin/env python3
"""Fix duplicate hooks_auto_accept line in config.yaml."""
import asyncio

config_path = r'C:\Users\Alexa\AppData\Local\hermes\config.yaml'


async def main():
    with open(config_path, 'r') as f:
        lines = f.readlines()

    # Remove duplicate hooks_auto_accept lines
    new_lines = []
    seen_hooks_auto_accept = False
    for line in lines:
        stripped = line.strip()
        if stripped == 'hooks_auto_accept: true':
            if not seen_hooks_auto_accept:
                new_lines.append(line)
                seen_hooks_auto_accept = True
            # skip duplicate
        else:
            new_lines.append(line)

    with open(config_path, 'w') as f:
        f.writelines(new_lines)

    print("Fixed duplicate hooks_auto_accept line")


if __name__ == "__main__":
    asyncio.run(main())
