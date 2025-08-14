"""
Test cases for Longest Palindromic Substring problem
Problem ID: 106
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import longest_palindrome

class TestLongestPalindrome:
    """Test class for Longest Palindromic Substring problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "babad"
        result = longest_palindrome(s)
        # Either "bab" or "aba" is acceptable
        assert result in ["bab", "aba"]
        assert len(result) == 3
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "cbbd"
        expected = "bb"
        assert longest_palindrome(s) == expected
    
    def test_single_character(self):
        """Test single character"""
        s = "a"
        expected = "a"
        assert longest_palindrome(s) == expected
    
    def test_all_same_characters(self):
        """Test all same characters"""
        s = "aaaa"
        expected = "aaaa"
        assert longest_palindrome(s) == expected
    
    def test_no_palindrome_longer_than_1(self):
        """Test string with no palindrome longer than 1"""
        s = "abcd"
        result = longest_palindrome(s)
        assert len(result) == 1
        assert result in "abcd"
    
    def test_entire_string_palindrome(self):
        """Test when entire string is palindrome"""
        s = "racecar"
        expected = "racecar"
        assert longest_palindrome(s) == expected
    
    def test_even_length_palindrome(self):
        """Test even length palindrome"""
        s = "abccba"
        expected = "abccba"
        assert longest_palindrome(s) == expected
    
    def test_odd_length_palindrome(self):
        """Test odd length palindrome"""
        s = "abcba"
        expected = "abcba"
        assert longest_palindrome(s) == expected
    
    def test_multiple_palindromes_same_length(self):
        """Test multiple palindromes of same length"""
        s = "abacabad"
        result = longest_palindrome(s)
        # Could be "aba", "aca", "aba", "bab"
        assert len(result) == 3
        # Verify it's actually a palindrome
        assert result == result[::-1]
    
    def test_overlapping_palindromes(self):
        """Test overlapping palindromes"""
        s = "bananas"
        result = longest_palindrome(s)
        # "anana" is the longest
        expected = "anana"
        assert longest_palindrome(s) == expected
    
    def test_palindrome_at_start(self):
        """Test palindrome at start of string"""
        s = "abccde"
        result = longest_palindrome(s)
        # "bcc" is not palindrome, but "cc" is
        assert "cc" in result or len(result) == 1
    
    def test_palindrome_at_end(self):
        """Test palindrome at end of string"""
        s = "abcdd"
        result = longest_palindrome(s)
        assert "dd" == result or len(result) == 1
    
    def verify_palindrome(self, s):
        """Helper to verify a string is a palindrome"""
        return s == s[::-1]
    
    def test_result_is_palindrome(self):
        """Test that result is always a palindrome"""
        test_cases = [
            "babad", "cbbd", "a", "ac", "racecar", 
            "abcdef", "noon", "level", "abccba"
        ]
        
        for s in test_cases:
            result = longest_palindrome(s)
            assert self.verify_palindrome(result), f"Result '{result}' is not a palindrome"
            assert result in s, f"Result '{result}' not found in original string '{s}'"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
