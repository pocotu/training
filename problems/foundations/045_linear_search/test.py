"""
Test cases for Linear Search
Problem ID: F045
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([2, 4, 6, 8, 10], 6), 2)
        self.assertEqual(linear_search([1, 3, 5, 7], 9), -1)
        self.assertEqual(linear_search([1, 2, 3, 2, 4], 2), 1)
        self.assertEqual(linear_search([], 5), -1)
        self.assertEqual(linear_search([5], 5), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)