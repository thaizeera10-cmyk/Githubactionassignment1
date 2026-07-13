import unittest
from greeter.greet import greet, Greeter

class TestGreeter(unittest.TestCase):

    def test_default_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_with_name(self):
        self.assertEqual(greet("John"), "Hello, John!")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet("   "), "Hello, World!")

    def test_custom_template(self):
        self.assertEqual(greet("John", "Welcome, {name}!"), "Welcome, John!")

    def test_invalid_template(self):
        with self.assertRaises(ValueError):
            Greeter("Hello World")

    def test_class_instantiation(self):
        greeter = Greeter("Good morning, {name}!")
        self.assertEqual(greeter.greet("Alice"), "Good morning, Alice!")


if __name__ == "__main__":
    unittest.main()
