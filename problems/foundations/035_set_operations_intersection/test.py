"""
Test cases for Set Operations (Intersection)
Problem ID: F035
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_intersection

class TestSetOperationsIntersection(unittest.TestCase):

    def test_get_intersection(self):
        self.assertEqual(get_intersection([1, 2, 3], [3, 4, 5]), {3})

if __name__ == '__main__':
    unittest.main(verbosity=2)
