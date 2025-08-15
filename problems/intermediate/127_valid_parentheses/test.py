"""
Test cases for Valid Parentheses problem
Problem ID: 107
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import is_valid

class TestValidParentheses:
    """Test class for Valid Parentheses problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        s = "()"
        assert is_valid(s) == True
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        s = "()[]{}"
        assert is_valid(s) == True
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        s = "(]"
        assert is_valid(s) == False
    
    def test_empty_string(self):
        """Test empty string"""
        s = ""
        assert is_valid(s) == True
    
    def test_single_opening(self):
        """Test single opening bracket"""
        assert is_valid("(") == False
        assert is_valid("[") == False
        assert is_valid("{") == False
    
    def test_single_closing(self):
        """Test single closing bracket"""
        assert is_valid(")") == False
        assert is_valid("]") == False
        assert is_valid("}") == False
    
    def test_nested_valid(self):
        """Test nested valid parentheses"""
        assert is_valid("([{}])") == True
        assert is_valid("((()))") == True
        assert is_valid("{[()]}") == True
    
    def test_nested_invalid(self):
        """Test nested invalid parentheses"""
        assert is_valid("([)]") == False
        assert is_valid("((]") == False
        assert is_valid("{[}]") == False
    
    def test_mismatched_pairs(self):
        """Test mismatched pairs"""
        assert is_valid("(]") == False
        assert is_valid("([)]") == False
        assert is_valid("{[}") == False
    
    def test_extra_closing(self):
        """Test extra closing brackets"""
        assert is_valid("())") == False
        assert is_valid("()]") == False
        assert is_valid("(){}]}") == False
    
    def test_extra_opening(self):
        """Test extra opening brackets"""
        assert is_valid("(()") == False
        assert is_valid("({[") == False
        assert is_valid("({[}") == False
    
    def test_complex_valid_cases(self):
        """Test complex valid cases"""
        assert is_valid("()[]{}") == True
        assert is_valid("([]){}") == True
        assert is_valid("{[()()]}") == True
        assert is_valid("(({}))[]") == True
    
    def test_complex_invalid_cases(self):
        """Test complex invalid cases"""
        assert is_valid("([{}]))]") == False
        assert is_valid("(({})[]]") == False
        assert is_valid("{[(())]}]") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
