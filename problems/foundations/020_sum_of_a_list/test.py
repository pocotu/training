"""
Test cases for Sum of a List
Problem ID: F020
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import calculate_sum

class TestSumOfAList(unittest.TestCase):

    def test_calculate_sum(self):
        """Test basic sum calculation without built-in sum()"""
        self.assertEqual(calculate_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(calculate_sum([]), 0)
        self.assertEqual(calculate_sum([-1, 1]), 0)
    
    def test_calculate_sum_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(calculate_sum([-2, 5, -1]), 2)
        self.assertEqual(calculate_sum([-1, -2, -3]), -6)
    
    def test_calculate_sum_single_element(self):
        """Test with single element"""
        self.assertEqual(calculate_sum([42]), 42)
        self.assertEqual(calculate_sum([0]), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
