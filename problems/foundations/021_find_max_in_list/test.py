"""
Test cases for Find Max in List
Problem ID: F021
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import find_max

class TestFindMaxInList(unittest.TestCase):

    def test_find_max(self):
        """Test basic max finding"""
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, -5, -3]), -1)
    
    def test_find_max_single_element(self):
        """Test with single element"""
        self.assertEqual(find_max([42]), 42)
        self.assertEqual(find_max([-10]), -10)
    
    def test_find_max_duplicates(self):
        """Test with duplicate maximum values"""
        self.assertEqual(find_max([3, 1, 3, 2]), 3)
        self.assertEqual(find_max([0, 0, 0]), 0)
    
    def test_find_max_mixed_numbers(self):
        """Test with mixed positive and negative"""
        self.assertEqual(find_max([-1, 0, 1]), 1)
        self.assertEqual(find_max([10, -5, 3, -2, 8]), 10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
