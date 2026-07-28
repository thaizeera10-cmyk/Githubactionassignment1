"""Greeting utilities for creating customizable messages."""


class Greeter:
    """A class responsible for generating customizable greetings."""
    # pylint: disable=too-few-public-methods
    def __init__(self, template: str = "Hello, {name}!"):
        """
        Initialize the Greeter with a custom greeting template.
        The template must contain '{name}' placeholder.
        """
        if "{name}" not in template:
            raise ValueError("Template must contain the '{name}' placeholder.")
        self.template = template
# Return a formatted greeting message.
    def greet(self, name: str = "World") -> str:
        """Generate a greeting for the specified name."""
        if not name or not name.strip():
            name = "World"
        return self.template.format(name=name.strip())


def greet(name: str = "World", template: str = "Hello, {name}!") -> str:
    """Convenience function to generate a greeting."""
    return Greeter(template).greet(name)
