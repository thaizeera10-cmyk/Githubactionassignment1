import unittest
from greeter.greet import greet


class TestGreet(unittest.TestCase):

    def test_valid_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
