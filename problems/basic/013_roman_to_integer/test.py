"""
Test cases for Roman to Integer problem
Problem ID: 013
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import roman_to_int, roman_to_int_left_to_right

class TestRomanToInteger:
    """Test class for Roman to Integer problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "III"
        expected = 3
        assert roman_to_int(s) == expected
        assert roman_to_int_left_to_right(s) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "LVIII"
        expected = 58
        assert roman_to_int(s) == expected
        assert roman_to_int_left_to_right(s) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        s = "MCMXC"
        expected = 1994
        assert roman_to_int(s) == expected
        assert roman_to_int_left_to_right(s) == expected
    
    def test_single_characters(self):
        """Test single character romans"""
        cases = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]
        for roman, expected in cases:
            assert roman_to_int(roman) == expected
            assert roman_to_int_left_to_right(roman) == expected
    
    def test_subtractive_cases(self):
        """Test subtractive notation cases"""
        cases = [("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900)]
        for roman, expected in cases:
            assert roman_to_int(roman) == expected
            assert roman_to_int_left_to_right(roman) == expected
    
    def test_complex_numbers(self):
        """Test complex roman numerals"""
        cases = [
            ("MCDXLIV", 1444),
            ("MCMLIV", 1954),
            ("MCMXC", 1990),
            ("MMCDXLIV", 2444),
            ("MMMCMXCIX", 3999)
        ]
        for roman, expected in cases:
            assert roman_to_int(roman) == expected
            assert roman_to_int_left_to_right(roman) == expected
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Minimum value
        assert roman_to_int("I") == 1
        # Maximum typical value
        assert roman_to_int("MMMCMXCIX") == 3999

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
