#!/usr/bin/env python3
"""
Unit tests for Longest Palindromic Substring (Problem 104)

Tests string manipulation and processing algorithms.
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to sys.path to import solution
sys.path.append(str(Path(__file__).parent))

try:
    from solution import LongestPalindromicSubstring
except ImportError:
    # Fallback if solution file doesn't exist yet
    class LongestPalindromicSubstring:
        def longest_palindromic_substring(self, s):
            raise NotImplementedError("Solution not implemented yet")


class TestLongestPalindromicSubstring(unittest.TestCase):
    """Test cases for Longest Palindromic Substring."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = LongestPalindromicSubstring()
    
    def test_basic_string(self):
        """Test basic string functionality."""
        s = "hello world"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should return a valid result")
    
    def test_empty_string(self):
        """Test edge case with empty string."""
        s = ""
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle empty string")
    
    def test_single_character(self):
        """Test edge case with single character."""
        s = "a"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle single character")
    
    def test_repeated_characters(self):
        """Test string with repeated characters."""
        s = "aaabbbccc"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle repeated characters")
    
    def test_mixed_case(self):
        """Test string with mixed case."""
        s = "Hello World"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle mixed case")
    
    def test_special_characters(self):
        """Test string with special characters."""
        s = "hello, world! 123"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle special characters")
    
    def test_palindrome(self):
        """Test with palindromic string."""
        s = "racecar"
        result = self.solution.longest_palindromic_substring(s)
        self.assertIsNotNone(result, "Should handle palindromes")
    
    def test_long_string(self):
        """Test performance with long string."""
        s = "a" * 10000
        
        import time
        start_time = time.time()
        result = self.solution.longest_palindromic_substring(s)
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 1.0, "Should be efficient")
        self.assertIsNotNone(result, "Should handle long strings")


if __name__ == "__main__":
    unittest.main(verbosity=2)
