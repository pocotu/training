"""
Test cases for filter() function
Problem ID: F040
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import filter_even_numbers

class TestFilterFunction(unittest.TestCase):

    def test_filter_even_numbers(self):
        """Test basic even number filtering"""
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
    
    def test_filter_even_numbers_empty(self):
        """Test with empty list"""
        self.assertEqual(filter_even_numbers([]), [])
    
    def test_filter_even_numbers_all_odd(self):
        """Test with all odd numbers"""
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
    
    def test_filter_even_numbers_all_even(self):
        """Test with all even numbers"""
        self.assertEqual(filter_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])
    
    def test_filter_even_numbers_with_zero(self):
        """Test that zero is considered even"""
        self.assertEqual(filter_even_numbers([-2, 0, 1, 2]), [-2, 0, 2])

if __name__ == '__main__':
    unittest.main(verbosity=2)
