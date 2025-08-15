"""
Test cases for Intersection of Two Arrays II
Problem ID: 045
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import intersect, intersect_sorted, intersect_optimized

class TestIntersectionOfTwoArraysII(unittest.TestCase):

    def test_example_1(self):
        """Test example 1 from problem statement"""
        result = intersect([1,2,2,1], [2,2])
        self.assertEqual(sorted(result), [2,2])

    def test_example_2(self):
        """Test example 2 from problem statement"""
        result = intersect([4,9,5], [9,4,9,8,4])
        self.assertEqual(sorted(result), [4,9])

    def test_no_intersection(self):
        """Test arrays with no common elements"""
        result = intersect([1,2,3], [4,5,6])
        self.assertEqual(result, [])

    def test_different_frequencies(self):
        """Test arrays with different frequencies"""
        result = intersect([1,1,1], [1,1])
        self.assertEqual(sorted(result), [1,1])

    def test_single_elements(self):
        """Test single element arrays"""
        result = intersect([1], [1])
        self.assertEqual(result, [1])

    def test_empty_arrays(self):
        """Test with empty arrays"""
        result = intersect([], [1,2,3])
        self.assertEqual(result, [])
        
        result = intersect([1,2,3], [])
        self.assertEqual(result, [])

    def test_duplicate_elements(self):
        """Test arrays with many duplicates"""
        result = intersect([1,2,2,2,3], [2,2,3,3,3])
        expected = sorted([2,2,3])
        self.assertEqual(sorted(result), expected)

    def test_all_same_elements(self):
        """Test arrays with all same elements"""
        result = intersect([5,5,5], [5,5])
        self.assertEqual(sorted(result), [5,5])

if __name__ == '__main__':
    unittest.main(verbosity=2)