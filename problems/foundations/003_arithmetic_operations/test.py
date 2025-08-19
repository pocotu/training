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
        """Test division by zero returns None for division"""
        result = perform_operations(10, 0)
        expected = (10, 10, 0, None)
        self.assertEqual(result, expected)
    
    def test_division_by_zero_negative(self):
        """Test division by zero with negative number"""
        result = perform_operations(-5, 0)
        expected = (-5, -5, 0, None)
        self.assertEqual(result, expected)
    
    def test_floating_point_operations(self):
        """Test with floating point numbers"""
        result = perform_operations(7.5, 2.5)
        expected = (10.0, 5.0, 18.75, 3.0)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
