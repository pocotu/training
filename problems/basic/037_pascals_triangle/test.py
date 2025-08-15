"""
Test cases for Pascal's Triangle
Problem ID: 037
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import generate

class TestPascalsTriangle(unittest.TestCase):

    def test_example_1(self):
        expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        self.assertEqual(generate(5), expected)

    def test_example_2(self):
        expected = [[1]]
        self.assertEqual(generate(1), expected)

    def test_two_rows(self):
        expected = [[1], [1,1]]
        self.assertEqual(generate(2), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)