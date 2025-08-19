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
        """Test basic vowel counting"""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)
    
    def test_count_vowels_mixed_case(self):
        """Test with mixed case"""
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("PyThOn"), 1)
    
    def test_count_vowels_special_cases(self):
        """Test with special characters and empty string"""
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("123!@#"), 0)
        self.assertEqual(count_vowels("a1e2i3o4u5"), 5)
    
    def test_count_vowels_repeated(self):
        """Test with repeated vowels"""
        self.assertEqual(count_vowels("aaa"), 3)
        self.assertEqual(count_vowels("beautiful"), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
