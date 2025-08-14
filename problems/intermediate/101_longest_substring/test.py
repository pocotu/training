"""
Test cases for Longest Substring Without Repeating Characters problem
Problem ID: 101
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import length_of_longest_substring

class TestLongestSubstring:
    """Test class for Longest Substring Without Repeating Characters problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "abcabcbb"
        expected = 3  # "abc"
        assert length_of_longest_substring(s) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "bbbbb"
        expected = 1  # "b"
        assert length_of_longest_substring(s) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        s = "pwwkew"
        expected = 3  # "wke"
        assert length_of_longest_substring(s) == expected
    
    def test_empty_string(self):
        """Test empty string"""
        assert length_of_longest_substring("") == 0
    
    def test_single_character(self):
        """Test single character"""
        assert length_of_longest_substring("a") == 1
    
    def test_all_unique(self):
        """Test string with all unique characters"""
        s = "abcdef"
        assert length_of_longest_substring(s) == 6
    
    def test_all_same(self):
        """Test string with all same characters"""
        s = "aaaa"
        assert length_of_longest_substring(s) == 1
    
    def test_two_characters(self):
        """Test two character patterns"""
        assert length_of_longest_substring("ab") == 2
        assert length_of_longest_substring("aa") == 1
        assert length_of_longest_substring("abab") == 2
    
    def test_complex_patterns(self):
        """Test complex patterns"""
        assert length_of_longest_substring("abba") == 2  # "ab" or "ba"
        assert length_of_longest_substring("tmmzuxt") == 5  # "mzuxt"
        assert length_of_longest_substring("dvdf") == 3   # "vdf"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
