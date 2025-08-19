"""
Test cases for String Concatenation
Problem ID: F004
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import concatenate_strings

class TestStringConcatenation(unittest.TestCase):

    def test_concatenate_strings(self):
        """Test basic string concatenation"""
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate_strings("Python ", "Programming"), "Python Programming")
    
    def test_concatenate_empty_strings(self):
        """Test concatenation with empty strings"""
        self.assertEqual(concatenate_strings("", "Hello"), "Hello")
        self.assertEqual(concatenate_strings("World", ""), "World")
        self.assertEqual(concatenate_strings("", ""), "")
    
    def test_concatenate_special_characters(self):
        """Test concatenation with special characters"""
        self.assertEqual(concatenate_strings("123", "456"), "123456")
        self.assertEqual(concatenate_strings("Hello\n", "World!"), "Hello\nWorld!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
