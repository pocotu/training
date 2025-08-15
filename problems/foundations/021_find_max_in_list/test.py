"""
Test cases for Find Max in List
Problem ID: F021
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import find_max

class TestFindMaxInList(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, -5, -3]), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
