"""
Test cases for Merge Sorted Array
Problem ID: 028
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import merge

class TestMergeSortedArray(unittest.TestCase):

    def test_example_1(self):
        nums1 = [1,2,3,0,0,0]
        merge(nums1, 3, [2,5,6], 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_example_2(self):
        nums1 = [1]
        merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_empty_nums1(self):
        nums1 = [0]
        merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

if __name__ == '__main__':
    unittest.main(verbosity=2)