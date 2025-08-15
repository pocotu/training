"""
Test cases for Factorial Recursive
Problem ID: F042
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import factorial

class TestFactorialRecursive(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)

if __name__ == '__main__':
    unittest.main(verbosity=2)