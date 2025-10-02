#!/usr/bin/env python3
"""
Treeson - Example usage and demonstration script.

This script demonstrates how to use treeson programmatically and serves as
a quick demonstration of the library's capabilities.
"""

import json
import sys
from pathlib import Path
from treeson.cli import dir_to_json, TreesonConfig, main as cli_main


def demo_programmatic_usage():
    """Demonstrate programmatic usage of treeson."""
    print("=== Treeson Programmatic Usage Demo ===\n")

    # Get current directory structure
    current_dir = Path(".")

    # Basic usage
    print("1. Basic directory structure (current directory):")
    try:
        basic_result = dir_to_json(current_dir)
        print(json.dumps(basic_result, indent=2)[:200] + "..." if len(str(basic_result)) > 200 else json.dumps(basic_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "="*50 + "\n")

    # Custom configuration
    print("2. Custom configuration (max depth 2, include hidden files):")
    try:
        config = TreesonConfig(
            include_hidden=True,
            max_depth=2,
            ignores={"__pycache__", ".git", "*.pyc"}
        )
        custom_result = dir_to_json(current_dir, config)
        print(json.dumps(custom_result, indent=2)[:300] + "..." if len(str(custom_result)) > 300 else json.dumps(custom_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "="*50 + "\n")
    print("For more examples and CLI usage, run: treeson --help")


def main():
    """
    Main entry point for demonstration script.

    If arguments are provided, delegate to the CLI.
    Otherwise, run the demonstration.
    """
    if len(sys.argv) > 1:
        # If arguments provided, use the CLI
        print("Delegating to treeson CLI...\n")
        return cli_main()
    else:
        # No arguments, run demonstration
        demo_programmatic_usage()
        return 0


if __name__ == "__main__":
    sys.exit(main())
