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
        # Tests básicos
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(7, 7), 7)
        
        # Edge cases críticos
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 0), 0)
        
        # Casos adicionales
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(13, 1), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)