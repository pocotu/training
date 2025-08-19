"""
Test cases for Iterating Dictionary Items
Problem ID: F031
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import format_dictionary

class TestIteratingDictionaryItems(unittest.TestCase):

    def test_format_dictionary(self):
        """Test basic dictionary formatting"""
        d = {"name": "John", "age": 30}
        result = format_dictionary(d)
        expected = ["name: John", "age: 30"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_format_dictionary_empty(self):
        """Test with empty dictionary"""
        self.assertEqual(format_dictionary({}), [])
    
    def test_format_dictionary_different_types(self):
        """Test with different value types"""
        d = {"count": 0, "active": True, "items": [1, 2, 3]}
        result = format_dictionary(d)
        expected = ["count: 0", "active: True", "items: [1, 2, 3]"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_format_dictionary_single_item(self):
        """Test with single item dictionary"""
        d = {"key": "value"}
        self.assertEqual(format_dictionary(d), ["key: value"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
