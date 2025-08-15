"""
Test cases for List Flattening
Problem ID: F053
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import flatten_list

class TestListFlattening(unittest.TestCase):

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_list([['a', 'b'], ['c'], ['d', 'e', 'f']]), ['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main(verbosity=2)