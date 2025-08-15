"""
Test cases for Sum of a List
Problem ID: F020
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import sum_list

class TestSumOfAList(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([]), 0)
        self.assertEqual(sum_list([-1, 1]), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
