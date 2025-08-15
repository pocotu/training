"""
Test cases for For Loop
Problem ID: F013
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import sum_list

class TestForLoop(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([]), 0)
        self.assertEqual(sum_list([-1, 1]), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
