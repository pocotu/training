"""
Test cases for Bubble Sort
Problem ID: F044
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(bubble_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([3, 3, 3]), [3, 3, 3])

if __name__ == '__main__':
    unittest.main(verbosity=2)