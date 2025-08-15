"""
Test cases for String Length
Problem ID: F005
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_string_length

class TestStringLength(unittest.TestCase):

    def test_get_string_length(self):
        self.assertEqual(get_string_length("Hello"), 5)
        self.assertEqual(get_string_length(""), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
