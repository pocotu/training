"""
Test cases for Hello, World!
Problem ID: F001
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import hello_world

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        """Test that the function returns 'Hello, World!'"""
        self.assertEqual(hello_world(), "Hello, World!")
    
    def test_hello_world_type(self):
        """Test that the function returns a string"""
        result = hello_world()
        self.assertIsInstance(result, str)
    
    def test_hello_world_exact_match(self):
        """Test exact string match including punctuation"""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
        self.assertTrue(result.endswith("!"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
