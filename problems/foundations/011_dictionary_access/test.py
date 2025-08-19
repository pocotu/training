"""
Test cases for Dictionary Access
Problem ID: F011
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_dictionary_value

class TestDictionaryAccess(unittest.TestCase):

    def test_get_dictionary_value(self):
        """Test basic dictionary access"""
        d = {"name": "John", "age": 30}
        self.assertEqual(get_dictionary_value(d, "name"), "John")
        self.assertEqual(get_dictionary_value(d, "age"), 30)
    
    def test_get_dictionary_value_missing_key(self):
        """Test accessing non-existent key"""
        d = {"name": "John", "age": 30}
        self.assertEqual(get_dictionary_value(d, "city"), None)
        self.assertEqual(get_dictionary_value(d, "country"), None)
    
    def test_get_dictionary_value_empty_dict(self):
        """Test with empty dictionary"""
        self.assertEqual(get_dictionary_value({}, "any_key"), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
