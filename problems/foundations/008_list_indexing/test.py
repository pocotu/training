"""
Test cases for List Indexing
Problem ID: F008
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_list_element

class TestListIndexing(unittest.TestCase):

    def test_get_list_element(self):
        self.assertEqual(get_list_element([10, 20, 30], 1), 20)
        self.assertEqual(get_list_element(["a", "b", "c"], 0), "a")

if __name__ == '__main__':
    unittest.main(verbosity=2)
