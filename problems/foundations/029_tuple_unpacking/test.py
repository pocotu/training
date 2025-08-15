"""
Test cases for Tuple Unpacking
Problem ID: F029
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import unpack_tuple

class TestTupleUnpacking(unittest.TestCase):

    def test_unpack_tuple(self):
        a, b = unpack_tuple((10, 20))
        self.assertEqual(a, 10)
        self.assertEqual(b, 20)

if __name__ == '__main__':
    unittest.main(verbosity=2)
