"""
Test cases for Letter Combinations of a Phone Number problem
Problem ID: 108
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import letter_combinations, letter_combinations_iterative, letter_combinations_bfs

class TestLetterCombinations:
    """Test class for Letter Combinations of a Phone Number problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        result = letter_combinations(digits)
        assert sorted(result) == sorted(expected)
        
        # Test other approaches
        assert sorted(letter_combinations_iterative(digits)) == sorted(expected)
        assert sorted(letter_combinations_bfs(digits)) == sorted(expected)
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        digits = ""
        expected = []
        assert letter_combinations(digits) == expected
        assert letter_combinations_iterative(digits) == expected
        assert letter_combinations_bfs(digits) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        digits = "2"
        expected = ["a","b","c"]
        result = letter_combinations(digits)
        assert sorted(result) == sorted(expected)
        
        assert sorted(letter_combinations_iterative(digits)) == sorted(expected)
        assert sorted(letter_combinations_bfs(digits)) == sorted(expected)
    
    def test_single_digit_all(self):
        """Test all single digits"""
        test_cases = {
            "2": ["a","b","c"],
            "3": ["d","e","f"], 
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        
        for digit, expected in test_cases.items():
            result = letter_combinations(digit)
            assert sorted(result) == sorted(expected)
    
    def test_two_digits(self):
        """Test two digit combinations"""
        digits = "34"
        result = letter_combinations(digits)
        # 3 letters * 3 letters = 9 combinations
        assert len(result) == 9
        
        # Check specific combinations
        assert "dg" in result
        assert "fi" in result
        
        # All combinations should be length 2
        assert all(len(combo) == 2 for combo in result)
    
    def test_three_digits(self):
        """Test three digit combinations"""
        digits = "234"
        result = letter_combinations(digits)
        # 3 * 3 * 3 = 27 combinations
        assert len(result) == 27
        
        # All combinations should be length 3
        assert all(len(combo) == 3 for combo in result)
        
        # Check some specific combinations
        assert "adg" in result
        assert "cfi" in result
    
    def test_digit_with_four_letters(self):
        """Test digits that have 4 letters (7 and 9)"""
        # Test digit 7 (pqrs)
        digits = "7"
        result = letter_combinations(digits)
        expected = ["p","q","r","s"]
        assert sorted(result) == sorted(expected)
        
        # Test digit 9 (wxyz)
        digits = "9"
        result = letter_combinations(digits)
        expected = ["w","x","y","z"]
        assert sorted(result) == sorted(expected)
    
    def test_mixed_digits(self):
        """Test combination of 3-letter and 4-letter digits"""
        digits = "27"  # 2 has 3 letters, 7 has 4 letters
        result = letter_combinations(digits)
        # 3 * 4 = 12 combinations
        assert len(result) == 12
        
        # Check specific combinations
        assert "ap" in result
        assert "cs" in result
    
    def test_all_methods_consistency(self):
        """Test that all implementation methods give same results"""
        test_cases = ["2", "23", "234", "7", "79", "2345"]
        
        for digits in test_cases:
            result1 = letter_combinations(digits)
            result2 = letter_combinations_iterative(digits)
            result3 = letter_combinations_bfs(digits)
            
            assert sorted(result1) == sorted(result2) == sorted(result3)
    
    def test_four_digits(self):
        """Test maximum constraint (4 digits)"""
        digits = "2345"
        result = letter_combinations(digits)
        # 3 * 3 * 3 * 3 = 81 combinations
        assert len(result) == 81
        
        # All combinations should be length 4
        assert all(len(combo) == 4 for combo in result)
        
        # Check first and last alphabetically
        sorted_result = sorted(result)
        assert sorted_result[0] == "adgj"
        assert sorted_result[-1] == "cfil"
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Empty string
        assert letter_combinations("") == []
        
        # Single digit with most letters
        result_7 = letter_combinations("7")
        assert len(result_7) == 4
        
        result_9 = letter_combinations("9")
        assert len(result_9) == 4

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
