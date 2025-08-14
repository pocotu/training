"""
Test cases for Longest Substring Without Repeating Characters problem
Problem ID: 003
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import length_of_longest_substring, length_of_longest_substring_set, length_of_longest_substring_optimized

class TestLongestSubstring:
    """Test class for Longest Substring Without Repeating Characters problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "abcabcbb"
        expected = 3
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "bbbbb"
        expected = 1
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        s = "pwwkew"
        expected = 3
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_empty_string(self):
        """Test empty string"""
        s = ""
        expected = 0
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_single_character(self):
        """Test single character"""
        s = "a"
        expected = 1
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_no_repeating_characters(self):
        """Test string with no repeating characters"""
        s = "abcdef"
        expected = 6
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_all_same_characters(self):
        """Test string with all same characters"""
        s = "aaaaa"
        expected = 1
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_special_characters(self):
        """Test string with special characters and spaces"""
        s = "a!@# $%^&*()"
        expected = 11
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_numbers(self):
        """Test string with numbers"""
        s = "0123456789"
        expected = 10
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_mixed_characters(self):
        """Test string with mixed characters"""
        s = "abcABC123!@#"
        expected = 12
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_long_string(self):
        """Test longer string"""
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = 26
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected
    
    def test_pattern_repetition(self):
        """Test string with pattern repetition"""
        s = "abcabcabcabcabc"
        expected = 3
        assert length_of_longest_substring(s) == expected
        assert length_of_longest_substring_set(s) == expected
        assert length_of_longest_substring_optimized(s) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
