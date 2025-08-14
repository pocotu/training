"""
Test cases for 3Sum problem
Problem ID: 104
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import three_sum

class TestThreeSum:
    """Test class for 3Sum problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]
        result = three_sum(nums)
        # Sort both result and expected for comparison
        result_sorted = [sorted(triplet) for triplet in result]
        expected_sorted = [sorted(triplet) for triplet in expected]
        assert sorted(result_sorted) == sorted(expected_sorted)
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        nums = [0,1,1]
        expected = []
        assert three_sum(nums) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        nums = [0,0,0]
        expected = [[0,0,0]]
        result = three_sum(nums)
        assert len(result) == 1
        assert [0,0,0] in result
    
    def test_all_negative(self):
        """Test all negative numbers"""
        nums = [-3, -2, -1]
        expected = []
        assert three_sum(nums) == expected
    
    def test_all_positive(self):
        """Test all positive numbers"""
        nums = [1, 2, 3]
        expected = []
        assert three_sum(nums) == expected
    
    def test_two_elements(self):
        """Test with less than 3 elements"""
        nums = [1, 2]
        expected = []
        assert three_sum(nums) == expected
    
    def test_exactly_three_elements(self):
        """Test with exactly 3 elements"""
        nums = [-1, 0, 1]
        expected = [[-1, 0, 1]]
        result = three_sum(nums)
        assert len(result) == 1
        assert sorted(result[0]) == [-1, 0, 1]
    
    def test_no_duplicates(self):
        """Test that result contains no duplicates"""
        nums = [-1, 0, 1, 2, -1, -4, -1, 0, 1]
        result = three_sum(nums)
        
        # Convert to set of tuples for duplicate check
        result_set = set(tuple(sorted(triplet)) for triplet in result)
        assert len(result) == len(result_set)
    
    def test_multiple_solutions(self):
        """Test case with multiple solutions"""
        nums = [-2, 0, 1, 1, 2]
        result = three_sum(nums)
        
        # Should have solutions like [-2, 0, 2] and [-2, 1, 1]
        result_sorted = [tuple(sorted(triplet)) for triplet in result]
        
        assert (-2, 0, 2) in result_sorted
        assert (-2, 1, 1) in result_sorted
    
    def test_all_sums_zero(self):
        """Test that all returned triplets sum to zero"""
        nums = [-4, -1, -1, 0, 1, 2]
        result = three_sum(nums)
        
        for triplet in result:
            assert sum(triplet) == 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
