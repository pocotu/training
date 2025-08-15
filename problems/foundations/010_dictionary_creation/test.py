"""
Test cases for Dictionary Creation
Problem ID: F010
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_dictionary

class TestDictionaryCreation(unittest.TestCase):

    def test_create_dictionary(self):
        self.assertEqual(create_dictionary(), {"name": "John", "age": 30})

if __name__ == '__main__':
    unittest.main(verbosity=2)
