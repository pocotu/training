"""
Test cases for Dictionary get() method
Problem ID: F030
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import get_value_safely

class TestDictionaryGetMethod(unittest.TestCase):

    def test_get_value_safely(self):
        d = {"name": "John", "age": 30}
        self.assertEqual(get_value_safely(d, "name"), "John")
        self.assertEqual(get_value_safely(d, "city"), "Not Found")

if __name__ == '__main__':
    unittest.main(verbosity=2)
