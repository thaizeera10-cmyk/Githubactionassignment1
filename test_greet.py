"""Tests for the greeting functionality."""

import unittest
from greeter.greet import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_valid_name(self):
        """Test that a valid name returns the correct greeting."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_empty_name(self):
        """Test that an empty name returns the default greeting."""
        self.assertEqual(greet(""), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
