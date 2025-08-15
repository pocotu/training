"""
Test cases for Iterating Dictionary Items
Problem ID: F031
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import format_dictionary

class TestIteratingDictionaryItems(unittest.TestCase):

    def test_format_dictionary(self):
        d = {"name": "John", "age": 30}
        self.assertEqual(sorted(format_dictionary(d)), sorted(["name: John", "age: 30"]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
