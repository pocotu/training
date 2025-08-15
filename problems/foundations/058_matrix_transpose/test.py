"""
Test cases for Matrix Transpose
Problem ID: F058
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import transpose_matrix

class TestMatrixTranspose(unittest.TestCase):

    def test_transpose_matrix(self):
        self.assertEqual(transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(transpose_matrix([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])
        self.assertEqual(transpose_matrix([[1]]), [[1]])
        self.assertEqual(transpose_matrix([[1, 2, 3]]), [[1], [2], [3]])

if __name__ == '__main__':
    unittest.main(verbosity=2)