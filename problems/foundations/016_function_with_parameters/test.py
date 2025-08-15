"""
Test cases for Function with Parameters
Problem ID: F016
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import add

class TestFunctionWithParameters(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
