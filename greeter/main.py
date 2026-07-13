import argparse
import sys
from greeter.greet import greet, Greeter

def main():
    """Main entry point for the greeter CLI tool."""
    parser = argparse.ArgumentParser(
        description="Greeter: A friendly CLI greeting utility."
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="The name of the person to greet (default: World)"
    )
    parser.add_argument(
        "-t", "--template",
        default="Hello, {name}!",
        help="Custom greeting template. Must include '{name}' (default: 'Hello, {name}!')"
    )

    args = parser.parse_args()

    try:
        greeter = Greeter(args.template)
        message = greeter.greet(args.name)
        print(message)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
