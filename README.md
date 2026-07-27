# Greeter

A friendly, customizable greeting package and command-line tool.

## Installation

You can install the package locally using pip:

```bash
pip install .
```

Or for development (editable mode):

```bash
pip install -e .
```

## Usage

### In Python

```python
from greeter import greet, Greeter

# Simple usage
print(greet("Alice"))  # Hello, Alice!

# Custom templates
greeter = Greeter("Welcome aboard, {name}!")
print(greeter.greet("Bob"))  # Welcome aboard, Bob!
```

### Command Line Interface (CLI)

You can run the greeter directly with Python:

```bash
python -m greeter --help
```

Or once installed via pip, use the `greeter` command:

```bash
greeter Alice
# Output: Hello, Alice!

greeter --template "Good morning, {name}!" Bob
# Output: Good morning, Bob!
```

## Running Tests

Run the unit test suite using Python's built-in `unittest` module:

```bash
python -m unittest discover -s tests
```
## Pull Requests and Continuous Integration

This project uses GitHub Actions to automatically run linting and unit tests whenever code is pushed to the `main` branch or when a pull request targeting the `main` branch is created or updated.

### Creating a Pull Request

1. Create a new branch:

```bash
git checkout -b feature-name
## CI Verification

This change was created to verify that GitHub Actions runs on pull requests.
