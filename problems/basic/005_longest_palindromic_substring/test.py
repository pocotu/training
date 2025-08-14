"""
Test cases for Longest Palindromic Substring problem
Problem ID: 005
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import longest_palindrome, longest_palindrome_dp, longest_palindrome_manacher

class TestLongestPalindrome:
    """Test class for Longest Palindromic Substring problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "babad"
        result = longest_palindrome(s)
        # "bab" or "aba" are both valid
        assert result in ["bab", "aba"]
        assert len(result) == 3
        
        result_dp = longest_palindrome_dp(s)
        assert result_dp in ["bab", "aba"]
        
        result_manacher = longest_palindrome_manacher(s)
        assert result_manacher in ["bab", "aba"]
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "cbbd"
        expected = "bb"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_single_character(self):
        """Test single character string"""
        s = "a"
        expected = "a"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_two_characters_same(self):
        """Test two identical characters"""
        s = "aa"
        expected = "aa"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_two_characters_different(self):
        """Test two different characters"""
        s = "ab"
        result = longest_palindrome(s)
        # Either "a" or "b" is valid
        assert result in ["a", "b"]
        assert len(result) == 1
        
        result_dp = longest_palindrome_dp(s)
        assert result_dp in ["a", "b"]
        
        result_manacher = longest_palindrome_manacher(s)
        assert result_manacher in ["a", "b"]
    
    def test_entire_string_palindrome(self):
        """Test when entire string is palindrome"""
        s = "racecar"
        expected = "racecar"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_no_palindrome_longer_than_one(self):
        """Test string with no palindrome longer than 1"""
        s = "abcdef"
        result = longest_palindrome(s)
        assert len(result) == 1
        assert result in "abcdef"
        
        result_dp = longest_palindrome_dp(s)
        assert len(result_dp) == 1
        
        result_manacher = longest_palindrome_manacher(s)
        assert len(result_manacher) == 1
    
    def test_multiple_palindromes(self):
        """Test string with multiple palindromes of same length"""
        s = "abacabad"
        result = longest_palindrome(s)
        # Should find one of the longest palindromes
        assert len(result) >= 3  # "aba" or "aca"
        
        result_dp = longest_palindrome_dp(s)
        assert len(result_dp) >= 3
        
        result_manacher = longest_palindrome_manacher(s)
        assert len(result_manacher) >= 3
    
    def test_even_length_palindrome(self):
        """Test even-length palindromes"""
        s = "abccba"
        expected = "abccba"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_odd_length_palindrome(self):
        """Test odd-length palindromes"""
        s = "abcba"
        expected = "abcba"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_palindrome_at_beginning(self):
        """Test palindrome at beginning of string"""
        s = "abaxyz"
        result = longest_palindrome(s)
        assert "aba" in result or len(result) == 1
        
        result_dp = longest_palindrome_dp(s)
        assert "aba" in result_dp or len(result_dp) == 1
        
        result_manacher = longest_palindrome_manacher(s)
        assert "aba" in result_manacher or len(result_manacher) == 1
    
    def test_palindrome_at_end(self):
        """Test palindrome at end of string"""
        s = "xyzaba"
        result = longest_palindrome(s)
        assert "aba" in result or len(result) == 1
        
        result_dp = longest_palindrome_dp(s)
        assert "aba" in result_dp or len(result_dp) == 1
        
        result_manacher = longest_palindrome_manacher(s)
        assert "aba" in result_manacher or len(result_manacher) == 1
    
    def test_repeating_characters(self):
        """Test string with repeating characters"""
        s = "aaaaaa"
        expected = "aaaaaa"
        assert longest_palindrome(s) == expected
        assert longest_palindrome_dp(s) == expected
        assert longest_palindrome_manacher(s) == expected
    
    def test_mixed_case_and_digits(self):
        """Test string with mixed case and digits"""
        s = "Aa1a2A"
        result = longest_palindrome(s)
        # Should handle case sensitivity
        assert len(result) >= 1
        
        result_dp = longest_palindrome_dp(s)
        assert len(result_dp) >= 1
        
        result_manacher = longest_palindrome_manacher(s)
        assert len(result_manacher) >= 1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
