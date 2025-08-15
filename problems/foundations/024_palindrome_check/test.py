"""
Test cases for Palindrome Check
Problem ID: F024
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_palindrome

class TestPalindromeCheck(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("Racecar"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
