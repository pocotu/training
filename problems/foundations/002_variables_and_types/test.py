"""
Test cases for Variables and Types
Problem ID: F002
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_variables

class TestVariablesAndTypes(unittest.TestCase):

    def test_create_variables_types(self):
        """Test that the function returns correct types"""
        result = create_variables()
        
        # Verify it's a tuple with 4 elements
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        
        # Verify each element type and value
        self.assertIsInstance(result[0], int)
        self.assertEqual(result[0], 10)
        
        self.assertIsInstance(result[1], float)
        self.assertEqual(result[1], 3.14)
        
        self.assertIsInstance(result[2], str)
        self.assertEqual(result[2], "Python")
        
        self.assertIsInstance(result[3], bool)
        self.assertEqual(result[3], True)

if __name__ == '__main__':
    unittest.main()
