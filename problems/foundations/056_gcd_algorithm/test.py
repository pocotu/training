"""
Test cases for GCD Algorithm
Problem ID: F056
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import gcd

class TestGCDAlgorithm(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(7, 7), 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)