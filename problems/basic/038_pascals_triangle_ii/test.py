"""
Test cases for Pascal's Triangle II
Problem ID: 038
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_row

class TestPascalsTriangleII(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(get_row(3), [1,3,3,1])

    def test_example_2(self):
        self.assertEqual(get_row(0), [1])

    def test_example_3(self):
        self.assertEqual(get_row(1), [1,1])

    def test_row_4(self):
        self.assertEqual(get_row(4), [1,4,6,4,1])

if __name__ == '__main__':
    unittest.main(verbosity=2)