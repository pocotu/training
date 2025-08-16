"""
Test cases for Arithmetic Operations
Problem ID: F003
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import perform_operations

class TestArithmeticOperations(unittest.TestCase):

    def test_basic_operations(self):
        """Test basic arithmetic operations"""
        result = perform_operations(10, 5)
        expected = (15, 5, 50, 2.0)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = perform_operations(-10, 2)
        expected = (-8, -12, -20, -5.0)
        self.assertEqual(result, expected)
    
    def test_division_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            perform_operations(10, 0)

if __name__ == '__main__':
    unittest.main()
