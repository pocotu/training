"""
Test cases for Reverse a String
Problem ID: F023
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import reverse_string

class TestReverseAString(unittest.TestCase):

    def test_reverse_string(self):
        """Test basic string reversal"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_string_mixed_case(self):
        """Test with mixed case strings"""
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("HeLLo"), "oLLeH")
    
    def test_reverse_string_special_chars(self):
        """Test with special characters and spaces"""
        self.assertEqual(reverse_string("Hello World!"), "!dlroW olleH")
        self.assertEqual(reverse_string("12345"), "54321")
    
    def test_reverse_string_single_char(self):
        """Test with single character"""
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Z"), "Z")

if __name__ == '__main__':
    unittest.main(verbosity=2)
