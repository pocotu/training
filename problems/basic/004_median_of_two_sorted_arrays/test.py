"""
Test cases for Median of Two Sorted Arrays problem
Problem ID: 004
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import find_median_sorted_arrays, find_median_merge

class TestMedianSortedArrays:
    """Test class for Median of Two Sorted Arrays problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_empty_arrays(self):
        """Test cases with empty arrays"""
        # One empty array
        nums1 = []
        nums2 = [1]
        expected = 1.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
        
        # Reverse case
        nums1 = [2]
        nums2 = []
        expected = 2.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_single_elements(self):
        """Test arrays with single elements"""
        nums1 = [1]
        nums2 = [2]
        expected = 1.5
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_equal_length_arrays(self):
        """Test arrays of equal length"""
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        expected = 3.5
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_different_length_arrays(self):
        """Test arrays of different lengths"""
        nums1 = [1, 2]
        nums2 = [3, 4, 5, 6]
        expected = 3.5
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_negative_numbers(self):
        """Test arrays with negative numbers"""
        nums1 = [-5, -1]
        nums2 = [-3, 0, 2]
        expected = -1.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_duplicate_numbers(self):
        """Test arrays with duplicate numbers"""
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        expected = 1.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_large_numbers(self):
        """Test arrays with large numbers"""
        nums1 = [1000000]
        nums2 = [999999, 1000001]
        expected = 1000000.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_edge_cases(self):
        """Test various edge cases"""
        # All elements in nums1 are smaller
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        expected = 3.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
        
        # All elements in nums2 are smaller
        nums1 = [4, 5, 6]
        nums2 = [1, 2]
        expected = 4.0
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected
    
    def test_precision(self):
        """Test floating point precision"""
        nums1 = [1]
        nums2 = [2]
        result = find_median_sorted_arrays(nums1, nums2)
        assert abs(result - 1.5) < 1e-9
        
        result_merge = find_median_merge(nums1, nums2)
        assert abs(result_merge - 1.5) < 1e-9
    
    def test_longer_arrays(self):
        """Test with longer arrays"""
        nums1 = [1, 3, 5, 7, 9]
        nums2 = [2, 4, 6, 8, 10, 11, 12]
        # Merged: [1,2,3,4,5,6,7,8,9,10,11,12] -> median = (6+7)/2 = 6.5
        expected = 6.5
        assert find_median_sorted_arrays(nums1, nums2) == expected
        assert find_median_merge(nums1, nums2) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
