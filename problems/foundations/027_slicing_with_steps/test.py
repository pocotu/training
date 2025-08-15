"""
Test cases for Slicing with Steps
Problem ID: F027
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_every_other_element

class TestSlicingWithSteps(unittest.TestCase):

    def test_get_every_other_element(self):
        self.assertEqual(get_every_other_element([1, 2, 3, 4, 5, 6]), [1, 3, 5])
        self.assertEqual(get_every_other_element(["a", "b", "c"]), ["a", "c"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
