"""
Test cases for Set Creation and Unique Elements
Problem ID: F033
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_unique_elements

class TestSetCreationAndUniqueElements(unittest.TestCase):

    def test_get_unique_elements(self):
        """Test basic unique element extraction"""
        result = get_unique_elements([1, 2, 2, 3, 1, 4])
        expected = [1, 2, 3, 4]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_get_unique_elements_empty(self):
        """Test with empty list"""
        self.assertEqual(get_unique_elements([]), [])
    
    def test_get_unique_elements_all_same(self):
        """Test with all identical elements"""
        result = get_unique_elements([5, 5, 5])
        self.assertEqual(result, [5])
    
    def test_get_unique_elements_already_unique(self):
        """Test with already unique elements"""
        result = get_unique_elements([1, 2, 3, 4])
        expected = [1, 2, 3, 4]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_get_unique_elements_mixed_types(self):
        """Test that result is a list"""
        result = get_unique_elements([1, 2, 1, 3])
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
