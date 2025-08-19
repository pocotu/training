"""
Test cases for Dictionary get() method
Problem ID: F030
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_value_safely

class TestDictionaryGetMethod(unittest.TestCase):

    def test_get_value_safely(self):
        """Test basic get method usage"""
        d = {"name": "John", "age": 30}
        self.assertEqual(get_value_safely(d, "name"), "John")
        self.assertEqual(get_value_safely(d, "city"), "Not Found")
    
    def test_get_value_safely_existing_keys(self):
        """Test with existing keys of different types"""
        d = {"count": 0, "active": False, "list": [1, 2, 3]}
        self.assertEqual(get_value_safely(d, "count"), 0)
        self.assertEqual(get_value_safely(d, "active"), False)
        self.assertEqual(get_value_safely(d, "list"), [1, 2, 3])
    
    def test_get_value_safely_empty_dict(self):
        """Test with empty dictionary"""
        self.assertEqual(get_value_safely({}, "any_key"), "Not Found")
    
    def test_get_value_safely_none_value(self):
        """Test when actual value is None"""
        d = {"key": None}
        self.assertEqual(get_value_safely(d, "key"), None)
        self.assertEqual(get_value_safely(d, "missing"), "Not Found")

if __name__ == '__main__':
    unittest.main(verbosity=2)
