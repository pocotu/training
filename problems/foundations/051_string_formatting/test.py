"""
Test cases for String Formatting
Problem ID: F051
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import format_person_info

class TestStringFormatting(unittest.TestCase):

    def test_format_person_info(self):
        result = format_person_info("Alice", 25, "New York")
        expected = "My name is Alice, I am 25 years old, and I live in New York."
        self.assertEqual(result, expected)
        
        result = format_person_info("Bob", 30, "London")
        expected = "My name is Bob, I am 30 years old, and I live in London."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)