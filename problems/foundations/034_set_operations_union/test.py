"""
Test cases for Set Operations (Union)
Problem ID: F034
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_union

class TestSetOperationsUnion(unittest.TestCase):

    def test_get_union(self):
        self.assertEqual(get_union([1, 2, 3], [3, 4, 5]), {1, 2, 3, 4, 5})

if __name__ == '__main__':
    unittest.main(verbosity=2)
