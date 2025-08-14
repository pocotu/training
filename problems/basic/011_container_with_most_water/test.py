"""
Test cases for Container With Most Water problem
Problem ID: 011
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import max_area, max_area_brute_force

class TestContainerWithMostWater:
    """Test class for Container With Most Water problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        assert max_area(height) == expected
        assert max_area_brute_force(height) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        height = [1, 1]
        expected = 1
        assert max_area(height) == expected
        assert max_area_brute_force(height) == expected
    
    def test_increasing_heights(self):
        """Test increasing heights"""
        height = [1, 2, 3, 4, 5]
        result = max_area(height)
        assert result == max_area_brute_force(height)
        assert result == 6  # height[0] * 4 or height[1] * 3
    
    def test_decreasing_heights(self):
        """Test decreasing heights"""
        height = [5, 4, 3, 2, 1]
        result = max_area(height)
        assert result == max_area_brute_force(height)
        assert result == 6  # height[4] * 4 or height[3] * 3
    
    def test_same_heights(self):
        """Test all same heights"""
        height = [3, 3, 3, 3]
        expected = 9  # 3 * 3
        assert max_area(height) == expected
        assert max_area_brute_force(height) == expected
    
    def test_two_tall_edges(self):
        """Test two tall edges with smaller middle values"""
        height = [8, 1, 2, 1, 8]
        expected = 32  # 8 * 4
        assert max_area(height) == expected
        assert max_area_brute_force(height) == expected
    
    def test_minimum_case(self):
        """Test minimum case with 2 elements"""
        height = [2, 1]
        expected = 1  # min(2,1) * 1
        assert max_area(height) == expected
        assert max_area_brute_force(height) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
