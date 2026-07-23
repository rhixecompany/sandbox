#!/usr/bin/env python3
"""Dev init code samples — scaffold code samples and example projects from templates.

Usage:
    python dev-init-code-samples.py [--template TYPE] [--output PATH] [--name NAME]
                                    [--language python|js|ts|rust] [--dry-run]
"""

import asyncio
import argparse
import sys
from pathlib import Path


SAMPLE_TEMPLATES = {
    "hello-world": {
        "python": {
            "main.py": "#!/usr/bin/env python3\n\"\"\"Hello World sample.\"\"\"\n\n\ndef main():\n    print(\"Hello, World!\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
        },
        "js": {
            "index.js": "/** Hello World sample. */\nfunction main() {\n    console.log(\"Hello, World!\");\n}\n\nmain();\n",
        },
        "ts": {
            "index.ts": "/** Hello World sample. */\nfunction main(): void {\n    console.log(\"Hello, World!\");\n}\n\nmain();\n",
        },
        "rust": {
            "main.rs": "/// Hello World sample.\nfn main() {\n    println!(\"Hello, World!\");\n}\n",
        },
    },
    "cli-app": {
        "python": {
            "cli.py": "#!/usr/bin/env python3\n\"\"\"CLI application sample.\"\"\"\n\nimport argparse\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Sample CLI app\")\n    parser.add_argument(\"--name\", default=\"World\", help=\"Name to greet\")\n    args = parser.parse_args()\n    print(f\"Hello, {args.name}!\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
            "README.md": "# CLI App Sample\n\nA sample command-line application.\n\n## Usage\n\n```bash\npython cli.py --name Alice\n```\n",
        },
        "js": {
            "cli.js": "#!/usr/bin/env node\n/** CLI application sample. */\nconst name = process.argv[2] || 'World';\nconsole.log(`Hello, ${name}!`);\n",
        },
    },
    "async-worker": {
        "python": {
            "worker.py": "#!/usr/bin/env python3\n\"\"\"Async worker sample.\"\"\"\n\nimport asyncio\n\n\nasync def process_item(item: str) -> str:\n    \"\"\"Process a single item.\"\"\"\n    await asyncio.sleep(0.1)\n    return f\"Processed: {item}\"\n\n\nasync def main():\n    items = [\"task1\", \"task2\", \"task3\"]\n    results = await asyncio.gather(*[process_item(item) for item in items])\n    for r in results:\n        print(r)\n\n\nif __name__ == \"__main__\":\n    asyncio.run(main())\n",
            "README.md": "# Async Worker Sample\n\nDemonstrates async/await patterns in Python.\n",
        },
    },
    "api-client": {
        "python": {
            "client.py": "#!/usr/bin/env python3\n\"\"\"API client sample.\"\"\"\n\nimport asyncio\nfrom pathlib import Path\n\n\nasync def fetch_data(url: str) -> str:\n    \"\"\"Simulate fetching data from an API.\"\"\"\n    await asyncio.sleep(0.5)\n    return f'{{\"url\": \"{url}\", \"status\": \"ok\"}}'\n\n\nasync def main():\n    urls = [\"https://api.example.com/data1\", \"https://api.example.com/data2\"]\n    tasks = [fetch_data(url) for url in urls]\n    results = await asyncio.gather(*tasks)\n    for r in results:\n        print(r)\n\n\nif __name__ == \"__main__\":\n    asyncio.run(main())\n",
        },
    },
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize development code samples")
    parser.add_argument("--template", choices=list(SAMPLE_TEMPLATES.keys()), default="hello-world",
                        help="Sample template type")
    parser.add_argument("--output", default=None, help="Output directory (default: current dir)")
    parser.add_argument("--name", default=None, help="Project/sample name")
    parser.add_argument("--language", choices=["python", "js", "ts", "rust"], default="python",
                        help="Programming language")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating files")
    return parser.parse_args(argv)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    template = SAMPLE_TEMPLATES.get(args.template, {})
    files = template.get(args.language, {})

    if not files:
        print(f"ERROR: no template for {args.template}/{args.language}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output or Path.cwd())
    if args.name:
        output_dir = output_dir / args.name

    print(f"Initializing '{args.template}' sample ({args.language})")
    print(f"Output: {output_dir}")

    created = 0
    for filename, content in files.items():
        filepath = output_dir / filename
        if args.dry_run:
            print(f"  [DRY-RUN] Would create: {filepath}")
            created += 1
            continue

        await asyncio.to_thread(filepath.parent.mkdir, parents=True, exist_ok=True)
        await asyncio.to_thread(filepath.write_text, content, encoding="utf-8")
        print(f"  [CREATED] {filepath}")
        created += 1

    mode = "would be created" if args.dry_run else "created"
    print(f"\n{created} file(s) {mode}")


if __name__ == "__main__":
    asyncio.run(main())
