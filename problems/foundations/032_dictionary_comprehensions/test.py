"""
Test cases for Dictionary Comprehensions
Problem ID: F032
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_squared_dict

class TestDictionaryComprehensions(unittest.TestCase):

    def test_create_squared_dict(self):
        """Test basic dictionary comprehension"""
        self.assertEqual(create_squared_dict([1, 2, 3]), {1: 1, 2: 4, 3: 9})
    
    def test_create_squared_dict_empty(self):
        """Test with empty list"""
        self.assertEqual(create_squared_dict([]), {})
    
    def test_create_squared_dict_negative_numbers(self):
        """Test with negative numbers"""
        expected = {-2: 4, 0: 0, 2: 4}
        self.assertEqual(create_squared_dict([-2, 0, 2]), expected)
    
    def test_create_squared_dict_single_element(self):
        """Test with single element"""
        self.assertEqual(create_squared_dict([5]), {5: 25})

if __name__ == '__main__':
    unittest.main(verbosity=2)
