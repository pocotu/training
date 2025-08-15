"""
Test cases for map() function
Problem ID: F039
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import square_list

class TestMapFunction(unittest.TestCase):

    def test_square_list(self):
        self.assertEqual(square_list([1, 2, 3]), [1, 4, 9])

if __name__ == '__main__':
    unittest.main(verbosity=2)
