"""
Test cases for Lambda Functions
Problem ID: F038
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import multiplier

class TestLambdaFunctions(unittest.TestCase):

    def test_multiplier(self):
        """Test basic lambda function"""
        self.assertEqual(multiplier(5), 50)
    
    def test_multiplier_zero(self):
        """Test with zero"""
        self.assertEqual(multiplier(0), 0)
    
    def test_multiplier_negative(self):
        """Test with negative number"""
        self.assertEqual(multiplier(-3), -30)
    
    def test_multiplier_is_lambda(self):
        """Test that multiplier is actually a lambda function"""
        self.assertTrue(callable(multiplier))
        self.assertEqual(multiplier.__name__, '<lambda>')

if __name__ == '__main__':
    unittest.main(verbosity=2)
