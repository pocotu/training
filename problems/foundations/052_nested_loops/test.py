"""
Test cases for Nested Loops
Problem ID: F052
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import multiplication_table

class TestNestedLoops(unittest.TestCase):

    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        self.assertEqual(multiplication_table(2), [[1, 2], [2, 4]])
        self.assertEqual(multiplication_table(1), [[1]])
        self.assertEqual(multiplication_table(0), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)