"""
Test cases for Palindrome Number problem
Problem ID: 009
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import is_palindrome, is_palindrome_string

class TestPalindromeNumber:
    """Test class for Palindrome Number problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        x = 121
        assert is_palindrome(x) == True
        assert is_palindrome_string(x) == True
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        x = -121
        assert is_palindrome(x) == False
        assert is_palindrome_string(x) == False
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        x = 10
        assert is_palindrome(x) == False
        assert is_palindrome_string(x) == False
    
    def test_single_digit(self):
        """Test single digit numbers"""
        for i in range(10):
            assert is_palindrome(i) == True
            assert is_palindrome_string(i) == True
    
    def test_negative_numbers(self):
        """Test negative numbers"""
        negative_cases = [-1, -123, -121, -1001]
        for num in negative_cases:
            assert is_palindrome(num) == False
            assert is_palindrome_string(num) == False
    
    def test_palindromes(self):
        """Test known palindromes"""
        palindromes = [0, 1, 11, 121, 1221, 12321, 123454321, 1234567899987654321]
        for num in palindromes:
            assert is_palindrome(num) == True
            assert is_palindrome_string(num) == True
    
    def test_non_palindromes(self):
        """Test known non-palindromes"""
        non_palindromes = [12, 123, 1234, 12345, 100, 1000, 10001]
        for num in non_palindromes:
            assert is_palindrome(num) == False
            assert is_palindrome_string(num) == False
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Numbers ending in zero (except 0)
        assert is_palindrome(10) == False
        assert is_palindrome(100) == False
        assert is_palindrome(1000) == False
        assert is_palindrome(0) == True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
