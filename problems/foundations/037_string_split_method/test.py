"""
Test cases for String split() method
Problem ID: F037
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import split_string

class TestStringSplitMethod(unittest.TestCase):

    def test_split_string(self):
        self.assertEqual(split_string("a-b-c", "-"), ["a", "b", "c"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
