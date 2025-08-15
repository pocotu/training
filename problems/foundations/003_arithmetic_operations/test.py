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

    def test_perform_operations(self):
        """Test that the function performs the arithmetic operations correctly."""
        self.assertEqual(perform_operations(10, 5), (15, 5, 50, 2.0))
        self.assertEqual(perform_operations(20, 4), (24, 16, 80, 5.0))
        self.assertEqual(perform_operations(7, 2), (9, 5, 14, 3.5))

if __name__ == '__main__':
    unittest.main(verbosity=2)
