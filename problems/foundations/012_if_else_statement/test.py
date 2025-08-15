"""
Test cases for If-Else Statement
Problem ID: F012
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import check_number

class TestIfElseStatement(unittest.TestCase):

    def test_check_number(self):
        self.assertEqual(check_number(5), "Positive")
        self.assertEqual(check_number(-5), "Negative")
        self.assertEqual(check_number(0), "Zero")

if __name__ == '__main__':
    unittest.main(verbosity=2)
