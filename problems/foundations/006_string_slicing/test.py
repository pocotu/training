"""
Test cases for String Slicing
Problem ID: F006
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_substring

class TestStringSlicing(unittest.TestCase):

    def test_get_substring(self):
        """Test basic string slicing"""
        result = get_substring("Hello, World!", 7, 12)
        self.assertEqual(result, "World")
    
    def test_get_substring_beginning(self):
        """Test slicing from beginning"""
        result = get_substring("Python", 0, 3)
        self.assertEqual(result, "Pyt")
    
    def test_get_substring_end(self):
        """Test slicing to end"""
        result = get_substring("Programming", 4, 11)
        self.assertEqual(result, "ramming")
    
    def test_get_substring_single_character(self):
        """Test slicing single character"""
        result = get_substring("Hello", 1, 2)
        self.assertEqual(result, "e")
    
    def test_get_substring_empty_range(self):
        """Test slicing with same start and end"""
        result = get_substring("Test", 2, 2)
        self.assertEqual(result, "")
    
    def test_get_substring_full_string(self):
        """Test slicing entire string"""
        result = get_substring("Hello", 0, 5)
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
