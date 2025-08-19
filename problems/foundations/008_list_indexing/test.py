"""
Test cases for List Indexing
Problem ID: F008
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_list_element

class TestListIndexing(unittest.TestCase):

    def test_get_list_element(self):
        """Test basic list indexing"""
        self.assertEqual(get_list_element([10, 20, 30], 1), 20)
        self.assertEqual(get_list_element(["a", "b", "c"], 0), "a")
    
    def test_get_list_element_last_index(self):
        """Test accessing last element"""
        self.assertEqual(get_list_element([5, 15, 25, 35], 3), 35)
    
    def test_get_list_element_negative_index(self):
        """Test negative indexing"""
        self.assertEqual(get_list_element([1, 2, 3], -1), 3)
        self.assertEqual(get_list_element([1, 2, 3], -2), 2)
    
    def test_get_list_element_single_item(self):
        """Test list with single element"""
        self.assertEqual(get_list_element([42], 0), 42)
        self.assertEqual(get_list_element([42], -1), 42)

if __name__ == '__main__':
    unittest.main(verbosity=2)
