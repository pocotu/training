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

if __name__ == '__main__':
    unittest.main()
