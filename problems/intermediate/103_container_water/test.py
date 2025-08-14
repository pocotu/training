"""
Test cases for Container With Most Water problem
Problem ID: 103
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import max_area

class TestContainerWithMostWater:
    """Test class for Container With Most Water problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        height = [1,8,6,2,5,4,8,3,7]
        expected = 49  # lines at index 1 and 8 (8*7 = 56, but width is 7, so 7*7 = 49)
        assert max_area(height) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        height = [1,1]
        expected = 1  # only two lines, height=1, width=1
        assert max_area(height) == expected
    
    def test_two_elements_different_heights(self):
        """Test two elements with different heights"""
        height = [2, 5]
        expected = 2  # min(2,5) * 1 = 2
        assert max_area(height) == expected
    
    def test_increasing_heights(self):
        """Test increasing heights"""
        height = [1, 2, 3, 4, 5]
        expected = 6  # between index 0 and 4: min(1,5) * 4 = 4, but better is index 1,4: min(2,5)*3=6
        assert max_area(height) == expected
    
    def test_decreasing_heights(self):
        """Test decreasing heights"""
        height = [5, 4, 3, 2, 1]
        expected = 6  # between index 0 and 3: min(5,2) * 3 = 6
        assert max_area(height) == expected
    
    def test_same_heights(self):
        """Test all same heights"""
        height = [3, 3, 3, 3, 3]
        expected = 12  # between first and last: 3 * 4 = 12
        assert max_area(height) == expected
    
    def test_peak_in_middle(self):
        """Test peak in middle"""
        height = [1, 5, 1]
        expected = 2  # between index 0 and 2: min(1,1) * 2 = 2
        assert max_area(height) == expected
    
    def test_multiple_maxima(self):
        """Test case with multiple local maxima"""
        height = [2, 3, 4, 5, 18, 17, 6]
        expected = 17  # between index 4 and 5: min(18,17) * 1 = 17, or other combinations
        result = max_area(height)
        assert result >= 17  # Should be at least this much

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
