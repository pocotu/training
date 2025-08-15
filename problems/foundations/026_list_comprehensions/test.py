"""
Test cases for List Comprehensions
Problem ID: F026
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import square_numbers

class TestListComprehensions(unittest.TestCase):

    def test_square_numbers(self):
        self.assertEqual(square_numbers([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(square_numbers([]), [])
        self.assertEqual(square_numbers([-1, 0, 1]), [1, 0, 1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
