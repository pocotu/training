"""
Test cases for Valid Palindrome
Problem ID: 040
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_palindrome

class TestValidPalindrome(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(" "))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main(verbosity=2)