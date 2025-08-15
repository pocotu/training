"""
Test cases for Anagram Check
Problem ID: F057
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import are_anagrams

class TestAnagramCheck(unittest.TestCase):

    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertTrue(are_anagrams("evil", "vile"))
        self.assertTrue(are_anagrams("a", "a"))
        self.assertFalse(are_anagrams("abc", "def"))
        self.assertTrue(are_anagrams("", ""))

if __name__ == '__main__':
    unittest.main(verbosity=2)