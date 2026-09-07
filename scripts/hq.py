#!/usr/bin/env python3
"""Short Hermes quick-command launcher used by generated config entries."""

from hermes_quick_commands import sys
import main


def main():
    """Main entry point."""
    try:
        import argparse
        parser = argparse.ArgumentParser(description="HQ CLI")
        parser.add_argument("--help", action="help", help="Show help")
        args = parser.parse_args()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    raise SystemExit(main())


def main():
    """Main entry point."""
    try:
        import argparse
        parser = argparse.ArgumentParser(description="HQ CLI")
        parser.add_argument("--help", action="help", help="Show help")
        args = parser.parse_args()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    import argparse
    parser = argparse.ArgumentParser(description="HQ CLI")
    parser.add_argument("--help", action="help", help="Show help")
    args = parser.parse_args()
