"""
Test cases for List Creation
Problem ID: F007
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_list

class TestListCreation(unittest.TestCase):

    def test_create_list(self):
        """Test that the function returns [1, 2, 3]"""
        result = create_list()
        expected = [1, 2, 3]
        self.assertEqual(result, expected)
        self.assertIsInstance(result, list)
    
    def test_create_list_length(self):
        """Test that the list has exactly 3 elements"""
        result = create_list()
        self.assertEqual(len(result), 3)
    
    def test_create_list_element_types(self):
        """Test that all elements are integers"""
        result = create_list()
        for element in result:
            self.assertIsInstance(element, int)
    
    def test_create_list_independence(self):
        """Test that multiple calls return independent lists"""
        list1 = create_list()
        list2 = create_list()
        list1.append(4)
        self.assertNotEqual(list1, list2)  # Should be different after modification

if __name__ == '__main__':
    unittest.main()
