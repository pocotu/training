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
        """Test that the function returns a dictionary with correct keys"""
        result = create_dictionary()
        
        # Verify it's a dictionary
        self.assertIsInstance(result, dict)
        
        # Verify it has the required keys
        required_keys = {'name', 'age', 'city'}
        self.assertEqual(set(result.keys()), required_keys)
        
        # Verify values are of correct types
        self.assertIsInstance(result['name'], str)
        self.assertIsInstance(result['age'], int)
        self.assertIsInstance(result['city'], str)

if __name__ == '__main__':
    unittest.main()
