"""
Test cases for String Concatenation
Problem ID: F004
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import concatenate_strings

class TestStringConcatenation(unittest.TestCase):

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate_strings("abc", "def"), "abcdef")

if __name__ == '__main__':
    unittest.main(verbosity=2)
