"""
Test cases for Set Creation and Unique Elements
Problem ID: F033
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_unique_elements

class TestSetCreationAndUniqueElements(unittest.TestCase):

    def test_get_unique_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
