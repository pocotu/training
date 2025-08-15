"""
Test cases for 2D Lists (Matrix Access)
Problem ID: F028
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_matrix_element

class Test2DLists(unittest.TestCase):

    def test_get_matrix_element(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(get_matrix_element(matrix, 0, 1), 2)
        self.assertEqual(get_matrix_element(matrix, 2, 0), 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)
