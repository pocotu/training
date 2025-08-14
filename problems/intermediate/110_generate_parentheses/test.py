"""
Test cases for Generate Parentheses problem
Problem ID: 110
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import generate_parenthesis, generate_parenthesis_dp, generate_parenthesis_iterative, is_valid_parentheses, count_valid_parentheses

class TestGenerateParentheses:
    """Test class for Generate Parentheses problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        n = 3
        result = generate_parenthesis(n)
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        assert sorted(result) == sorted(expected)
        
        # Test other approaches
        assert sorted(generate_parenthesis_dp(n)) == sorted(expected)
        assert sorted(generate_parenthesis_iterative(n)) == sorted(expected)
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        n = 1
        result = generate_parenthesis(n)
        expected = ["()"]
        assert result == expected
        
        assert generate_parenthesis_dp(n) == expected
        assert generate_parenthesis_iterative(n) == expected
    
    def test_n_equals_2(self):
        """Test n = 2 case"""
        n = 2
        result = generate_parenthesis(n)
        expected = ["(())","()()"]
        assert sorted(result) == sorted(expected)
        
        # Verify all approaches agree
        assert sorted(generate_parenthesis_dp(n)) == sorted(expected)
        assert sorted(generate_parenthesis_iterative(n)) == sorted(expected)
    
    def test_n_equals_4(self):
        """Test n = 4 case"""
        n = 4
        result = generate_parenthesis(n)
        
        # Should have 14 combinations (4th Catalan number)
        assert len(result) == 14
        
        # All strings should be length 8
        assert all(len(s) == 8 for s in result)
        
        # All should be valid
        assert all(is_valid_parentheses(s) for s in result)
        
        # Check specific combinations exist
        assert "(((())))" in result
        assert "()()()()" in result
    
    def test_catalan_numbers(self):
        """Test that results match Catalan numbers"""
        catalan_expected = [1, 1, 2, 5, 14, 42]  # C(0) through C(5)
        
        for n in range(6):
            if n == 0:
                # Special case for n=0
                continue
            
            result = generate_parenthesis(n)
            catalan_calc = count_valid_parentheses(n)
            
            assert len(result) == catalan_expected[n]
            assert len(result) == catalan_calc
    
    def test_all_results_valid(self):
        """Test that all generated parentheses are valid"""
        for n in range(1, 6):
            result = generate_parenthesis(n)
            
            for parentheses in result:
                assert is_valid_parentheses(parentheses), f"Invalid: {parentheses}"
                assert len(parentheses) == 2 * n, f"Wrong length: {parentheses}"
    
    def test_all_methods_consistency(self):
        """Test that all implementation methods give same results"""
        for n in range(1, 5):
            result1 = generate_parenthesis(n)
            result2 = generate_parenthesis_dp(n)
            result3 = generate_parenthesis_iterative(n)
            
            assert sorted(result1) == sorted(result2) == sorted(result3)
    
    def test_no_duplicates(self):
        """Test that there are no duplicate results"""
        for n in range(1, 5):
            result = generate_parenthesis(n)
            assert len(result) == len(set(result)), f"Duplicates found for n={n}"
    
    def test_specific_patterns(self):
        """Test specific pattern expectations"""
        # n=1: only "()"
        assert generate_parenthesis(1) == ["()"]
        
        # n=2: nested and sequential
        result_2 = generate_parenthesis(2)
        assert "(())" in result_2  # nested
        assert "()()" in result_2  # sequential
        
        # n=3: should include all nested
        result_3 = generate_parenthesis(3)
        assert "((()))" in result_3  # fully nested
        assert "()()()" in result_3  # fully sequential
    
    def test_edge_cases(self):
        """Test edge cases"""
        # n=0 would be empty string, but typically not tested
        # since problem states n >= 1
        
        # n=1 minimal case
        result = generate_parenthesis(1)
        assert result == ["()"]
        assert len(result) == 1
    
    def test_valid_parentheses_helper(self):
        """Test the validation helper function"""
        # Valid cases
        assert is_valid_parentheses("()")
        assert is_valid_parentheses("(())")
        assert is_valid_parentheses("()()")
        assert is_valid_parentheses("((()))")
        
        # Invalid cases
        assert not is_valid_parentheses("(")
        assert not is_valid_parentheses(")")
        assert not is_valid_parentheses("(()")
        assert not is_valid_parentheses("())")
        assert not is_valid_parentheses("))(")
    
    def test_catalan_calculation(self):
        """Test Catalan number calculation function"""
        expected_catalan = [1, 1, 2, 5, 14, 42, 132]
        
        for i, expected in enumerate(expected_catalan):
            assert count_valid_parentheses(i) == expected
    
    def test_performance_characteristics(self):
        """Test that results grow as expected"""
        prev_count = 0
        for n in range(1, 6):
            result = generate_parenthesis(n)
            current_count = len(result)
            
            # Count should increase (Catalan numbers are increasing)
            assert current_count > prev_count
            prev_count = current_count

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
