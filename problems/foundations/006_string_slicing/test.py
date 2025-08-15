"""
Test cases for String Slicing
Problem ID: F006
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_substring

class TestStringSlicing(unittest.TestCase):

    def test_get_substring(self):
        self.assertEqual(get_substring("Hello, World!", 7, 12), "World")
        self.assertEqual(get_substring("abcdef", 1, 4), "bcd")

if __name__ == '__main__':
    unittest.main(verbosity=2)
