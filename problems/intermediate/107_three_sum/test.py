#!/usr/bin/env python3
"""
Unit tests for 3Sum (Problem 107)

Tests array manipulation and algorithms with comprehensive test cases.
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to sys.path to import solution
sys.path.append(str(Path(__file__).parent))

try:
    from solution import Solution3sum
except ImportError:
    # Fallback if solution file doesn't exist yet
    class Solution3sum:
        def solve_3sum(self, nums):
            raise NotImplementedError("Solution not implemented yet")


class TestSolution3sum(unittest.TestCase):
    """Test cases for 3Sum."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution3sum()
    
    def test_basic_array(self):
        """Test basic array functionality."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.solve_3sum(nums)
        # Adjust expected result based on specific problem
        self.assertIsNotNone(result, "Should return a valid result")
    
    def test_empty_array(self):
        """Test edge case with empty array."""
        nums = []
        result = self.solution.solve_3sum(nums)
        # Adjust based on problem requirements
        self.assertIsNotNone(result, "Should handle empty array")
    
    def test_single_element(self):
        """Test edge case with single element."""
        nums = [42]
        result = self.solution.solve_3sum(nums)
        self.assertIsNotNone(result, "Should handle single element")
    
    def test_duplicate_elements(self):
        """Test array with duplicate elements."""
        nums = [1, 1, 2, 2, 3, 3]
        result = self.solution.solve_3sum(nums)
        self.assertIsNotNone(result, "Should handle duplicates")
    
    def test_sorted_array(self):
        """Test with sorted array."""
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.solve_3sum(nums)
        self.assertIsNotNone(result, "Should handle sorted array")
    
    def test_reverse_sorted_array(self):
        """Test with reverse sorted array."""
        nums = [6, 5, 4, 3, 2, 1]
        result = self.solution.solve_3sum(nums)
        self.assertIsNotNone(result, "Should handle reverse sorted array")
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-3, -1, 0, 1, 3]
        result = self.solution.solve_3sum(nums)
        self.assertIsNotNone(result, "Should handle negative numbers")
    
    def test_large_array(self):
        """Test performance with large array."""
        nums = list(range(10000))
        
        import time
        start_time = time.time()
        result = self.solution.solve_3sum(nums)
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 1.0, "Should be efficient")
        self.assertIsNotNone(result, "Should handle large arrays")


if __name__ == "__main__":
    unittest.main(verbosity=2)
