"""
Test cases for String join() method
Problem ID: F036
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import join_strings

class TestStringJoinMethod(unittest.TestCase):

    def test_join_strings(self):
        self.assertEqual(join_strings(["a", "b", "c"], "-"), "a-b-c")

if __name__ == '__main__':
    unittest.main(verbosity=2)
