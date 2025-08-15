"""
Test cases for Prime Numbers
Problem ID: F055
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_prime

class TestPrimeNumbers(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

if __name__ == '__main__':
    unittest.main(verbosity=2)