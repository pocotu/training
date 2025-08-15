"""
Test cases for Class Instance
Problem ID: F019
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Person

class TestClassInstance(unittest.TestCase):

    def test_person_instance(self):
        person = Person("John")
        self.assertEqual(person.name, "John")

if __name__ == '__main__':
    unittest.main(verbosity=2)
