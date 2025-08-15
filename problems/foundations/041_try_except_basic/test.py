"""
Test cases for Try-Except Basic
Problem ID: F041
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import safe_divide

class TestTryExceptBasic(unittest.TestCase):

    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5.0)
        self.assertEqual(safe_divide(15, 3), 5.0)
        self.assertEqual(safe_divide(10, 0), "Error: Division by zero")
        self.assertEqual(safe_divide(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)