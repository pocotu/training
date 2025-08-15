"""
Test cases for Check for Even/Odd
Problem ID: F022
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_even

class TestCheckForEvenOdd(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
