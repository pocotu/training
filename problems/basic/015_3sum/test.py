"""
Test cases for 3Sum problem
Problem ID: 015
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import three_sum, three_sum_brute_force

class TestThreeSum:
    """Test class for 3Sum problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        nums = [-1, 0, 1, 2, -1, -4]
        result = three_sum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(result) == sorted(expected)
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        nums = [0, 1, 1]
        result = three_sum(nums)
        expected = []
        assert result == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        nums = [0, 0, 0]
        result = three_sum(nums)
        expected = [[0, 0, 0]]
        assert result == expected
    
    def test_no_solution(self):
        """Test case with no valid triplets"""
        nums = [1, 2, 3]
        result = three_sum(nums)
        assert result == []
    
    def test_multiple_solutions(self):
        """Test case with multiple solutions"""
        nums = [-2, 0, 1, 1, 2]
        result = three_sum(nums)
        # Should find [-2, 0, 2] and [-2, 1, 1]
        assert len(result) == 2
        assert [-2, 0, 2] in result
        assert [-2, 1, 1] in result
    
    def test_duplicates(self):
        """Test handling of duplicate numbers"""
        nums = [-1, 0, 1, 0]
        result = three_sum(nums)
        expected = [[-1, 0, 1]]
        assert result == expected
    
    def test_all_negative(self):
        """Test all negative numbers"""
        nums = [-3, -2, -1]
        result = three_sum(nums)
        assert result == []
    
    def test_all_positive(self):
        """Test all positive numbers"""
        nums = [1, 2, 3]
        result = three_sum(nums)
        assert result == []
    
    def test_minimum_length(self):
        """Test minimum array length"""
        nums = [0, 0, 0]
        result = three_sum(nums)
        assert result == [[0, 0, 0]]
    
    def test_comparison_with_brute_force(self):
        """Compare optimized solution with brute force"""
        test_cases = [
            [-1, 0, 1, 2, -1, -4],
            [0, 1, 1],
            [0, 0, 0],
            [-2, 0, 1, 1, 2],
            [1, -1, 0, 2, -2]
        ]
        
        for nums in test_cases:
            result_opt = three_sum(nums.copy())
            result_brute = three_sum_brute_force(nums.copy())
            assert sorted(result_opt) == sorted(result_brute)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
