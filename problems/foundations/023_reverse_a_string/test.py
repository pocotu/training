"""
Test cases for Reverse a String
Problem ID: F023
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import reverse_string

class TestReverseAString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main(verbosity=2)
