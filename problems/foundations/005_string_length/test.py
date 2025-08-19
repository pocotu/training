"""
Test cases for String Length
Problem ID: F005
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_string_length

class TestStringLength(unittest.TestCase):

    def test_get_string_length(self):
        """Test basic string length"""
        self.assertEqual(get_string_length("Hello"), 5)
        self.assertEqual(get_string_length(""), 0)
    
    def test_get_string_length_special_cases(self):
        """Test string length with special characters"""
        self.assertEqual(get_string_length("Hello World!"), 12)
        self.assertEqual(get_string_length("123456789"), 9)
        self.assertEqual(get_string_length("   "), 3)  # spaces
    
    def test_get_string_length_unicode(self):
        """Test string length with unicode characters"""
        self.assertEqual(get_string_length("café"), 4)
        self.assertEqual(get_string_length("Hello\nWorld"), 11)  # with newline

if __name__ == '__main__':
    unittest.main(verbosity=2)
