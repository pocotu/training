"""
Test cases for Count Vowels
Problem ID: F025
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
