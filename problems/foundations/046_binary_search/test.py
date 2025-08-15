"""
Test cases for Binary Search
Problem ID: F046
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11], 7), 3)
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 5), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(binary_search([], 1), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)