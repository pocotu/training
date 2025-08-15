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

    def test_create_variables(self):
        """Test that the function returns the correct tuple of variables."""
        result = create_variables()
        self.assertIsInstance(result, tuple, "The function should return a tuple.")
        self.assertEqual(len(result), 4, "The tuple should have 4 elements.")
        
        integer_var, float_var, string_var, bool_var = result
        
        self.assertEqual(integer_var, 10)
        self.assertIsInstance(integer_var, int)
        
        self.assertEqual(float_var, 3.14)
        self.assertIsInstance(float_var, float)
        
        self.assertEqual(string_var, "Python")
        self.assertIsInstance(string_var, str)
        
        self.assertEqual(bool_var, True)
        self.assertIsInstance(bool_var, bool)

if __name__ == '__main__':
    unittest.main(verbosity=2)
