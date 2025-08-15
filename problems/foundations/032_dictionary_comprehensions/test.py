"""
Test cases for Dictionary Comprehensions
Problem ID: F032
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_squared_dict

class TestDictionaryComprehensions(unittest.TestCase):

    def test_create_squared_dict(self):
        self.assertEqual(create_squared_dict([1, 2, 3]), {1: 1, 2: 4, 3: 9})

if __name__ == '__main__':
    unittest.main(verbosity=2)
