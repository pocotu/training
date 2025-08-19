"""
Test cases for Dictionary Creation
Problem ID: F010
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_dictionary

class TestDictionaryCreation(unittest.TestCase):

    def test_create_dictionary(self):
        """Test that the function returns correct dictionary"""
        result = create_dictionary()
        expected = {"name": "John", "age": 30}
        
        # Verify it's a dictionary
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected)
    
    def test_create_dictionary_keys(self):
        """Test dictionary has correct keys"""
        result = create_dictionary()
        required_keys = {'name', 'age'}
        self.assertEqual(set(result.keys()), required_keys)
    
    def test_create_dictionary_values(self):
        """Test dictionary has correct value types"""
        result = create_dictionary()
        self.assertIsInstance(result['name'], str)
        self.assertIsInstance(result['age'], int)
        self.assertEqual(result['name'], "John")
        self.assertEqual(result['age'], 30)

if __name__ == '__main__':
    unittest.main()
