"""
Test cases for Single Number
Problem ID: 041
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import single_number

class TestSingleNumber(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(single_number([2,2,1]), 1)

    def test_example_2(self):
        self.assertEqual(single_number([4,1,2,1,2]), 4)

    def test_example_3(self):
        self.assertEqual(single_number([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(single_number([-1,-1,2]), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)