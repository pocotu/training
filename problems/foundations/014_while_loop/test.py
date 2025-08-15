"""
Test cases for While Loop
Problem ID: F014
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import count_down

class TestWhileLoop(unittest.TestCase):

    def test_count_down(self):
        self.assertEqual(count_down(5), [5, 4, 3, 2, 1])
        self.assertEqual(count_down(1), [1])
        self.assertEqual(count_down(0), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
