"""
Test cases for Two Sum problem
Problem ID: 001
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import two_sum

class TestTwoSum:
    """Test class for Two Sum problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        assert result == [0, 1]
        # Verify the sum is correct
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        assert result == [1, 2]
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        assert result == [0, 1]
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Minimum length array
        nums = [1, 2]
        target = 3
        result = two_sum(nums, target)
        assert result == [0, 1]
        
        # Negative numbers
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = two_sum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target
        
        # Zero target
        nums = [0, 4, 3, 0]
        target = 0
        result = two_sum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_corner_cases(self):
        """Test corner cases"""
        # Large numbers
        nums = [1000000000, -1000000000, 999999999]
        target = 1999999999
        result = two_sum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target
        
        # Different order result (both [0,2] and [2,0] are valid)
        nums = [3, 2, 4]
        target = 7
        result = two_sum(nums, target)
        assert sorted(result) == [0, 2]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
